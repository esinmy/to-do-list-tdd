# Useful Concepts

#### Expected failure
When a test fails in the way that we expected it to.

#### Functional Test
Functional Test == Acceptance Test == End-to-End Test

What I call functional tests, some people prefer to call acceptance tests, or end-to-end tests. The main point is that these kinds of tests look at how the whole application functions, from the outside. Another term is black box test, because the test doesn’t know anything about the internals of the system under test.

#### User Story
A description of how the application will work from the point of view of the user. 
Used to structure a functional test.

#### The unit-test/code cycle
1. Run the unit tests in the terminal.
2. Make a minimal code change in the editor.
3. Repeat!

#### Regression
When new code breaks some aspect of the application which used to work.

#### Unexpected failure
When a test fails in a way we weren’t expecting. This either means that we’ve made a mistake in our tests, or that the tests have helped us find a regression, and we need to fix something in our code.

#### Red/Green/Refactor
Another way of describing the TDD process. Write a test and see it fail (Red), write some code to get it to pass (Green), then Refactor to improve the implementation.

#### Triangulation
Adding a test case with a new specific example for some existing code, to justify generalising the implementation (which may be a "cheat" until that point).

#### Three strikes and refactor
A rule of thumb for when to remove duplication from code. When two pieces of code look very similar, it often pays to wait until you see a third use case, so that you’re more sure about what part of the code really is the common, re-usable part to refactor out.

#### The scratchpad to-do list
A place to write down things that occur to us as we’re coding, so that we can finish up what we’re doing and come back to them later.

#### Ensuring test isolation and managing global state
Different tests shouldn’t affect one another. This means we need to reset any permanent state at the end of each test. Django’s test runner helps us do this by creating a test database, which it wipes clean in between each test.

#### Avoid "voodoo" sleeps
Whenever we need to wait for something to load, it’s always tempting to throw in a quick-and-dirty time.sleep. But the problem is that the length of time we wait is always a bit of a shot in the dark, either too short and vulnerable to spurious failures, or too long and it’ll slow down our test runs. Prefer a retry loop that polls our app and moves on as soon as possible.

#### Don’t rely on Selenium’s implicit waits
Selenium does theoretically do some "implicit" waits, but the implementation varies between browsers, and at the time of writing was highly unreliable in the Selenium 3 Firefox driver. "Explicit is better than implict", as the Zen of Python says, so prefer explicit waits.

#### Working State to Working State (aka The Testing Goat vs. Refactoring Cat)
Our natural urge is often to dive in and fix everything at once…​but if we’re not careful, we’ll end up like Refactoring Cat, in a situation with loads of changes to our code and nothing working. The Testing Goat encourages us to take one step at a time, and go from working state to working state.

#### Split work out into small, achievable tasks
Sometimes this means starting with "boring" work rather than diving straight in with the fun stuff, but you’ll have to trust that YOLO-you in the parallel universe is probably having a bad time, having broken everything, and struggling to get the app working again.

#### YAGNI
You ain’t gonna need it! Avoid the temptation to write code that you think might be useful, just because it suggests itself at the time. Chances are, you won’t use it, or you won’t have anticipated your future requirements correctly.