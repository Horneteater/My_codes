


import pytest
import random


def divide(x,y):
    return x/y
    
        
    
    
    
    

def test_divide():
   
    for i in range(2000000):
    	a=random.randint(-10,10)
    	b=random.randint(-10,10)
    	
    	if  b==0:
    		
    		with pytest.raises(ZeroDivisionError):
    			divide(a,b)
    	
    	else:
    		assert divide(a,b)== a/b	
    
   

#.   pytest   /storage/emulated/0/Programs/Test_c.py      