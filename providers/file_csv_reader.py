from providers.csv_reader import CSVReader, CSVReadException
import csv

column_list = ["first", "last", "address", "town", "state", "zipcode"]
column_list_length = len(column_list)
INVALID_DATA = {}
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
                        if len(row) != column_list_length:
                            raise CSVReadException("Column length should be equal to " + column_list_length)
                        if column in column_list:
                            columns.append(column.strip())
                        else:
                            raise CSVReadException("invalid column header in file")
                else:
                    if len(row) != column_list_length:
                        dataList.append(INVALID_DATA)
                    else:
                        data = {}
                        for i in range(column_list_length):
                            data[columns[i]] = row[i].strip()
                        dataList.append(data)
                line_count += 1
        
        return dataList
