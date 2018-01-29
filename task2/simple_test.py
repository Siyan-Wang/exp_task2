import numpy as np
import pytest
import io

def test_built_in_functiton():
    #test using built-in function
    np.testing.assert_allclose(2.0/8.0,0.25,rtol=1e-5)
    
def test_array():
    #test using numpy.array
    np.testing.assert_allclose(np.divide(2.0,8.0),0.25,rtol=1e-5)
    

def test_input_size():
    f=open("task2/input.txt","rb")
    char=f.readline().strip().decode("utf-8")
    assert len(char)==6
