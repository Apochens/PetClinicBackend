from PetClinicBackend.utils import read_csv_data
from management.models import Department, Medicine


def init_department():
    rows = read_csv_data('department.csv')
    for row in rows:
        save_department(row)

def save_department(row):
    d = Department()
    d.id = int(row[0])
    d.name = row[1]
    d.description = row[2]
    d.save()

def init_medicine():
    rows = read_csv_data('medicine.csv')
    for row in rows:
        save_medicine(row)

def save_medicine(row):
    d = Medicine()
    d.id = int(row[0])
    d.name = row[1]
    d.type = row[2]
    d.tag = row[3]
    d.price = row[4]
    d.description = row[5]
    d.save()