from datetime import datetime

def get_days_from_today(date):
    try:
        current_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

    today = datetime.today().date()
    delta = (current_date - today).days
    return delta
print(get_days_from_today("2021-10-09"))