from datetime import datetime
def days_until(date_string):
    future_date = datetime.strptime(date_string, "%Y-%m-%d")
    today = datetime.now()
    difference = future_date - today
    return difference.days