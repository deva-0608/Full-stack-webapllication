from flask import Flask, render_template, request, redirect, url_for,jsonify
app = Flask(__name__)
sales=[
  {
  'id':1,'name':'cats','location':'sydney','price':50000
  
},
{
  'id':2,'name':'birds','location':'India','price':20000
  
},
{
  'id':3,'name':'dogs','location':'london','price':40000
  
},
]
@app.route("/")
def hello():
  return render_template('home.html',jobs= sales)
@app.route("/sales")
def list_sales():
  return jsonify(sales)



if __name__=="__main__":
  app.run(debug=True)
  