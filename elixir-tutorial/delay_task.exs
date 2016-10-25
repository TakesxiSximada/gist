foo = fn() -> Process.sleep(5000) end
tasks = for _ <- 1..10, true, do: Task.async(foo)
Task.yield_many(tasks)
