import fibl as fib

def test_answers():
  # Test Cases for the Function.
  a = 5
  b = 21
  c = 75025
  d = float("inf")
  
  # Evaluating the results.
  at = round(fib.Fibonacci(5))
  bt = round(fib.Fibonacci(8))
  ct = round(fib.Fibonacci(25))
  dt = fib.Fibonacci(2000)
  
  # Checking the known answers against our calculation.
  assert (a, b, c, d) == (at, bt, ct, dt)
