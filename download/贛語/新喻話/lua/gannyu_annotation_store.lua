local M = {}
local byte = string.byte
local sub = string.sub

local function u32(data, position)
  local a, b, c, d = byte(data, position, position + 3)
  assert(d, "truncated annotation index")
  return a + b * 256.0 + c * 65536.0 + d * 16777216.0
end

local function less(left, right)
  for position = 1, math.min(#left, #right) do
    local a, b = byte(left, position), byte(right, position)
    if a ~= b then
      return a < b
    end
  end
  return #left < #right
end

local function checksum(data)
  local a, b = 1.0, 0.0
  for first = 25, #data, 5552 do
    for position = first, math.min(first + 5551, #data) do
      a = a + byte(data, position)
      b = b + a
    end
    a, b = a % 65521, b % 65521
  end
  return b * 65536 + a
end

function M.open(name)
  assert(type(name) == "string" and name:match("^[A-Za-z0-9_-]+$"), "invalid annotation module")
  local source
  for template in package.path:gmatch("[^;]+") do
    local path = template:gsub("%?", name .. "_data")
    local module = io.open(path, "rb")
    if module then
      module:close()
      source = path
      break
    end
  end
  assert(source, "annotation data module not found: " .. name)
  local directory = source:match("^(.*[/\\])") or ""
  local file, failure = io.open(directory .. name .. "_annotations.bin", "rb")
  assert(file, failure)
  local ok, data = pcall(function()
    local length, seek_failure = file:seek("end")
    assert(length, seek_failure)
    assert(length >= 24, "invalid annotation format")
    local position, rewind_failure = file:seek("set", 0)
    assert(position, rewind_failure)
    local contents, read_failure = file:read(length)
    assert(contents, read_failure)
    assert(#contents == length, "truncated annotation data")
    local trailing, trailing_failure = file:read(1)
    assert(trailing_failure == nil, trailing_failure)
    assert(trailing == nil, "annotation size changed during read")
    return contents
  end)
  local closed, close_failure = file:close()
  assert(ok, data)
  assert(closed, close_failure)
  assert(#data >= 24 and sub(data, 1, 8) == "GNYANN01", "invalid annotation format")
  local count, size, name_size = u32(data, 9), u32(data, 13), u32(data, 17)
  local index = 25 + name_size
  local blob = index + count * 16
  assert(name_size == #name and sub(data, 25, index - 1) == name, "annotation region mismatch")
  assert(blob + size - 1 == #data, "annotation size mismatch")
  assert(checksum(data) == u32(data, 21), "annotation checksum mismatch")

  local function record(number)
    local position = index + (number - 1) * 16
    return u32(data, position), u32(data, position + 4),
      u32(data, position + 8), u32(data, position + 12)
  end

  local previous, cursor = nil, 0
  for number = 1, count do
    local key_offset, key_size, value_offset, value_size = record(number)
    assert(key_offset == cursor and value_offset == key_offset + key_size and
      value_offset + value_size <= size, "invalid annotation offsets")
    local key = sub(data, blob + key_offset, blob + key_offset + key_size - 1)
    assert(previous == nil or less(previous, key), "invalid annotation key order")
    previous, cursor = key, value_offset + value_size
  end
  assert(cursor == size, "unreferenced annotation data")

  return setmetatable({}, {
    __index = function(_, word)
      if type(word) ~= "string" then
        return nil
      end
      local first, last = 1, count
      while first <= last do
        local middle = math.floor((first + last) / 2)
        local key_offset, key_size, value_offset, value_size = record(middle)
        local key = sub(data, blob + key_offset, blob + key_offset + key_size - 1)
        if key == word then
          return sub(data, blob + value_offset, blob + value_offset + value_size - 1)
        elseif less(key, word) then
          first = middle + 1
        else
          last = middle - 1
        end
      end
      return nil
    end,
    __pairs = function()
      local number = 0
      return function()
        number = number + 1
        if number <= count then
          local key_offset, key_size, value_offset, value_size = record(number)
          return sub(data, blob + key_offset, blob + key_offset + key_size - 1),
            sub(data, blob + value_offset, blob + value_offset + value_size - 1)
        end
      end
    end,
  })
end

return M
