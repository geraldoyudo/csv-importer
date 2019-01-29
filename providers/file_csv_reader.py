from providers.csv_reader import CSVReader
import csv

class FileCSVReader(CSVReader):
    def read(self, sourceName = "source.csv"):
        dataList = []
        columns = []
        
        with open(sourceName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    for column in row:
                        columns.append(column.strip())
                else:
                    data = {}
                    for i in range(len(row)):
                        data[columns[i]] = row[i].strip()
                    dataList.append(data)
                line_count += 1
        
        return dataList
