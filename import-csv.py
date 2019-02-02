#!/usr/bin/env python

import sys
import os
import sqlite3
from providers.csv_reader import CSVReadException
from providers.file_csv_reader import FileCSVReader
from providers.sqlite_person_store import SQLitePersonStore
from providers.console_data_stats_printer import ConsoleDataStatsPrinter

try:
    dbName = os.getenv('CSV_IMPORTER_DB', "test.db")

    csvReader = FileCSVReader()
    dataStore = SQLitePersonStore(dbName)
    dataStore.initialize()
    dataStatsPrinter = ConsoleDataStatsPrinter()

    if len(sys.argv) > 1:
        csv_file_name = sys.argv[1]
        dataList = csvReader.read(csv_file_name)
        dataStats = dataStore.save_person_list(dataList)
        dataStatsPrinter.print(dataStats)
    else:
        print("Error: specify a file")
except CSVReadException as csvReadError: 
    print(csvReadError)
except FileNotFoundError:
    print("Error: File not found: " + csv_file_name)
except IOError:
    print("Error: Could not read file: " + csv_file_name)
except sqlite3.Error as databaseError:
    print("Error: A database error has occured: " + databaseError)
except:
    print("Error: An unexpected error has occured")