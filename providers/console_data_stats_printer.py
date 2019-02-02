from providers.data_stats_printer import DataStatsPrinter

class ConsoleDataStatsPrinter(DataStatsPrinter):
    def print(self, data_save_stats):
        print("Number of records = " + str(data_save_stats.totalRecords))
        print("Number of inserted records = " + str(data_save_stats.totalSavedRecords))
