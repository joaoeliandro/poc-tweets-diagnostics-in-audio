from ttdiagnosis.cli import init_cli


def test_initializing():
    assert init_cli() == 'initializing...'
