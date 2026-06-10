import datetime
def format_date(date):
    return date.strftime("%d-%m-%Y")
def is_valid_email(email):
    return "@" in email and "." in email
def truncate(text, length):
    return text[:length]