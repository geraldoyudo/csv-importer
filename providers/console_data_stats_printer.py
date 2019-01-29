from providers.data_stats_printer import DataStatsPrinter

class ConsoleDataStatsPrinter(DataStatsPrinter):
    def print(self, dataSaveStats):
        print("Number of records = " + str(dataSaveStats.totalRecords))
        print("Number of inserted records = " + str(dataSaveStats.totalSavedRecords))