local WINDOW_SIZE = 24
local MIN_FREQUENCY = 250000

local function is_single_character(text)
  return utf8.len(text or "") == 1
end

local function frequency(candidate, data)
  return data.single_character_frequencies[candidate.text] or 0
end

local function is_eligible(candidate, anchor, data)
  return (candidate.type == "phrase" or candidate.type == "user_phrase")
    and candidate._end < anchor._end
    and is_single_character(candidate.text)
    and frequency(candidate, data) >= MIN_FREQUENCY
end

local M = {}

function M.func(input, env)
  local data = env.data
  local next_candidate, state = input:iter()
  local anchor = next_candidate(state)
  if not anchor then
    return
  end

  local buffered = {}
  for _ = 1, WINDOW_SIZE do
    local candidate = next_candidate(state)
    if not candidate then
      break
    end
    table.insert(buffered, candidate)
  end

  local best_index = nil
  for index, candidate in ipairs(buffered) do
    if is_eligible(candidate, anchor, data)
      and (best_index == nil or frequency(candidate, data) > frequency(buffered[best_index], data)) then
      best_index = index
    end
  end

  yield(anchor)
  if best_index then
    yield(buffered[best_index])
  end
  for index, candidate in ipairs(buffered) do
    if index ~= best_index then
      yield(candidate)
    end
  end
  while true do
    local candidate = next_candidate(state)
    if not candidate then
      break
    end
    yield(candidate)
  end
end

function M.init(env)
  env.data = require(env.engine.schema.schema_id .. "_data")
end

return M
