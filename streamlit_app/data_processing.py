import pandas as pd
import datetime
import streamlit as st
from format_timedelta import format_timedelta
from count_activity_last_n_days import count_activity_last_n_days

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
    sorted_activity_europe_50['activity_per_day_since_acquisition'] = sorted_activity_europe_50['counts'] / ( sorted_activity_europe_50['number_days'] * 0.87)
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