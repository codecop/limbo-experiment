import pytest
from test_snake import Snake


@pytest.fixture
def snake():
    return Snake()
