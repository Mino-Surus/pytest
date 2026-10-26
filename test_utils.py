from utils import generate_code, read_from_sum
from unittest.mock import patch
import pytest
import os

def test_generate_code():
    code = generate_code()
    assert len(code) == 6, "Длина чето там"
    assert code.isdigit()


