import numpy as np

# Patient IDs
patient_ids = np.array([
    "P001", "P002", "P003", "P004", "P005",
    "P006", "P007", "P008", "P009", "P010",
    "P011", "P012", "P013", "P014", "P015"
])

# Patient Names
names = np.array([
    "Ali", "Sara", "Ahmed", "Hina", "Usman",
    "Ayesha", "Hamza", "Maham", "Bilal", "Zoya",
    "Danish", "Sana", "Omar", "Ira", "Saad"
])

patient_ages = np.array([
    25, 30, 22, np.nan, 35,
    40, 27, 32, -5, 31,
    26, 33, 24, 38, 21
])

patient_weights = np.array([
    70, 60, 80, 55, 75,
    np.nan, 68, 72, 78, 62,
    74, 66, -10, 69, 64
])

patient_heights = np.array([
    175, 160, 180, 155, 170,
    165, 172, 168, np.nan, 158,
    177, 163, 173, -150, 159
])


systolic_bp = np.array([
    120, 130, np.nan, 140, 125,
    135, 155, 132, 138, 118,
    122, 148, 134, 136, 124
])

diastolic_bp = np.array([
    80, 85, 75, 90, 82,
    88, 84, np.nan, np.nan, 78,
    81, 83, 87, 89, 79
])


blood_sugar = np.array([
    90, 110, 85, 120, np.nan,
    135, 100, 115, 108, 92,
    98, 102, 145, 118, 88
])
#detecting missing values 
missing_ages = np.isnan(patient_ages)
missing_weights = np.isnan(patient_weights)
missing_heights = np.isnan(patient_heights)
missing_systolic_bp = np.isnan(systolic_bp)
missing_diastolic_bp = np.isnan(diastolic_bp)
missing_blood_sugar = np.isnan(blood_sugar)


#counting missing values
print("\nTotal Missing Count:")
print("Count of Missing Ages:", np.sum(missing_ages))
print("Count of Missing Weights:", np.sum(missing_weights))
print("Count of Missing Heights:", np.sum(missing_heights))
print("Count of Missing Systolic BP:", np.sum(missing_systolic_bp))
print("Count of Missing Diastolic BP:", np.sum(missing_diastolic_bp))
print("Count of Missing Blood Sugar:", np.sum(missing_blood_sugar))
#index of missing values
print("\nMissing Value Locations (Index):")
print("Indices of Missing Ages:", np.where(missing_ages)[0])
print("Indices of Missing Weights:", np.where(missing_weights)[0])
print("Indices of Missing Heights:", np.where(missing_heights)[0])
print("Indices of Missing Systolic BP:", np.where(missing_systolic_bp)[0])
print("Indices of Missing Diastolic BP:", np.where(missing_diastolic_bp)[0])
print("Indices of Missing Blood Sugar:", np.where(missing_blood_sugar)[0])
##detecting negative values
with np.errstate(invalid='ignore'):
    invalid_ages = patient_ages < 0
    invalid_weights = patient_weights < 0
    invalid_heights = patient_heights < 0
    invalid_systolic_bp = systolic_bp < 0
    invalid_diastolic_bp = diastolic_bp < 0
    invalid_blood_sugar = blood_sugar < 0


#print count of invalid values
print("\nTotal Invalid Count:")
print("Count of Invalid Ages:", np.sum(invalid_ages))
print("Count of Invalid Weights:", np.sum(invalid_weights))
print("Count of Invalid Heights:", np.sum(invalid_heights))
print("Count of Invalid Systolic BP:", np.sum(invalid_systolic_bp))
print("Count of Invalid Diastolic BP:", np.sum(invalid_diastolic_bp))
print("Count of Invalid Blood Sugar:", np.sum(invalid_blood_sugar))
#print index of invalid values
print("\nInvalid Value Locations (Index):")
print("Indices of Invalid Ages:", np.where(invalid_ages)[0])
print("Indices of Invalid Weights:", np.where(invalid_weights)[0])
print("Indices of Invalid Heights:", np.where(invalid_heights)[0])
print("Indices of Invalid Systolic BP:", np.where(invalid_systolic_bp)[0])
print("Indices of Invalid Diastolic BP:", np.where(invalid_diastolic_bp)[0])
print("Indices of Invalid Blood Sugar:", np.where(invalid_blood_sugar)[0])
#Calculating median of valid values
age_median = np.nanmedian(patient_ages[patient_ages >= 0])
weight_median = np.nanmedian(patient_weights[patient_weights >= 0])
height_median = np.nanmedian(patient_heights[patient_heights >= 0])
systolic_bp_median = np.nanmedian(systolic_bp[systolic_bp >= 0])
diastolic_bp_median = np.nanmedian(diastolic_bp[diastolic_bp >= 0])
blood_sugar_median = np.nanmedian(blood_sugar[blood_sugar >= 0])

