# Funzione per ottenere le categorie di viaggio
import openai
import requests
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)



def get_travel_recommendations(preferences,total_revenue):
    prompt_general = (
        f"Based on the following preferences, suggest some travel destinations:\n"
        f"Preferences: {preferences}\n"
        f"Reccommended destinations where the estimated revenue meets or exceeds {total_revenue}.\n")

    prompt_stops = "Provide a list of stops and detailed descriptions for each stop."
    prompt_costs = "Provide an estimated cost for each stop and the overall trip"


    response_gpt_35 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", 
            "content": f"{prompt_general}{prompt_stops}"}]
    )

    stops_gpt_35 = response_gpt_35.choices[0].message['content']

  
    ###GEMINI
    model = genai.GenerativeModel("gemini-1.5-flash-8b")
    prompt_gemini_foods = (
        f"Based on the following travel stops generated by GPT-3.5:\n\n"
        f"Preferences: {preferences}\n"
        f"{stops_gpt_35}\n\n"
        "Provide recommendations for local foods, popular restaurants, and unique attractions for each stop. "
        "Focus on local specialties, must-try dishes, and key cultural or natural attractions suitable for a relaxing experience."
    )
    
    attractions_gemini = model.generate_content(prompt_gemini_foods)
    ####################cultural#########################################
    prompt_gemini_cultural = (
        f"Based on the following travel stops generated by GPT-3.5:\n\n"
        f"Preferences: {preferences}\n"
        f"{stops_gpt_35}\n\n"
        f"{prompt_gemini_foods}\n\n"
        "Provide best cultural activities. "
    )
    
    cultural_gemini = model.generate_content(prompt_gemini_cultural)
    ####################################################################################BLOCCO CULTURALE
    #Creazione di una raccomandazione dettagliata e combinata
    combined_recommendations = (
    f"### Travel Recommendations ###\n\n"
    f"**Stops and Descriptions (GPT-3.5):**\n{stops_gpt_35}\n\n"
    f"**Food and Attractions (Gemini):**\n{attractions_gemini}\n\n"
    f"**Cultural Experiences (Geminil):**\n{cultural_gemini}\n"
    )

    print(combined_recommendations)


    return combined_recommendations