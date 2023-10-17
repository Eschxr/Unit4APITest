from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()

API_KEYS = ["pnmnyyyyss", "apsicbrthj"]

data = [
    {"name": "Samuel Wu", "age": "17", "favorite_game": "potty warriors"},
    {"name": "Laurence Yang", "age": "18", "favorite_game": "stardew valley"},
    {"name": "Joe Fernando", "age": "69", "favorite_game": "ET"},
    {"name": "Sam Xue", "age": "17", "favorite_game": "Oneshot"},
    {"name": "Jonathan Fernandes", "age": "34", "favorite_game": "Earthbound"},
    {"name": "Hudson Jones", "age": "16", "favorite_game": "Fortnite"},
    {"name": "Adriaan Cilliers", "age": "16", "favorite_game": "Single latinas in your area"},
    {"name": "Plus master", "age": "690", "favorite_game": "man of the chair"},
    {"name": "joe's nuts", "age": "2", "favorite_game": "nuts journey"},
    {"name": "josiah fernando", "age": "4", "favorite_game": "boomerang fu"},
    {"name": "james fernando", "age": "7", "favorite_game": "mario kart"},
    {"name": "Dumas Bozo", "age": "17", "favorite_game": "samuel wu adventures"},
    {"name": "Andy Zhang", "age": "18", "favorite_game": "Needy streamer overload"},
    {"name": "baldr", "age": "37", "favorite_game": "baldur's gate 3"},
    {"name": "pooper", "age": "42", "favorite_game": "man of the chair"},
    {"name": "Ben Dover", "age": "19", "favorite_game": "G.A.M.M.A"},
    {"name": "Harry Wang", "age": "16", "favorite_game": "Harry Potter's amazing adventures"},
    {"name": "Sarah Fernando", "age": "30", "favorite_game": "secret of the hidden fart room"},
    {"name": "Barac Obema", "age": "58", "favorite_game": "a mimir"},
    {"name": "pepe elpepe", "age": "16969", "favorite_game": "elpepe"}
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

@app.get("/funny")
def funny():
    return RedirectResponse(url="https://tinyurl.com/lawhousehold/")
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=6969, log_level="info", reload=True)