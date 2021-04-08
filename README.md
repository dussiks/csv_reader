# csv reader

Console application for calculation average value in desired columns in *.csv file located at given directory.

# App running conditions
## Required arguments
1. Directory as local path or full path - .csv file will be looking for in this directory or in folders inside it.
2. Keyword - word that will be looking for inside .csv file in column with name 'Name'. Exact match required.

## Starting app format
`python csv_reader.py ~/date SPENT`

## Searching key moments
1. .csv file and given directory should exist. Otherwise, app will return specific note and stop running.
2. .csv file should contain columns with names: 'date', 'open', 'high', 'low', 'close', 'volume', 'Name'


# Calculation scheme
## Data collection
App looking for keyword in column with name 'Name'. If it is, row will be considered during calculations.
Average value will be calculated only for columns with next names inside file: 'open', 'high', 'low', 'close'.

## Average calculation
For each desired column value in row passes validation process if it is a number. If yes - it will be used in calculations, else - no.  If between 4 values one is not a number - average calculated for 3 values.

# Output form
If no relevant .csv file, or no values inside, None will be returned.
If such file detected, answer will be as:

```{'low': 67.035, 'close': 67.525, 'high': 68.875, 'open': 68.096}```
