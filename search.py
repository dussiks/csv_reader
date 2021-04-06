import os
import sys

import reading


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
            output_data = reading.read_csv_file(file, keyword)
            if output_data:
                print(output_data)
