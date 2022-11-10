from flask import Flask, render_template, json
from flask import request, jsonify

app = Flask("app")

@app.route("/")

def index_page():
    return render_template("chats.html")


@app.route("/tests")

def test_page():
    return render_template("tests.html")




@app.route("/joks")

def joks():
    return render_template("joks.html")





@app.route("/chats/suuti", methods=["POST"])
def suuti_zinu():
    dati = request.json
    rindasTeksts = dati["chats"]
    atstarpesVieta = rindasTeksts.index(" : ")
    if rindasTeksts[atstarpesVieta+3] == "\\" and rindasTeksts[atstarpesVieta+4]=="d":
      with open("chats.txt", "w", newline="") as f:
        f.write("")
      return ielasit_chat()
      
    with open("chats.txt", "a", newline="") as f:
        f.write(rindasTeksts+"\n")
    return ielasit_chat()


@app.route("/chats/lasi")

def ielasit_chat():
    chata_rindas=[]
    with open("chats.txt", "r") as f:
        for rinda in f:
            chata_rindas.append(rinda)
    return jsonify({"chats":chata_rindas})



app.run(host='0.0.0.0', port=81)
