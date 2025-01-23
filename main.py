from fastapi import FastAPI, HTTPException
from typing import Union

app = FastAPI()

# Simulated database for the "nodered" endpoint
nodered_data = {}

# POST: Ajouter un nouvel élément dans la base nodered
@app.post("/nodered")
def post_nodered(item_id: int, q: Union[str, None] = None):
    """
    Crée un nouvel élément pour Node-RED.
    :param item_id: Identifiant de l'élément (obligatoire).
    :param q: Une requête ou un paramètre optionnel.
    :return: Les données ajoutées.
    """
    if item_id in nodered_data:
        raise HTTPException(status_code=400, detail="Item already exists.")
    nodered_data[item_id] = {"item_id": item_id, "query": q}
    return {"message": "Item added successfully.", "data": nodered_data[item_id]}

# GET: Récupérer un élément spécifique depuis l'endpoint nodered
@app.get("/nodered/{item_id}")
def get_nodered(item_id: int):
    """
    Récupère un élément Node-RED par son ID.
    :param item_id: Identifiant de l'élément.
    :return: Les données associées à cet ID.
    """
    if item_id not in nodered_data:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"data": nodered_data[item_id]}

# PUT: Mettre à jour un élément existant dans nodered
@app.put("/nodered/{item_id}")
def put_nodered(item_id: int, q: Union[str, None] = None):
    """
    Met à jour un élément existant dans Node-RED.
    :param item_id: Identifiant de l'élément à mettre à jour.
    :param q: Nouvelle requête ou paramètre optionnel.
    :return: Les données mises à jour.
    """
    if item_id not in nodered_data:
        raise HTTPException(status_code=404, detail="Item not found.")
    nodered_data[item_id]["query"] = q
    return {"message": "Item updated successfully.", "data": nodered_data[item_id]}