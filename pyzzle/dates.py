from datetime import timedelta


def daterange_gen(start_date, end_date):
    """generator for all days between start and end date"""
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
