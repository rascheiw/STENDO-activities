from dateutil import relativedelta

# Function to display the number of years, months and days between two dates
def format_timedelta(start_date, end_date):
    delta = relativedelta.relativedelta(end_date, start_date)
    years = delta.years
    months = delta.months
    days = delta.days
    return f"{years} an(s), {months} mois, {days} jour(s)"  