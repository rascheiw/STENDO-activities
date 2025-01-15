import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import os

# Définir la variable globale activity
activity = None

# Lire le fichier des activités dans le répertoire courant et retourner une erreur si le fichier n'est pas trouvé
def read_activities_file():
    global activity
    try:
        activity = pd.read_excel("./activity.xlsx")
    except FileNotFoundError:
        st.error("Fichier non trouvé. Assurez-vous que le fichier s'appelle 'activity.xlsx' et qu'il est dans le même répertoire que le script.")
        return None
    return activity

# Afficher le fichier des activités
def display_activities():
    activities = read_activities_file()
    if activities is not None:
        st.write(activities)

# Appeler la fonction pour afficher les activités
read_activities_file()

activity = activity.drop(columns=['mac_address', 'name', 'care_note', 'credit_number', 'active'])
activity['percentage_real_duration'] = activity['real_duration'] / (activity['duration'] * 60) * 100
activity_europe = activity[(activity['ps_server'] == 'EU') & (activity['spare_type'] == 'pants')]
activity_europe = activity_europe[activity_europe['full_name.1'] != 'T0362 - LETESTEUR Ludovic']
activity_europe_50 = activity_europe[activity_europe['percentage_real_duration'] >= 50]
#activity_europe_50 = activity_europe_50.sort_values(by=['full_name.1'])

# Calculer le nombre d'activités, la date de la première activité, la date de la dernière activité et le nombre de jours entre les deux
sorted_activity_europe_50 = activity_europe_50.groupby('full_name.1').size().reset_index(name='counts')
first_activity_dates = activity_europe_50.groupby('full_name.1')['start_date'].min().reset_index()
first_activity_dates.rename(columns={'start_date': 'first_activity'}, inplace=True)
sorted_activity_europe_50 = pd.merge(sorted_activity_europe_50, first_activity_dates, on='full_name.1', how='left')
last_activity_dates = activity_europe_50.groupby('full_name.1')['start_date'].max().reset_index()
last_activity_dates.rename(columns={'start_date': 'last_activity'}, inplace=True)
sorted_activity_europe_50 = pd.merge(sorted_activity_europe_50, last_activity_dates, on='full_name.1', how='left')
sorted_activity_europe_50['first_activity'] = pd.to_datetime(sorted_activity_europe_50['first_activity'])
sorted_activity_europe_50['last_activity'] = pd.to_datetime(sorted_activity_europe_50['last_activity'])
sorted_activity_europe_50['number_days'] = 1+ (sorted_activity_europe_50['last_activity'] - sorted_activity_europe_50['first_activity']).dt.days

# Ensure 'start_date' in activity_europe_50 is datetime
activity_europe_50['start_date'] = pd.to_datetime(activity_europe_50['start_date'])

def count_activity_last_week(df, user):
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=7)
    user_activity = df[df['full_name.1'] == user]
    last_week_activity = user_activity[
        (user_activity['start_date'].dt.date >= last_week) &
        (user_activity['start_date'].dt.date <= today)
    ]
    return len(last_week_activity)


activity_last_week = []
for user in sorted_activity_europe_50['full_name.1']:
    activity_last_week.append(count_activity_last_week(activity_europe_50, user))

sorted_activity_europe_50['activity_last_week'] = activity_last_week

# Ensure 'start_date' in activity_europe_50 is datetime
activity_europe_50['start_date'] = pd.to_datetime(activity_europe_50['start_date'])

def count_activity_last_2_weeks(df, user):
    today = datetime.date.today()
    two_weeks_ago = today - datetime.timedelta(days=14)
    user_activity = df[df['full_name.1'] == user]
    last_2_weeks_activity = user_activity[
        (user_activity['start_date'].dt.date >= two_weeks_ago) &
        (user_activity['start_date'].dt.date <= today)
    ]
    return len(last_2_weeks_activity)

activity_last_2_week = []
for user in sorted_activity_europe_50['full_name.1']:
    activity_last_2_week.append(count_activity_last_2_weeks(activity_europe_50, user))

sorted_activity_europe_50['activity_last_2_week'] = activity_last_2_week


def count_activity_last_30_days(df, user):
    today = datetime.date.today()
    month_ago = today - datetime.timedelta(days=30)
    user_activity = df[df['full_name.1'] == user]
    last_month_activity = user_activity[
        (user_activity['start_date'].dt.date >= month_ago) &
        (user_activity['start_date'].dt.date <= today)
    ]
    return len(last_month_activity)

activity_last_30_days = []
for user in sorted_activity_europe_50['full_name.1']:
    activity_last_30_days.append(count_activity_last_30_days(activity_europe_50, user))

sorted_activity_europe_50['activity_last_30_days'] = activity_last_30_days

