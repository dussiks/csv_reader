#!/usr/bin/python
import csv
import logging
import os
import sys


REQUIRED_COLUMNS = ['open', 'high', 'low', 'close']
SEARCH_COLUMN = 'Name'


def check_data(data):
    """Checks if given data is a number and return it. If not - return 0."""
    try:
        number = float(data)
        return number
    except ValueError:
        return None


def calculate_average(datalist: list):
    """
    Summarize all values in given list and return average for values.
    If any data is not number - it is not considered into account.
    """
    datalist_sum = 0
    counter = 0
    for value in datalist:
        number = check_data(value)
        if number:
            datalist_sum += number
            counter += 1
    try:
        average = datalist_sum / counter
    except ZeroDivisionError:
        return None
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
        try:
            headers = reader.fieldnames
        except UnicodeError as error:
            return
        if SEARCH_COLUMN not in headers:
            return
        required_rows = [line for line in reader if line[SEARCH_COLUMN] == keyword]
        available_columns = [column for column in REQUIRED_COLUMNS if column in headers]
        if not (required_rows and available_columns):
            return
        answer = {}
        for column in available_columns:
            datalist = []
            for row in required_rows:
                datalist.append(row[column])
            average = calculate_average(datalist)
            try:
                answer[column] = round(average, 3)
            except Exception as e:
                return None
        return answer


def main():
    if len(sys.argv) != 3:
        print('Run app correctly - it should contain command, path and keyword.')
        sys.exit()

    directory = sys.argv[1]
    keyword = sys.argv[2]

    if not os.path.isdir(directory):
        print('No such directory or enter in correct format.')
        sys.exit()

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.csv'):
                os.chdir(root)
                output_data = read_csv_file(file, keyword)
                if output_data:
                    print(output_data)


if __name__ == '__main__':
    main()
