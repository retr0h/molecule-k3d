import pytest


@pytest.fixture
def DRIVER():
    """Return name of the driver to be tested."""
    return "k3d"
