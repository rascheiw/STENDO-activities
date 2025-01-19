import datetime

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