#!/usr/bin/env python

import sys
from providers.csv_reader import CSVReadException
from providers.file_csv_reader import FileCSVReader
from providers.sqlite_person_store import SQLitePersonStore
from providers.console_data_stats_printer import ConsoleDataStatsPrinter

dbName = "test.db"

csvReader = FileCSVReader()
dataStore = SQLitePersonStore(dbName)
dataStore.initialize()
dataStatsPrinter = ConsoleDataStatsPrinter()

csv_file_name = sys.argv[1]

try:
    dataList = csvReader.read(csv_file_name)
    dataStats = dataStore.save_person_list(dataList)
    dataStatsPrinter.print(dataStats)
except CSVReadException as csvReadError: 
    print(csvReadError)
except IOError:
    print("Could not read file: " + csv_file_name)
except:
    print("An error has occured")