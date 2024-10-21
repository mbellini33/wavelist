# Funzione per ottenere le categorie di viaggio
import openai

def get_travel_categories():
    categories = [
        "Viaggi Avventurosi",
        "Viaggi Culturali",
        "Viaggi di Relax",
        "Viaggi di Affari",
        "Viaggi Romantici",
        "Viaggi Gastronomici",
        "Viaggi Naturali",
        "Viaggi di Studio",
        "Viaggi in Famiglia",
        "Viaggi di Lusso",
        "Viaggi Religiosi o Spirituali",
        "Viaggi Sostenibili"
    ]
    return categories

# Funzione per ottenere raccomandazioni di viaggio
def get_travel_recommendations(user_preferences):
    prompt = (
        f"Based on the following preferences, suggest some travel destinations:\n"
        f"Preferences: {user_preferences}\n"
        "Please provide a list of recommended destinations along with brief descriptions."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    recommendations = response.choices[0].message['content']
    return recommendations