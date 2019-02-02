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

    csv_reader = FileCSVReader()
    person_store = SQLitePersonStore(dbName)
    person_store.initialize()
    data_stats_printer = ConsoleDataStatsPrinter()

    if len(sys.argv) > 1:
        csv_file_name = sys.argv[1]
        data_list = csv_reader.read(csv_file_name)
        data_stats = person_store.save_person_list(data_list)
        data_stats_printer.print(data_stats)
    else:
        print("Error: specify a file")
except CSVReadException as csv_read_error: 
    print(csv_read_error)
except FileNotFoundError:
    print("Error: File not found: " + csv_file_name)
except IOError:
    print("Error: Could not read file: " + csv_file_name)
except sqlite3.Error as database_error:
    print("Error: A database error has occured: " + database_error)
except:
    print("Error: An unexpected error has occured")