print("\nMedian Values (Excluding Missing and Invalid):")
print("Median Age:", age_median)
print("Median Weight:", weight_median)
print("Median Height:", height_median)

print("Median Systolic BP:", systolic_bp_median)
print("Median Diastolic BP:", diastolic_bp_median)
print("Median Blood Sugar:", blood_sugar_median)
#replacing missing and invalid values with median
patient_ages[missing_ages | invalid_ages] = age_median
patient_weights[missing_weights | invalid_weights] = weight_median
patient_heights[missing_heights | invalid_heights] = height_median
systolic_bp[missing_systolic_bp | invalid_systolic_bp] = systolic_bp_median
diastolic_bp[missing_diastolic_bp | invalid_diastolic_bp] = diastolic_bp_median
blood_sugar[missing_blood_sugar | invalid_blood_sugar] = blood_sugar_median

print("\nUpdated Patient Data (After Handling Missing and Invalid Values):")
print("Patient Ages:", patient_ages)
print("Patient Weights:", patient_weights)
print("Patient Heights:", patient_heights)
print("Systolic BP:", systolic_bp)
print("Diastolic BP:", diastolic_bp)
print("Blood Sugar:", blood_sugar)
# Statistical Analysis
print("\nStatistical Analysis:")
print("--- Age Statistics ---")
print("Mean :", np.mean(patient_ages))
print("Median:", np.median(patient_ages))
print("Min:", np.min(patient_ages))
print("Max:", np.max(patient_ages))
print("Std:", np.std(patient_ages))

print("\n--- Weight Statistics ---")
print("Mean :", np.mean(patient_weights))
print("Median:", np.median(patient_weights))
print("Min:", np.min(patient_weights))
print("Max:", np.max(patient_weights))
print("Std:", np.std(patient_weights))

print("\n--- Height Statistics ---")
print("Mean :", np.mean(patient_heights))
print("Median:", np.median(patient_heights))
print("Min:", np.min(patient_heights))
print("Max:", np.max(patient_heights))
print("Std:", np.std(patient_heights))

print("\n--- Systolic BP Statistics ---")
print("Mean :", np.mean(systolic_bp))
print("Median:", np.median(systolic_bp))
print("Min:", np.min(systolic_bp))
print("Max:", np.max(systolic_bp))
print("Std:", np.std(systolic_bp))

print("\n--- Diastolic BP Statistics ---")
print("Mean :", np.mean(diastolic_bp))
print("Median:", np.median(diastolic_bp))
print("Min:", np.min(diastolic_bp))
print("Max:", np.max(diastolic_bp))
print("Std:", np.std(diastolic_bp))


print("\n--- Blood Sugar Statistics ---")
print("Mean :", np.mean(blood_sugar))   
print("Median:", np.median(blood_sugar))
print("Min:", np.min(blood_sugar))
print("Max:", np.max(blood_sugar))
print("Std:", np.std(blood_sugar))

#filtering patients with high blood pressure
high_bp_patients =(systolic_bp > 140) | (diastolic_bp > 90)
print("\nPatients with High Blood Pressure:")
print("Patient IDs:", patient_ids[high_bp_patients])
print("Patient Names:", names[high_bp_patients])
print("Systolic BP:", systolic_bp[high_bp_patients])
print("Diastolic BP:", diastolic_bp[high_bp_patients])
 # filtering patients with high blood sugar
high_blood_sugar_patients = blood_sugar > 125
print("\nPatients with High Blood Sugar:")
print("Patient IDs:", patient_ids[high_blood_sugar_patients])
print("Patient Names:", names[high_blood_sugar_patients])
print("Blood Sugar Levels:", blood_sugar[high_blood_sugar_patients])

# Extreme Values Detection

highest_age_index = np.argmax(patient_ages)
lowest_age_index = np.argmin(patient_ages)

highest_weight_index = np.argmax(patient_weights)
lowest_weight_index = np.argmin(patient_weights)

highest_height_index = np.argmax(patient_heights)
lowest_height_index = np.argmin(patient_heights)

highest_systolic_bp_index = np.argmax(systolic_bp)
lowest_systolic_bp_index = np.argmin(systolic_bp)

highest_diastolic_bp_index = np.argmax(diastolic_bp)
lowest_diastolic_bp_index = np.argmin(diastolic_bp)

highest_blood_sugar_index = np.argmax(blood_sugar)
lowest_blood_sugar_index = np.argmin(blood_sugar)


