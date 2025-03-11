# Hospital Bed Allocation System
# Filename: hospital_bed.py
# Create a `HospitalBed` class with:
# - `bed_number`
# - `patient_name` (default `None`)
# Implement methods:
# - `assign_bed(patient_name)` → Assigns a patient to the bed.
# - `release_bed()` → Frees up the bed

class HospitalBed:
    def __init__(self, bed_number):
        self.bed_number = bed_number
        self.patient_name = None  # Bed is free by default

    def assign_bed(self, patient_name):
        if self.patient_name is not None:
            print(f"Bed {self.bed_number} is already occupied by {self.patient_name}.")
        else:
            self.patient_name = patient_name
            print(f"Bed {self.bed_number} has been assigned to {self.patient_name}.")

    def release_bed(self):
        if self.patient_name is None:
            print(f"Bed {self.bed_number} is already free.")
        else:
            print(f"Bed {self.bed_number} has been released by {self.patient_name}.")
            self.patient_name = None