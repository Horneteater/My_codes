
#basic calculator



while True:

  a=int(input("first number:"))

  opr=str(input(""" chose operation:
	×
	+
	-
	÷
	^
	
	"""))
	
  b=int(input("second number:"))
	

  if opr=="×":
  	c=a*b
  elif opr=="+":
	  c=a+b
  elif opr=="-":
  	c=a-b
  elif opr=="÷":
	  c=a/b
  elif opr=="^":
  	c=a**b
  
  
  else:
  	c="invalid"	
  	
	
	
  
  
  print("result is: ",c)
  
	
			
		