

array=[1,72,838,8284,5,62,73,9,61]
target=72
def linearsearch (array,target):
	if target in array:
	  for index in range(len(array)):
		  if array[index]==target:
		  	return index
	else:
		return "not here"
	
result=linearsearch(array,target)

print(result)