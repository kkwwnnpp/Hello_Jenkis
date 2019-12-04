import pytest
from HelloWorld import *

#This is a test, Hello Jenkins!

def test_hello():
    result = hello()
    assert result == "Hello!"
    
#full auto
