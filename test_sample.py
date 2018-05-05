import fibl as fib

def test(n):
  return round(fib.Fibonacci(n))

def test_answer():
  assert test(5) == 5
