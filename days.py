from datetime import datetime

def calculate_days_difference(start_date, end_date):
    """
    Calculate the difference in days between two dates.

    :param start_date: datetime, starting date
    :param end_date: datetime, ending date
    :return: int, number of days difference
    """
    return (end_date - start_date).days

# Define the dates
start_date = datetime(2023, 3, 7)
end_date = datetime(2023, 11, 13)

# Calculate and print the difference in days
days_difference = calculate_days_difference(start_date, end_date)
print(f"The difference is {days_difference} days.")
