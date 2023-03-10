import streamlit as st
import requests
import json

st.title("Application d'ajout des entités")

#st.texts('Id : ')
id = st.number_input('id', step=1)
Libellé_entité = st.text_input('libellé_entité') 
contenu_entité = st.text_input('contenu_entité')

if st.button('Ajouter'):
	url = f"http://api_entite_micro_service:5000/entite/{id}"

	payload= json.dumps({
		"libellé_entité": libellé_entité,
		"contenu_entité": contenu_entité
	})

	headers = {
		'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	
	print (response.text)