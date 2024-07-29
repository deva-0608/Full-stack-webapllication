from flask import Flask, render_template, request, redirect, url_for,jsonify
from db import list_pet,listpet



app = Flask(__name__)







  

# for free database try planetscale
@app.route("/")
def hello():
  sales= list_pet()
  return render_template('home.html',jobs= sales)
@app.route("/sales")
def list_sales():
  sales= list_pet()
  return jsonify(sales)
@app.route("/sales/<id>")
def show_pet(id):
  pet=listpet(id)
  if  not pet:
    return "not found",404
  return  render_template('salespage.html',sales=pet,id=id)
  
# @app.route("/sales/<id>/order")
# def placing(id):
#   return ("user application is sent successfully on id %d",id)


if __name__=="__main__":
  app.run(debug=True)
  