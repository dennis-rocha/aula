from flask import Flask,request

from db import data

app = Flask(__name__)

def message(message,status_code = 200):
    return {
        "message" : message
    },status_code

@app.get("/")
def main_page():
    return "Olá Mundo!"

@app.get("/user")
def get_user():
    return data

@app.post("/user")
def post_user():
    raw_data:dict = request.get_json()
    for i in ["nome", "email", "idade"]:
        if not i in raw_data.keys():
            return message(f"Não contém o campo '{i}' na requisição", 400)
        
    data.append({
        "nome" : raw_data.get("nome"),
        "email" : raw_data.get("email"),
        "idade" : raw_data.get("idade"),

    })

    return message("Ok",201)

  
@app.get("/user/<int:id>")
def get_user_id(id):
    print(id,type(id))
    try:
        return message(data[id], 200)
    except:
        return message(f"Usuário {id} não encontrado", 404)

 
@app.put("/user/<int:id>")
def put_user_id(id):
    try:
        raw_data = data[id]
    except:
        return message(f"Usuário {id} não encontrado", 404)

    index = data.index(raw_data)

    raw_dict:dict = request.get_json()
    nome = raw_dict.get("nome")
    email =  raw_dict.get("email")
    idade =  raw_dict.get("idade")

    if nome:
        raw_data["nome"] = nome
    
    if email:
        raw_data["email"] = email

    if idade:
        raw_data["idade"] = idade

    data.pop(index)
    data.insert(index,raw_data)

    return("Dados atualizados com sucesso!",201)


@app.delete("/user/<int:id>")
def delete_user_id(id):
    try:
        raw_data = data[id]
    except:
        return message(f"Usuário {id} não encontrado", 404)
    
    index = data.index(raw_data)

    data.pop(index)

    return message("Usuário removido com sucesso!")