
### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Installation](#Installation)
3. [Instructions](#instructions)
4. [File Descriptions](#files)
5. [Licensing, Authors, and Acknowledgements](#licensing)


## Project Motivation<a name="motivation"></a>

### Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity 
on their new music streaming app. The analysis team is particularly interested in understanding what 
songs users are listening to. Currently, there is no easy way to query the data to generate the results, 
since the data reside in a directory of CSV files on user activity on the app.

They'd like a data engineer to create an Apache Cassandra database with tables designed to optimize 
queries on song play analysis, and bring you on the project. The objective is to create a database 
and ETL pipeline for this analysis.
 
For example, they want to ask the following three question:
1. Provide the artist, song title and song's length in the music app history that was heard during 
`sessionId` = 338, and `itemInSession` = 4
2. Provide only the following: name of artist, song (sorted by `itemInSession`) and user (first and 
last name) for `userId` = 10, `sessionId` = 182
3. Provide every user name (first and last) in my music app history who listened to the song 
`All Hands Against His Own`.

### Dataset

The dataset is in `event_data` folder one dataset: event_data. The directory of CSV 
files partitioned by date. Here are examples of filepaths to two files in the dataset:

```
event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv
```


## Installation <a name="installation"></a>

1. [Anaconda distribution](https://www.anaconda.com/distribution/) of Python version 3.6 or later
2. [Apache Cassandra](https://cassandra.apache.org/doc/latest/getting_started/installing.html) 3.11 or later 


## Instructions<a name="instructions"></a>

Run the following command in the root directory to run the ETL.

`python etl.py`

To check the result, open and run cells in `etl_test.ipynb`




## File Descriptions <a name="files"></a>

Other than dataset, the main files consist of :
- `etl_test.ipynb` displays the first few rows of each table to let you check your database.
- `create_tables.py` drops and creates your tables. Run this file to reset tables before each time 
running ETL scripts.
- `etl.ipynb` notebook to reads and processes data and loads the data into tables.
- `etl.py` script to reads and processes data and loads the data into tables
- `queries.py` contains all queries, and is imported into the last three files above.
- `event_datafile_new.csv` created as a result of running `etl.ipynb` or `etl.py` as the main processed dataset file 
to load into tables.


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Udacity as part of Data Engineering NanoDegree Program
