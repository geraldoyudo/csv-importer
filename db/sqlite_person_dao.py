import sqlite3
from db.person_entity import INVALID_PERSON

def create_table(db):
    db.execute('''create table if not exists person
                    (
                        id integer primary key , 
                        first text not null,
                        last text not null,
                        address text not null,
                        town text not null,
                        state text not null,
                        zipcode text not null
                    )''')

def commit_and_close_connection(connection):
    connection.commit()
    connection.close()

def convert_person_entity_list_to_tupule_list(person_entity_list):
    data_list = []
    for data in person_entity_list:
        if data == INVALID_PERSON:
            continue
        data_list.append(tuple((data.first, data.last, data.address,
        data.town, data.state, data.zipcode)))
    return data_list


class SQLiteRecordPersonDAO:
    db = "test.db"

    def __init__(self, db):
        self.db = db

    def intialize_database(self):
        conn = sqlite3.connect(self.db)
        db = conn.cursor()
        create_table(db)
        commit_and_close_connection(conn)
    
    def save_data_entities(self, person_entity_list):
        dataList = convert_person_entity_list_to_tupule_list(person_entity_list)
        conn = sqlite3.connect(self.db)
        db = conn.cursor()
        db.executemany("insert into person(first,last,address,town,state,zipcode) values (?,?,?,?,?,?)", dataList)
        commit_and_close_connection(conn)
        return db.rowcount