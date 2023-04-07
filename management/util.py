from datetime import datetime

from PetClinicBackend.utils import read_csv_data
from case.models import Case
from management.models import Department, Medicine, Instrumentation, Checkup, Hospitalization


def init_department():
    rows = read_csv_data('department.csv')
    for row in rows:
        save_department(row)

def save_department(row):
    d = Department()
    d.id = row[0]
    d.name = row[1]
    d.description = row[2]
    d.save()

def init_medicine():
    rows = read_csv_data('medicine.csv')
    for row in rows:
        save_medicine(row)

def save_medicine(row):
    d = Medicine()
    d.id = row[0]
    d.name = row[1]
    d.type = row[2]
    d.tag = row[3]
    d.price = row[4]
    d.description = row[5]
    d.save()

def init_instrumentation():
    rows = read_csv_data('instrumentation.csv')
    for row in rows:
        save_instrumentation(row)

def save_instrumentation(row):
    d = Instrumentation()
    d.id = row[0]
    d.dept_id = Department.objects.get(id=row[1])
    d.name = row[2]
    d.description = row[3]
    d.method = row[4]
    d.save()

def init_checkup():
    rows = read_csv_data('checkup.csv')
    for row in rows:
        save_checkup(row)

def save_checkup(row):
    d = Checkup()
    d.id = row[0]
    d.dept_id = Department.objects.get(id=row[1])
    d.name = row[2]
    d.price = row[3]
    d.description = row[4]
    d.save()

def init_hospitalization():
    rows = read_csv_data('hospitalization.csv')
    for row in rows:
        save_hospitalization(row)

def save_hospitalization(row):
    d = Hospitalization()
    d.id = row[0]
    d.case_id = row[1]
    # assert Case.objects.get(id=d.case_id) is not None
    d.price = row[2]
    d.bg_time = datetime.strptime(row[3], '%Y/%m/%d')
    d.ed_time = datetime.strptime(row[4], '%Y/%m/%d')
    assert d.ed_time >= d.bg_time
    d.save()