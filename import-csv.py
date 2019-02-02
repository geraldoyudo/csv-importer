#!/usr/bin/env python

import sys
from providers.file_csv_reader import FileCSVReader
from providers.sqlite_person_store import SQLitePersonStore
from providers.console_data_stats_printer import ConsoleDataStatsPrinter

dbName = "test.db"

csvReader = FileCSVReader()
dataStore = SQLitePersonStore(dbName)
dataStore.initialize()
dataStatsPrinter = ConsoleDataStatsPrinter()

csv_file_name = sys.argv[1]

dataList = csvReader.read(csv_file_name)
dataStats = dataStore.savePersonList(dataList)
dataStatsPrinter.print(dataStats)