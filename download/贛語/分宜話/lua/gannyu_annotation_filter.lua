local function clean_spelling(comment)
  return (comment or ""):gsub("^G", ""):gsub(" G", " ")
end

local function sentence_reading(text, data)
  local readings = {}
  for character in text:gmatch("[%z\1-\127\194-\244][\128-\191]*") do
    local reading = data.readings[character]
    if not reading then
      return nil
    end
    table.insert(readings, reading)
  end
  return table.concat(readings, " ")
end

local M = {}

function M.func(input, env)
  local data = env.data
  for candidate in input:iter() do
    candidate.comment = data.annotations[candidate.text]
      or sentence_reading(candidate.text, data)
      or clean_spelling(candidate.comment)
    yield(candidate)
  end
end

function M.init(env)
  env.data = require(env.engine.schema.schema_id .. "_data")
end

return M
