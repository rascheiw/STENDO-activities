# Command to run the app localy
# streamlit run ./streamlit_app/STENDO_activities.py --server.enableXsrfProtection false



#import pandas as pd
#import datetime
#from dateutil import relativedelta
#import matplotlib.pyplot as plt
from demo import Liste_des_clients_non_rentables, classement_nombre_moyen_par_jour, classement_nombre_par_jour, statistiques_par_clients
from data_processing import process_activity_data
import streamlit as st




#streamlit app 
# Title and presentation
st.sidebar.title("Statistiques des activités des consoles V4")
st.image('./figures/Logo.png')
st.sidebar.markdown("---")

# Streamlit function to upload a file
st.write("## Analyse des activités des consoles V4")
uploaded_file = st.file_uploader("Sélectionnez le fichier Excel contenant les activités", type=['xlsx'])
if uploaded_file is not None:
    sorted_activity_europe_50 = process_activity_data(uploaded_file)
else:
    st.write("Veuillez sélectionner un fichier pour continuer.")


# Streamlit sidebar menu to select the features to display
liste_menu = ['Liste des clients non rentables', 
              'Classement des 30 premiers clients européens en fonction du nombre moyen de séances par jour',
              'Classement des 30 premiers clients européens en fonction du nombre de séances', 
              'Statistiques par clients']
menu = st.sidebar.selectbox('Select the project presentation:', liste_menu)
if uploaded_file is not None:
    if menu == liste_menu[0]:
        Liste_des_clients_non_rentables(sorted_activity_europe_50)
    elif menu == liste_menu[1]:
        classement_nombre_moyen_par_jour(sorted_activity_europe_50)
    elif menu == liste_menu[2]:
        classement_nombre_par_jour(sorted_activity_europe_50)
    else:
        statistiques_par_clients(sorted_activity_europe_50)