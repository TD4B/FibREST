import fibl as fib

def test_answer():
  a = 5
  b = 21
  c = 75025
  at = round(fib.Fibonacci(5))
  ab = round(fib.Fibonacci(8))
  ac = round(fib.Fibonacci(25))
  assert (a,b,c) == (at,ab,ac)
