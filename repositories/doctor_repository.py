from db.run_sql import run_sql

from models.doctor import Doctor
from models.patient import Patient

# Save new doctor to the database
# ---------------------------------
def save(doctor):
    sql = "INSERT INTO doctors(name) VALUES (%s) RETURNING id"
    values = [doctor.name]
    results = run_sql( sql, values )
    doctor.id = results[0]['id']
    return doctor


# Select all saved doctors from database and return
# ---------------------------------
def select_all():
    doctors = []

    sql = "SELECT * FROM doctors"
    results = run_sql(sql)

    for row in results:
        doctor = Doctor(row['name'], row['id'])
        doctors.append(doctor)
    return doctors


# Select one doctors from the database and return
# ---------------------------------
def select(id):
    doctor = None

    sql = "SELECT * FROM doctors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        doctor = Doctor(result['name'], result['id'] )
    return doctor

# Delete all from doctors table
# ---------------------------------
def delete_all():
    sql = "DELETE FROM doctors"
    run_sql(sql)

# Delete one doctor from table
# ---------------------------------
def delete(id):
    sql = "DELETE  FROM doctors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Update the details of selected doctor
# ---------------------------------
def update(doctor):
    sql = "UPDATE doctors SET name = %s WHERE id = %s"

    values = [doctor.name, doctor.id]
    run_sql( sql, values )