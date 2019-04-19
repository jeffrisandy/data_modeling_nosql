import os
import glob
import csv
from queries import *
import create_tables


def get_file_path_list():
    """
    Get the filepath of all csv files in event_data folder
    INPUT: None
    RETURN: a list of filepath for all csv files in event_data folder
    """
    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):
        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root, '*'))

    return file_path_list


def get_data_rows():
    """
    Read and get all data in csv files in event_data folder
    INPUT: None
    RETURN: a lits of data 
    """
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = []

    # for every filepath in the file path list 
    for f in get_file_path_list():

        # reading csv file
        with open(f, 'r', encoding='utf8', newline='') as csvfile:
            # creating a csv reader object 
            csvreader = csv.reader(csvfile)
            next(csvreader)

            # extracting each data row one by one and append it
            for line in csvreader:
                full_data_rows_list.append(line)

    return full_data_rows_list


def create_event_data():
    """
    Creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into tables
    INPUT: None
    RETURN: None
    """

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length', \
                         'level', 'location', 'sessionId', 'song', 'userId'])
        for row in get_data_rows():
            if row[0] == '':
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))


def insert_session_data(session, filepath):
    """
    Insert data to session table session
    INPUT:
        session: connection to database
        filepath: string, filepath to event_datafile_new.csv
    RETURN: None
    """
    with open(filepath, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            session.execute(session_table_insert,
                            (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))


def insert_user_data(session, filepath):
    """
    Insert data to user table
    INPUT:
        session: connection to database
        filepath: string, filepath to event_datafile_new.csv
    RETURN: None
    """

    with open(filepath, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            session.execute(user_table_insert,
                            (int(line[10]), int(line[8]), int(line[3]), line[0], line[9], line[1], line[4]))


def insert_song_data(session, filepath):
    """
    Insert data to song table
    INPUT:
        session: connection to database
        filepath: string, filepath to event_datafile_new.csv
    RETURN: None
    """

    with open(filepath, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            session.execute(song_table_insert,
                            (line[9], int(line[10]), line[1], line[4]))


def main():
    """
    Main program for etl.py
    INPUT: None
    RETURN: None
    """

    # create event data
    create_event_data()
    print("Created event_datafile_new.csv")

    # create tables
    create_tables.main()
    print("Created tables")

    # connect to db
    session, cluster = create_tables.connect_db()

    # event data filepath
    file = 'event_datafile_new.csv'

    # insert data to session table
    insert_session_data(session, file)
    print("Inserted data to session_history table")

    # insert data to user table
    insert_user_data(session, file)
    print("Inserted data to user_history table")

    # insert data to song table
    insert_song_data(session, file)
    print("Inserted data to song_history table")

    # close session and disconnect cluster
    create_tables.disconnect_db(session, cluster)
    print("ETL Completed")


if __name__ == "__main__":
    main()
