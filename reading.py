import csv
import logging


REQUIRED_COLUMNS = ['open', 'high', 'low', 'close']
SEARCH_COLUMN = 'Names'


def check_data(data):
    """Checks if given data is a number and return it. If not - return 0."""
    try:
        number = float(data)
        return number
    except ValueError:
        return 0


def calculate_average(datalist: list):
    """Summarize all values in given list and return average for values."""
    datalist_sum = 0
    counter = 0
    for value in datalist:
        number = check_data(value)
        datalist_sum += number
        counter += 1
    try:
        average = datalist_sum / counter
    except ZeroDivisionError:
        return 0
    return average


def read_csv_file(csv_filename, keyword):
    """
    Function for calculating average number in each given at REQUIRED_COLUMNS
    column in file. For calculation taken only values in rows where keyword
    presents in SEARCH_COLUMN.
    :param csv_filename: file with .csv format required.
    :param keyword: word for searching in SEARCH_COLUMN. Exact match required.
    :return: dictionary with keys as names of columns listed in
    REQUIRED_COLUMNS that are found in csv_filename and with values that are
    equal to average calculated in function for each key.
    """
    with open(csv_filename, 'r') as File:
        reader = csv.DictReader(File)
        headers = reader.fieldnames
        if SEARCH_COLUMN not in headers:
            return None
        required_rows = [line for line in reader if line[SEARCH_COLUMN] == keyword]
        available_columns = [column for column in REQUIRED_COLUMNS if column in headers]
        if not (required_rows and available_columns):
            return None
        answer = {}
        for column in available_columns:
            datalist = []
            for row in required_rows:
                datalist.append(row[column])
            average = calculate_average(datalist)
            answer[column] = round(average, 3)
        return answer


print(read_csv_file('casdd.csv', 'AAPL'))
