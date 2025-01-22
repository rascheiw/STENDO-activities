# Imge python
FROM python:3.10.2

LABEL Raphaël SCHEIWILLER <rascheiw@gmail.com>

# Répertoire de travail du conteneur
WORKDIR /app

# Copie du fichier de requirements
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install -r requirements.txt

# Copie des fichiers de l'application dans le conteneur
COPY ./streamlit_app/count_activity_last_n_days.py ./
COPY ./streamlit_app/STENDO_activities.py ./
COPY ./streamlit_app/demo.py ./
COPY ./streamlit_app/data_processing.py ./
COPY ./streamlit_app/format_timedelta.py ./
COPY ./figures/Logo.png ./figures/

# Exposition du port 8501
EXPOSE 8501

# Démarrage de l'application Streamlit
CMD ["streamlit", "run", "STENDO_activities.py"]