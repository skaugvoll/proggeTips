"""
The core of Wove's functionality is the weave context manager.
It is used in a with block to define a list of tasks that will be executed as concurrently and as soon as possible.
When Python closes the weave block,
the tasks are executed immediately based on a dependency graph that Wove builds from the function signatures.
Results of a task are passed to any same-named function parameters.
The result of the last task that runs are available in w.result.final.
"""

import time

from wove import weave

with weave() as w:
  # These first two tasks run concurrently.
  @w.do
  def magic_number():
    time.sleep(1.0)
    return 42

  @w.do
  def important_text():
    time.sleep(1.0)
    return "The meaning of life"

  # This task depends on the first two. It runs only after both are complete.
  @w.do
  def combined(important_text, magic_number):
    return f"{important_text} is {magic_number}!"


# NOTE: only when the `with` block closes, all tasks are executed.
print(w.result.final)
# >> The meaning of life is 42!
print(f"The magic number was {w.result.magic_number}")
# >> The magic number was 42
print(f'The important text was "{w.result["important_text"]}"')
# >> The important text was "The meaning of life"
