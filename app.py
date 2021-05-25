from flask import Flask, redirect, url_for, render_template, request, flash

from pymongo import MongoClient


app=Flask("app")

client=MongoClient("mongodb://127.0.0.1:27017")
mydb = client["mydatabase"]
mycol = mydb["customers"]
list=[]

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/output",methods=["GET"])
def dia():
    x1=int(request.args.get("n1"))
    x2=int(request.args.get("n2"))
    x3=int(request.args.get("n3"))
    x4=int(request.args.get("n4"))
    x5=int(request.args.get("n5"))
    x6=float(request.args.get("n6"))
    x7=float(request.args.get("n7"))
    x8=int(request.args.get("n8"))
    mydb.mycol.insert({"n1":x1,"n2":x2,"n3":x3,"n4":x4,"n5":x5,"n6":x6,"n7":x7,"n8":x8})
    output=client["mydb"]["mycol"].find({})
    for i in output:
        print(i)
    return "Hello"
    
    
