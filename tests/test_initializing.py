from ttdiagnosis.cli import __main__

def test_initializing():
  assert __main__() == "initializing..."