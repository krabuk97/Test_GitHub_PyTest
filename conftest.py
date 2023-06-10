import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "run(order): run test in specified order"
    )
