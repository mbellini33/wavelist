# Funzione per ottenere le categorie di viaggio
import openai

############################################
# Funzione per ottenere raccomandazioni di viaggio
def get_travel_recommendations(preferences):
    prompt = (
        f"Based on the following preferences, suggest some travel destinations:\n"
        f"Preferences: {preferences}\n"
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