# IDS706-Python-Script-YuhanXue

![format workflow](https://github.com/nogibjj/IDS706-Python-Script-YuhanXue/actions/workflows/cicd.yml/badge.svg)

This project 7 contains Python scripts/functions that perform CRUD operations in SQLite through command line.

## Formatting and Erorrs
Please run `make all` to ensure all codes are well-formatted and free of errors.

## Schema of diabetes data
Here is the SQL query used to create the table:
```SQL
CREATE TABLE IF NOT EXISTS diabetes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pregnancies INTEGER,
                glucose INTEGER,
                blood_pressure INTEGER,
                skin_thickness INTEGER,
                insulin INTEGER,
                bmi INTEGER,
                diabetes_pedigree_function DOUBLE,
                age INTEGER,
                outcome INTEGER
        );
```


## Command Manual
First, load all data from diabetes.csv to the SQLite database with the following command:
```
python3 main.py load
```

To insert a record, issue the following command (9 values in parentheses, comma-separated):
```
python3 main.py insert -a "(...)"
```

To delete a record, issue the following command (without brace):
```
python3 main.py delete -a [id]
```


To update a record, issue the following command (last argument should be a tuple start with id, 10 values in parentheses, comma-separated):
```
python3 main.py update -a "(id, ...)"
```


To read a record with id, issue the following command (without brace):
```
python3 main.py read -a [id]
```


## Functions in mylib/crud.py
1. load: load a csv file to diabetes database. All row ids are created automatically by SQLite. 
2. insert: insert an individual record into diabetes table.
3. read_all_records: fetch all rows and all attributes from diabetes table.
4. read_record_id: fetch the content of one row by its id.
5. update_record: update a record given a row id and all values that this record should be updated to.
6. delete_record: delete a record given a row id.
7. close_conn: close database connection.
