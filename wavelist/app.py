from fastapi import FastAPI,Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
import openai
from functions import get_travel_recommendations
import logging

app = FastAPI()

print('hello')

print('hello')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Monta la cartella dei file statici
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura la tua API Key qui

# Rotta per la pagina iniziale con il form
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html") as f:
        return f.read()

# Rotta che riceve i dati e mostra le raccomandazioni
@app.post("/show-recommendations/", response_class=HTMLResponse)
async def show_recommendations(
    selected_category: str = Form(...), 
    trip_duration: int = Form(...), 
    number_people: int = Form(...)
):
    
    #Business Filter
    
    if number_people == 6:
       total_revenue = 4000

    elif number_people == 7:
       total_revenue = 5000
    
    elif number_people == 8:
       total_revenue = 6000
    
    elif number_people == 9:
       total_revenue = 7000

    elif number_people == 10:
       total_revenue = 8000

    elif number_people < 6:
        total_revenue = 8000

    else : 
        total_revenue = 10000
    
def print():
    return "hello"

    # Crea le preferenze di viaggio
    preferences = {
        'category': selected_category,
        'duration': trip_duration,
        'people': number_people
    }

    # Chiama la funzione di raccomandazione importata da functions.py
    recommendations = get_travel_recommendations(preferences,total_revenue)
    
    if isinstance(recommendations, dict):
        return JSONResponse(content=recommendations)
    else:
        return HTMLResponse(content=f"<html><body><h1>Travel Recommendations</h1><p>{recommendations}</p></body></html>")

    