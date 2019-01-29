#!/usr/bin/env python

import sys
from providers.file_csv_reader import FileCSVReader
from providers.mock_data_store import MockDataStore
from providers.console_data_stats_printer import ConsoleDataStatsPrinter

csvReader = FileCSVReader()
dataStore = MockDataStore()
dataStatsPrinter = ConsoleDataStatsPrinter()

csv_file_name = sys.argv[1]

dataList = csvReader.read(csv_file_name)
dataStats = dataStore.saveDataList(dataList)
dataStatsPrinter.print(dataStats)