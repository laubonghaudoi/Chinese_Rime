local users = {}
local M = {}

function M.init(env)
  local name = env.engine.schema.schema_id .. "_data"
  local data = require(name)
  users[name] = (users[name] or 0) + 1
  env.data_name = name
  env.data = data
end

function M.fini(env)
  local name = env.data_name
  if not name then
    return
  end
  local data = env.data
  env.data = nil
  env.data_name = nil
  users[name] = users[name] - 1
  if users[name] == 0 then
    users[name] = nil
    if package.loaded[name] == data then
      package.loaded[name] = nil
    end
    data = nil
    collectgarbage("collect")
  end
end

return M