def count_activity_last_90_days(df, user):
    today = datetime.date.today()
    month_3_ago = today - datetime.timedelta(days=90)
    user_activity = df[df['full_name.1'] == user]
    last_3_month_activity = user_activity[
        (user_activity['start_date'].dt.date >= month_3_ago) &
        (user_activity['start_date'].dt.date <= today)
    ]
    return len(last_3_month_activity)

activity_last_90_days = []
for user in sorted_activity_europe_50['full_name.1']:
    activity_last_90_days.append(count_activity_last_90_days(activity_europe_50, user))

sorted_activity_europe_50['activity_last_90_days'] = activity_last_90_days

def count_activity_last_year(df, user):
    today = datetime.date.today()
    year_ago = today - datetime.timedelta(days=365)
    user_activity = df[df['full_name.1'] == user]
    last_year_activity = user_activity[
        (user_activity['start_date'].dt.date >= year_ago) &
        (user_activity['start_date'].dt.date <= today)
    ]
    return len(last_year_activity)

activity_last_year = []
for user in sorted_activity_europe_50['full_name.1']:
    activity_last_year.append(count_activity_last_year(activity_europe_50, user))

sorted_activity_europe_50['activity_last_year'] = activity_last_year


sorted_activity_europe_50['activity_per_day_since_acquisition'] = sorted_activity_europe_50['counts'] / sorted_activity_europe_50['number_days']
sorted_activity_europe_50['activity_per_day_7_days'] = sorted_activity_europe_50['activity_last_week'] / 7
sorted_activity_europe_50['activity_per_day_14_days'] = sorted_activity_europe_50['activity_last_2_week'] / 14
sorted_activity_europe_50['activity_per_day_30_days'] = sorted_activity_europe_50['activity_last_30_days'] / 30
sorted_activity_europe_50['activity_per_day_90_days'] = sorted_activity_europe_50['activity_last_90_days'] / 90
sorted_activity_europe_50['activity_per_day_year'] = sorted_activity_europe_50['activity_last_year'] / 365

sorted_activity_europe_50 = sorted_activity_europe_50.sort_values(by=['activity_per_day_since_acquisition'], ascending=False)

sorted_activity_europe_50['rank_activity_7_days'] = sorted_activity_europe_50['activity_last_week'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_14_days'] = sorted_activity_europe_50['activity_last_2_week'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_30_days'] = sorted_activity_europe_50['activity_last_30_days'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_90_days'] = sorted_activity_europe_50['activity_last_90_days'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_year'] = sorted_activity_europe_50['activity_last_year'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_per_day_since_acquisition'] = sorted_activity_europe_50['activity_per_day_since_acquisition'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_per_day_7_days'] = sorted_activity_europe_50['activity_per_day_7_days'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_per_day_14_days'] = sorted_activity_europe_50['activity_per_day_14_days'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_per_day_30_days'] = sorted_activity_europe_50['activity_per_day_30_days'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_per_day_90_days'] = sorted_activity_europe_50['activity_per_day_90_days'].rank(ascending=False, method='min').astype(int)
sorted_activity_europe_50['rank_activity_per_day_year'] = sorted_activity_europe_50['activity_per_day_year'].rank(ascending=False, method='min').astype(int)


sorted_activity_europe_50['percentage_total_activity_per_day'] = (sorted_activity_europe_50['activity_per_day_since_acquisition'] / sorted_activity_europe_50['activity_per_day_since_acquisition'].sum()) * 100


sorted_activity_europe_50['cumulated_percentage_total_activity_per_day'] = sorted_activity_europe_50['percentage_total_activity_per_day'].cumsum()


def format_timedelta(days):
    years = days // 365
    months = (days % 365) // 30
    remaining_days = (days % 365) % 30
    return f"{years} an(s), {months} mois, {remaining_days} jour(s)"

sorted_activity_europe_50['formatted_duration'] = sorted_activity_europe_50['number_days'].apply(format_timedelta)





# Liste des clients non rentables sur 7 jours
display_unprofitable_clients_activity_per_days_7_days = sorted_activity_europe_50[sorted_activity_europe_50['activity_last_week'] < 1.25][['full_name.1', 'activity_last_week']].sort_values(by=['activity_last_week'], ascending=False)
display_unprofitable_clients_activity_per_days_7_days = display_unprofitable_clients_activity_per_days_7_days.rename(columns={
    'full_name.1' : 'Nom du client',
    'activity_last_week': 'Nombre moyen séance par jours sur les 7 derniers jours',
        })
print(f"Il y a {len(display_unprofitable_clients_activity_per_days_7_days)} clients non rentables sur les 7 derniers jours")
display(display_unprofitable_clients_activity_per_days_7_days.style.hide(axis='index'))