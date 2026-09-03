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

local function annotate(candidate, data)
  candidate.comment = data.annotations[candidate.text]
    or sentence_reading(candidate.text, data)
    or clean_spelling(candidate.comment)
  return candidate
end

local function related(source, text, quality, data)
  local candidate = Candidate("gannyu_relation", source.start, source._end, text, data.annotations[text] or "")
  candidate.quality = quality
  return candidate
end

local function emit_relations(source, words, seen, offset, data)
  if not words then
    return
  end
  for _, word in ipairs(words) do
    if not seen[word] then
      seen[word] = true
      yield(related(source, word, source.quality + offset, data))
    end
  end
end

local M = {}

function M.func(input, env)
  local data = env.data
  local seen = {}
  for candidate in input:iter() do
    if not seen[candidate.text] then
      emit_relations(candidate, data.before[candidate.text], seen, 0.01, data)
      if not seen[candidate.text] then
        seen[candidate.text] = true
        yield(annotate(candidate, data))
      end
      emit_relations(candidate, data.after[candidate.text], seen, -0.02, data)
    end
  end
end

function M.init(env)
  env.data = require(env.engine.schema.schema_id .. "_data")
end

return M
