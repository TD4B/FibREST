import fibl as fib

def test(x):
  return round(fib.Fibonacci(x))

def test_answer():
  assert test(5) == 5
