import re   # Import the regular expressions module for pattern matching

# Sample medical records: each record is a dictionary with patient details
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


# Function to check validity of each field in a single record
def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    # Define validation rules for each field
    constraints = {
        # patient_id must be a string starting with 'p' or 'P' followed by digits
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\\d+', patient_id, re.IGNORECASE),

        # age must be an integer and at least 18
        'age': isinstance(age, int) and age >= 18,

        # gender must be a string and either 'male' or 'female' (case-insensitive)
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),

        # diagnosis must be a string or None
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # medications must be a list of strings
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),

        # last_visit_id must be a string starting with 'v' or 'V' followed by digits
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\\d+', last_visit_id, re.IGNORECASE)
    }

    # Return a list of keys that failed validation
    return [key for key, value in constraints.items() if not value]


# Function to validate the entire dataset
def validate(data):
    # Check if data is a list or tuple
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False
    # Expected set of keys in each record
    key_set = {'patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'}

    # Iterate through each record
    for index, dictionary in enumerate(data):
        # Check if each item is a dictionary
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        # Check if dictionary has exactly the expected keys
        if set(dictionary.keys()) != key_set:
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True
            continue

        # Validate fields inside the dictionary
        invalid_records = find_invalid_records(**dictionary)

        # Print details for each invalid field
        for key in invalid_records: 
            val = dictionary.get(key) 
            print(f"Unexpected format '{key}: {val}' at position {index}.")
            is_invalid = True

    # Final result: return False if any invalid record was found
    if is_invalid:
        return False
    print('Valid format.')
    return True


# Run validation on the sample medical_records
validate(medical_records)
