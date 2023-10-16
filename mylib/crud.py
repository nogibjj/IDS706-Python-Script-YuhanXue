import sqlite3
import csv

conn = sqlite3.connect('diabetes.db')
cur = conn.cursor()


def load(csvfile='diabetes.csv'):
    cur.execute('DROP TABLE IF EXISTS diabetes')
    conn.commit()
    cur.execute('''
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
        )
    ''')
    conn.commit()

    with open(csvfile, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute('''
                INSERT INTO diabetes (pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age,outcome) VALUES (?,?,?,?,?,?,?,?,?)
            ''', (row['Pregnancies'],row['Glucose'],row['BloodPressure'],row['SkinThickness'],row['Insulin'],row['BMI'],row['DiabetesPedigreeFunction'],row['Age'],row['Outcome']))
        conn.commit()

    print("succesfully loaded the database!")


def insert(pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age,outcome):
    cur.execute('INSERT INTO diabetes(pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age,outcome) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age,outcome))
    conn.commit()
    record = [pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age,outcome]
    print('Record successfully inserted: ' + ','.join(map(str, record)))


def read_all_records():
    cur.execute('SELECT * FROM diabetes')
    return cur.fetchall()


def read_record_id(id):
    cur.execute('SELECT * FROM diabetes WHERE id=?', (id,))
    res = cur.fetchone()
    print('Record ' + str(id) + ": ", res)
    return res


def update_record(id,pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age,outcome):
    cur.execute('UPDATE diabetes SET pregnancies=?, glucose=?, blood_pressure=?, skin_thickness=?, insulin=?, bmi=?, diabetes_pedigree_function=?, age=?, outcome=? WHERE id=?', (pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age,outcome,id))
    conn.commit()
    print('Update record ' + str(id) + ' successfully.')


def delete_record(id):
    cur.execute('DELETE FROM diabetes WHERE id=?', (id,))
    conn.commit()
    print("Delete record " + str(id) + ' successfully.')


def close_conn():
    cur.close()
    conn.close()



