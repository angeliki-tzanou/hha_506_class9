import numpy as np

np.greetings("Ang")

import pandas as pd

pd.greetings("A")


# Number variable
number_variable = 3

# String variable
string_variable = "Hello my name is Angeliki but people call me Ang"

# List variable- birthday
A_list = [8, 3, 2001]

# Dictionary
my_dictionary = {
    "Patient's name": "Jane Doe",
    "pt age": 33,
    "chief complaints": ["coughing", "shortness of breath", "chest pain"],
    " family history": {
        "maternal aunt": "lung cancer at 55 years old",
        "paternal aunt": "COPD",
        "sister": "adenocarcinoma at 78 years old"
    }

}

def evaluation_of_cancer_symptoms (age, symptoms):
    symptoms = ["chronic cough", "feeling of weakness or tiredness", "coughing up blood", "chest pain"]
    has_any_cancer_symptoms = any(symptoms)

    if age <= 65:
        print("low cancer risk")
    elif has_any_cancer_symptoms:
        print("High cancer risk patient:", symptoms)
    else:
        print("Moderate risk")

evaluation_of_cancer_symptoms(55, "chronic cough")