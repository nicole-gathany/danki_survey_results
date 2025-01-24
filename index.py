import pandas as pd

# Load the dataset
file_path = "danki_survey_results_sin_personal_data.csv"
data = pd.read_csv(file_path)

struggle_mapping = {
    'Studying': 1,
    'Networking': 2,
    'Interviewing': 3,
    'Consistency with everything': 4,
    'Imposter syndrome': 5,
    'Using correct terminology even if I know how to do something': 6,
    'Studying, networking and interviewing': 7,
    'Programming outside projects': 8,
    'Building interesting project': 9
}


data["Struggle_encoded"] = data["Struggle"].map(struggle_mapping)

print(data.head())

# Descriptive statistics
numeric_cols = [
    "Struggle_encoded",
    "Motivation",
    "Notification",
    "Visual"
]
print(data[numeric_cols].describe())

# Correlation matrix
correlations = data[numeric_cols].corr()
print(correlations)

