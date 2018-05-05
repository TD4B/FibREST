import fibl as fib

def test(x):
  return round(fib.Fibonacci(x))

def test_answer():
  assert type(test(5)) == type(int)
