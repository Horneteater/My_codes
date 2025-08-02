

#date time and day of today

import requests

url="https://api.keybit.ir/time/"

response=requests.get(url)

data=response.json()


i1=data["date"]["full"]["official"]["iso"]["fa"]

print(i1)

i4=data["date"]["weekday"]["name"]

print(i4)

i5=data["date"]["other"]["gregorian"]["iso"]["en"]

print(i5)

i2=data["date"]["day"]["events"]["holy"]["text"]

i3=data["date"]["day"]["events"]["holy"]["holiday"]

if i3==True:
	print(i2)
	print(".تعطیل.")
else:
	print(" تعطیل نیست")


