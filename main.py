from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()

API_KEYS = ["pnmnyyyyss", "apsicbrthj"]

class Item(BaseModel):
    name: str
    age: str
    favgame: str | None = "bababooey"

data = [
    Item(name="Samuel Wu", age="17", favgame="potty warriors"),
    Item(name="Laurence Yang", age="18", favgame="stardew valley"),
    Item(name="Joe Fernando", age="69", favgame="ET"),
    Item(name="Sam Xue", age="17", favgame="Oneshot"),
    Item(name="Jonathan Fernandes", age="34", favgame="Earthbound"),
    Item(name="Hudson Jones", age="16", favgame="Fortnite"),
    Item(name="Adriaan Cilliers", age="16", favgame="Single latinas in your area"),
    Item(name="Plus master", age="690", favgame="man of the chair"),
    Item(name="joe's nuts", age="2", favgame="nuts journey"),
    Item(name="josiah fernando", age="4", favgame="boomerang fu"),
    Item(name="james fernando", age="7", favgame="mario kart"),
    Item(name="Dumas Bozo", age="17", favgame="samuel wu adventures"),
    Item(name="Andy Zhang", age="18", favgame="Needy streamer overload"),
    Item(name="baldr", age="37", favgame="baldur's gate 3"),
    Item(name="pooper", age="42", favgame="man of the chair"),
    Item(name="Ben Dover", age="19", favgame="G.A.M.M.A"),
    Item(name="Harry Wang", age="16", favgame="Harry Potter's amazing adventures"),
    Item(name="Sarah Fernando", age="30", favgame="secret of the hidden fart room"),
    Item(name="Barac Obema", age="58", favgame="a mimir"),
    Item(name="pepe elpepe", age="16969", favgame="elpepe")
]

@app.get("/")
def home_route():
    return "Buncha peeps and their favorite games"

@app.get("/names")
async def get_names(api_key: str = None):
    if api_key in API_KEYS:
        names = []
        for person in data:
            names.append(person["name"])
        return names
    return "ACCESS DENIED"

@app.get("/names/{name}")
async def get_person(name: str, api_key: str = None):
    if api_key in API_KEYS:
        for person in data:
            if name in person["name"]:
                return person
    return "ACCESS DENIED"

@app.post("/names/")
async def add_person(name: Item, api_key: str = None):
    if api_key in API_KEYS:
        data.append(name)
        return "Action SUCCESSFUL"
    return "ACCESS DENIED"

@app.get("/funny")
def funny():
    return RedirectResponse(url="https://tinyurl.com/lawhousehold/")
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)