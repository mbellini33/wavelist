import streamlit as st
import polars 


# Interfaccia utente in Streamlit
st.title("Travel Recommendation App")

# Mostra il dataframe caricato per verifica
st.write("Destinations available:")

# Input dall'utente per il budget
budget = st.number_input("Enter your maximum budget (€)", min_value=100, max_value=10000, step=100)

# Selectbox opzionale per la categoria di viaggio
selected_category = st.selectbox(
    "Select a travel category (optional)", 
    ["Nessuna preferenza", "Relax", "Adventure", "Culture", "Nature"]
)

# Slider per la durata del viaggio e numero di persone
trip_duration = st.slider("Trip duration (days)", 1, 30)
number_people = st.slider("Number of people", 1, 10)

# Quando l'utente clicca sul bottone
if st.button("Get Recommendations"):
    # Filtra le destinazioni nel dataframe in base al budget

        
        # Genera raccomandazioni con OpenAI
    #recommendations = get_travel_recommendations(combined_preferences)
        
    st.write("Recommended destinations based on your preferences:")
    #st.write(recommendations)
    st.write('Hello')
else:
        st.write("No destinations found within your budget.")