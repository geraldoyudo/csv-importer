# csv-importer

The csv-importer reads entries in a csv file and persists them in an sqlite db. 

## Dependencies

1. Python 3.7 and above

## Getting Started 

All you need to do is pull the code and run import-csv.sh

~~~
git clone https://github.com/geraldoyudo/csv-importer
cd csv-importer
~~~

## Running the script

To run type the following

~~~
./import-csv.py [path/to/file.csv]
~~~

or 

~~~
./import-csv.sh [path/to/file.csv]
~~~

## Running the tests

To run the tests type the following:

~~~
python -m unittest
~~~

The csv format is depicted in [sample.csv](sample.csv). The input csv file must adhere to the following restrictions:

1. The first line is the csv header, comprising of the columns 
Please note, the first line is for the columns below: 

    a. first: First Name
    b. last: Last Name
    c. address: Person's address
    d. town: Town/city of residence
    e. state: State or Region
    f. zipcode: Zip/Postal code
    
2. Each row must have exactly 6 columns. Any row that does not have 6 columns will be ignored and will not be saved to the database

Once a valid csv file has been processed, it outputs the total number of rows, and the number of inserted rows. Invalid rows will be ignored.

## Usage Example

~~~
./import-csv.sh sample.csv
~~~

### Output

~~~
Number of records = 3
Number of inserted records = 3
~~~