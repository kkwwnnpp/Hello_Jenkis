import pytest
from HelloWorld import *

def test_hello():
    result = hello()
    assert result == "Hello!"
    
