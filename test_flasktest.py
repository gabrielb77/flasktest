

# content of test_sample.py
def inc(x):
  return x + 1


def test_answer():
  assert inc(3) == 4

# test.py
def test_always_passes():
  assert True

def test_always_fails():
  assert False

def test_GetRandom():
  import flasktest

  assert flasktest.GetRandom.len > 1