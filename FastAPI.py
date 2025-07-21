

From fastAPI import FastAPI
#here we import the used framework

App=FastAPI() 
#To initialize an app instance


@app.get("/route" ) 
Async Def hi():
  Return "hi" 
#to define HTTP method and Url of API endpoint, followed by the function that our API would use



#Now when our url is hit with an HTTP, fast API would return the string "hi". 