print("\nExtreme Values Detection:")

print(
    f"\nOldest patient: {names[highest_age_index]} "
    f"({patient_ids[highest_age_index]}) - "
    f"{patient_ages[highest_age_index]} years"
)


print(
    f"Youngest patient: {names[lowest_age_index]} "
    f"({patient_ids[lowest_age_index]}) - "
    f"{patient_ages[lowest_age_index]} years"
)

print(
    f"\nHeaviest patient: {names[highest_weight_index]} "
    f"({patient_ids[highest_weight_index]}) - "
    f"{patient_weights[highest_weight_index]} kg"
)

print(
    f"Lightest patient: {names[lowest_weight_index]} "
    f"({patient_ids[lowest_weight_index]}) - "
    f"{patient_weights[lowest_weight_index]} kg"
)

print(
    f"\nTallest patient: {names[highest_height_index]} "
    f"({patient_ids[highest_height_index]}) - "
    f"{patient_heights[highest_height_index]} cm"
)

print(
    f"Shortest patient: {names[lowest_height_index]} "
    f"({patient_ids[lowest_height_index]}) - "
    f"{patient_heights[lowest_height_index]} cm"
)

print(
    f"\nHighest systolic BP: {names[highest_systolic_bp_index]} "
    f"({patient_ids[highest_systolic_bp_index]}) - "
    f"{systolic_bp[highest_systolic_bp_index]} mmHg"
)

print(
    f"Lowest systolic BP: {names[lowest_systolic_bp_index]} "
    f"({patient_ids[lowest_systolic_bp_index]}) - "
    f"{systolic_bp[lowest_systolic_bp_index]} mmHg"
)

print(
    f"\nHighest diastolic BP: {names[highest_diastolic_bp_index]} "
    f"({patient_ids[highest_diastolic_bp_index]}) - "
    f"{diastolic_bp[highest_diastolic_bp_index]} mmHg"
)

print(
    f"Lowest diastolic BP: {names[lowest_diastolic_bp_index]} "
    f"({patient_ids[lowest_diastolic_bp_index]}) - "
    f"{diastolic_bp[lowest_diastolic_bp_index]} mmHg"
)

print(
    f"\nHighest blood sugar: {names[highest_blood_sugar_index]} "
    f"({patient_ids[highest_blood_sugar_index]}) - "
    f"{blood_sugar[highest_blood_sugar_index]} mg/dL"
)

print(
    f"Lowest blood sugar: {names[lowest_blood_sugar_index]} "
    f"({patient_ids[lowest_blood_sugar_index]}) - "
    f"{blood_sugar[lowest_blood_sugar_index]} mg/dL"
)
#categorizing patients 
bp_category = np.where((systolic_bp > 140) | (diastolic_bp > 90), "High", "Normal")
sugar_category = np.where(blood_sugar > 125, "High", "Normal")
print("\nPatient Categories:")

print("Blood Pressure Category:")
print(bp_category)

print("\nBlood Sugar Category:")
print(sugar_category)

# Blood Sugar Ranking

ranking_order = np.argsort(blood_sugar)[::-1]

ranked_ids = patient_ids[ranking_order]
ranked_names = names[ranking_order]
ranked_sugar = blood_sugar[ranking_order]

print("\nBlood Sugar Ranking:")

for i in range(len(ranking_order)):
    print(
        f"{i + 1}. {ranked_names[i]} "
        f"({ranked_ids[i]}) - "
        f"{ranked_sugar[i]} mg/dL"
    )

# Blood Pressure Ranking

bp_ranking_order = np.argsort(systolic_bp)[::-1]

ranked_bp_ids = patient_ids[bp_ranking_order]
ranked_bp_names = names[bp_ranking_order]
ranked_systolic_bp = systolic_bp[bp_ranking_order]

print("\nSystolic Blood Pressure Ranking:")

for i in range(len(bp_ranking_order)):
    print(
        f"{i + 1}. {ranked_bp_names[i]} "
        f"({ranked_bp_ids[i]}) - "
        f"{ranked_systolic_bp[i]} mmHg"
    )
   
print("\nFINAL PATIENT DATA REPORT")

print(f"Total Patients Analyzed: {len(names)}")
print(f"High BP Patients: {np.sum(high_bp_patients)}")
print(f"High Blood Sugar Patients: {np.sum(high_blood_sugar_patients)}")
print(f"Average Age: {np.mean(patient_ages):.1f} years")
print(f"Average BP: {np.mean(systolic_bp):.1f}/{np.mean(diastolic_bp):.1f} mmHg")
print(f"Average Blood Sugar: {np.mean(blood_sugar):.1f} mg/dL")
