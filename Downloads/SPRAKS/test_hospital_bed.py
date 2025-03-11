import pytest
from hospital_bed import HospitalBed

def test_hospital_bed():
    # Create a bed with number 101
    bed = HospitalBed(101)
    
    # Check that the bed is correctly initialized
    assert bed.bed_number == 101  # Bed number should be 101
    assert bed.patient_name is None  # Bed should be free initially
    
    # Assign a patient to the bed
    bed.assign_bed("Michael")
    assert bed.patient_name == "Michael"  # Patient should now be assigned to the bed
    
    # Release the bed
    bed.release_bed()
    assert bed.patient_name is None  # Bed should be free after release