

import pytest


def add(x,y):
    return x+y
    
    
    
    


@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (2,3,5),
    (10,5,15),
])
def test_add(a, b, expected):
    assert add(a,b)== expected    

#.  pytest   /storage/emulated/0/Programs/test_a.py        


# pytest --showlocals --html=report.html --self-contained-html /storage/emulated/0/Programs/test_a.py        
  