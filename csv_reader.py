#!/usr/bin/python
import csv
import os
import sys

from logger import get_logger


REQUIRED_COLUMNS = ['open', 'high', 'low', 'close']
SEARCH_COLUMN = 'Name'

logger = get_logger(__name__)


def check_data(data):
    """Checks if given data is a number and return it. If not - return 0."""
    try:
        number = float(data)
        return number
    except ValueError:
        logger.warning(f'Not number obtained in current column.')
        return None


def calculate_average(datalist: list):
    """
    Summarize all values in given list and return average for values.
    If any data is not number - it is not considered into account.
    """
    datalist_sum = 0
    counter = 0
    for element in datalist:
        number = check_data(element)
        if number:
            datalist_sum += number
            counter += 1
    try:
        average = datalist_sum / counter
    except ZeroDivisionError as e:
        logger.error(f'Error occurred during average calculation: {e}.')
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
    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file)
        try:
            headers = reader.fieldnames
        except UnicodeError as e:
            logger.error(f'During reading {file.name} error occurred: {e}')
            return None
        if SEARCH_COLUMN not in headers:
            logger.warning(f'No column "{SEARCH_COLUMN}" in {file.name}')
            return None
        required_rows = [row for row in reader if row[SEARCH_COLUMN] == keyword]
        available_columns = [column for column in REQUIRED_COLUMNS
                             if column in headers]
        if not (required_rows and available_columns):
            logger.warning(f'No required data found in {file.name}')
            return None
        answer = {}
        for column in available_columns:
            datalist = []
            for row in required_rows:
                datalist.append(row[column])
            average = calculate_average(datalist)
            try:
                answer[column] = round(average, 3)
                logger.info(f'Average for column "{column}": {average}.')
            except Exception as e:
                logger.error(f'Error with average rounding occurred in'
                             f'column "{column}": {e}.')
                return None
        return answer


def main():
    logger.info(f'App initialized with {sys.argv[1]} and {sys.argv[2]}.')
    if len(sys.argv) != 3:
        logger.error('App started with incorrect arguments - not equal 3.')
        print('Run app correctly - should contain command, path and keyword.')
        sys.exit()

    directory = sys.argv[1]
    keyword = sys.argv[2]

    if not os.path.isdir(directory):
        logger.error(f'Directory {sys.argv[1]} not found.')
        print('No such directory or enter in correct format.')
        sys.exit()

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.csv'):
                logger.info(f'.csv file found in directory: {root}')
                os.chdir(root)
                output_data = read_csv_file(file, keyword)
                if output_data:
                    logger.info(f'Next results found: {output_data}')
                    print(output_data)


if __name__ == '__main__':
    main()
