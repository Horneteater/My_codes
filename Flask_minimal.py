from flask import Flask

app=Flask(__name__)

@app.route('/')
def chat():
	#use flask requests
	
	massage='hi'
	
	return massage
	
if __name__== "__main__":
	app.run(debug=True)	
	