import streamlit as st
import pandas as pd
import datetime
from dateutil import relativedelta
import matplotlib.pyplot as plt
from demo import Liste_des_clients_non_rentables, classement_nombre_moyen_par_jour, classement_nombre_par_jour, statistiques_par_clients
import matplotlib.pyplot as plt

# Function to count the number of activities of a user in the last n days
def count_activity_last_n_days(df, user, n_days):
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=n_days)
    user_activity = df[df['full_name.1'] == user]
    last_n_days_activity = user_activity[
        (user_activity['start_date'].dt.date >= start_date) &
        (user_activity['start_date'].dt.date <= today)
    ]
    return len(last_n_days_activity)

# Function to display the number of years, months and days between two dates
def format_timedelta(start_date, end_date):
    delta = relativedelta.relativedelta(end_date, start_date)
    years = delta.years
    months = delta.months
    days = delta.days
    return f"{years} an(s), {months} mois, {days} jour(s)"   

@st.cache_data
def process_activity_data(uploaded_file):
    activity = pd.read_excel(uploaded_file)
    activity = activity.drop(columns=['mac_address', 'name', 'care_note', 'credit_number', 'active'])
    activity['percentage_real_duration'] = activity['real_duration'] / (activity['duration'] * 60) * 100
    activity_europe = activity[(activity['ps_server'] == 'EU') & (activity['spare_type'] == 'pants')]
    activity_europe = activity_europe[activity_europe['full_name.1'] != 'T0362 - LETESTEUR Ludovic']
    activity_europe_50 = activity_europe[activity_europe['percentage_real_duration'] >= 50]
    sorted_activity_europe_50 = activity_europe_50.groupby('full_name.1').size().reset_index(name='counts')
    first_activity_dates = activity_europe_50.groupby('full_name.1')['start_date'].min().reset_index()
    first_activity_dates.rename(columns={'start_date': 'first_activity'}, inplace=True)
    sorted_activity_europe_50 = pd.merge(sorted_activity_europe_50, first_activity_dates, on='full_name.1', how='left')
    last_activity_dates = activity_europe_50.groupby('full_name.1')['start_date'].max().reset_index()
    last_activity_dates.rename(columns={'start_date': 'last_activity'}, inplace=True)
    sorted_activity_europe_50 = pd.merge(sorted_activity_europe_50, last_activity_dates, on='full_name.1', how='left')
    sorted_activity_europe_50['first_activity'] = pd.to_datetime(sorted_activity_europe_50['first_activity'])
    sorted_activity_europe_50['number_days'] = 1 + (pd.to_datetime(datetime.date.today()) - sorted_activity_europe_50['first_activity']).dt.days
    activity_europe_50['start_date'] = pd.to_datetime(activity_europe_50['start_date'])
    activity_data = []
    for user in sorted_activity_europe_50['full_name.1']:
        activity_data.append({
            'full_name.1': user,
            'activity_last_7_days': count_activity_last_n_days(activity_europe_50, user, 7),
            'activity_last_14_days': count_activity_last_n_days(activity_europe_50, user, 14),
            'activity_last_30_days': count_activity_last_n_days(activity_europe_50, user, 30),
            'activity_last_90_days': count_activity_last_n_days(activity_europe_50, user, 90),
            'activity_last_365_days': count_activity_last_n_days(activity_europe_50, user, 365)
        })
    activity_df = pd.DataFrame(activity_data)
    sorted_activity_europe_50 = pd.merge(sorted_activity_europe_50, activity_df, on='full_name.1', how='left')
    sorted_activity_europe_50['activity_per_day_since_acquisition'] = sorted_activity_europe_50['counts'] / sorted_activity_europe_50['number_days']
    sorted_activity_europe_50['activity_per_day_7_days'] = sorted_activity_europe_50['activity_last_7_days'] / 5
    sorted_activity_europe_50['activity_per_day_14_days'] = sorted_activity_europe_50['activity_last_14_days'] / 10
    sorted_activity_europe_50['activity_per_day_30_days'] = sorted_activity_europe_50['activity_last_30_days'] / 20
    sorted_activity_europe_50['activity_per_day_90_days'] = sorted_activity_europe_50['activity_last_90_days'] / 55
    sorted_activity_europe_50['activity_per_day_year'] = sorted_activity_europe_50['activity_last_365_days'] / 220
    sorted_activity_europe_50 = sorted_activity_europe_50.round({'activity_per_day_since_acquisition': 2, 'activity_per_day_7_days': 2, 'activity_per_day_14_days': 2, 'activity_per_day_30_days': 2, 'activity_per_day_90_days': 2, 'activity_per_day_year': 2})
    sorted_activity_europe_50['rank_activity_7_days'] = sorted_activity_europe_50['activity_last_7_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_14_days'] = sorted_activity_europe_50['activity_last_14_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_30_days'] = sorted_activity_europe_50['activity_last_30_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_90_days'] = sorted_activity_europe_50['activity_last_90_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_year'] = sorted_activity_europe_50['activity_last_365_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_per_day_since_acquisition'] = sorted_activity_europe_50['activity_per_day_since_acquisition'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_per_day_7_days'] = sorted_activity_europe_50['activity_per_day_7_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_per_day_14_days'] = sorted_activity_europe_50['activity_per_day_14_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_per_day_30_days'] = sorted_activity_europe_50['activity_per_day_30_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_per_day_90_days'] = sorted_activity_europe_50['activity_per_day_90_days'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_per_day_year'] = sorted_activity_europe_50['activity_per_day_year'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['rank_activity_since_acquisition'] = sorted_activity_europe_50['counts'].rank(ascending=False, method='min').astype(int)
    sorted_activity_europe_50['percentage_total_activity_per_day'] = (sorted_activity_europe_50['activity_per_day_since_acquisition'] / sorted_activity_europe_50['activity_per_day_since_acquisition'].sum()) * 100
    sorted_activity_europe_50['cumulated_percentage_total_activity_per_day'] = sorted_activity_europe_50['percentage_total_activity_per_day'].cumsum()
    sorted_activity_europe_50['today'] = datetime.date.today()
    sorted_activity_europe_50['formatted_duration'] = sorted_activity_europe_50.apply(lambda row: format_timedelta(row['first_activity'], row['today']), axis=1)
    return sorted_activity_europe_50

st.sidebar.title("Statistiques des activités des consoles V4")
st.image('./figures/Logo.png')
st.sidebar.markdown('[Activités recénsées sur Axelor](https://axelor.stendo.net/#/ds/stendo-stendo-activity-action/list/1) ')
st.sidebar.markdown("---")

st.write("Upload the file")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    sorted_activity_europe_50 = process_activity_data(uploaded_file)
else:
    st.write("Please upload a file to proceed.")

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