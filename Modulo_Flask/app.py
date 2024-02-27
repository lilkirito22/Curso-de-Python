from flask import Flask

app= Flask(__name__)


#CRUD
#Create, Read, Update and Delete 

@app.route("/")
def hello_world():
  return "Ola Mundo"

@app.route("/cars")
def cars():
  return "Formula 1"
if __name__ == "__main__":
  app.run(debug=True)

  