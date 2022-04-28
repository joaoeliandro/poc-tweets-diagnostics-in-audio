from ttdiagnosis.cli import init

def test_initializing():
  assert init() == "initializing..."