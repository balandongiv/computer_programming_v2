"""Session 2: practice variables, basic arithmetic, comparisons, type conversions, and adding a second flower.
Note: Variable names must match exactly because later sessions import these names.
"""

# Task 1: Print student summary (optional but good practice)
print("=== Student Label ===")
student_id = "YOUR_ID_HERE"
full_name = "YOUR_FULL_NAME_HERE"
print("Student ID:", student_id)
print("Full Name:", full_name)

# Task 2: Declare variables for one Iris flower
# We define these variables to represent a single setosa flower.
id = "flower1"
sepal_length = 5.1
sepal_width = 3.5
petal_length = 1.4
petal_width = 0.2
species = "setosa"

print("\n=== Flower Summary ===")
print("ID:", id)
print("Sepal Length:", sepal_length)
print("Sepal Width:", sepal_width)
print("Petal Length:", petal_length)
print("Petal Width:", petal_width)
print("Species:", species)

# Task 3: Compute petal area
# Multiply petal_length and petal_width to get the area
petal_area = petal_length * petal_width
# Observe the exact floating-point output
print("\nPetal Area:", petal_area)

# Task 4: Define rule variables and comparison
# We use these variables in the next session for our rule-based classifier
threshold = 2.0
feature_name = "petal_length"
positive_label = "setosa"
negative_label = "not_setosa"
label_key = "species"

is_short_petal = petal_length < threshold
print("\n=== Comparison ===")
print("is_short_petal (petal_length < threshold):", is_short_petal)

# Task 5: Type conversion practice
petal_length_text = str(petal_length)
threshold_text = "2.0"
threshold_number = float(threshold_text)

print("\n=== Conversions ===")
print("petal_length_text:", petal_length_text, "| type:", type(petal_length_text))
print("threshold_text:", threshold_text, "| type:", type(threshold_text))
print("threshold_number:", threshold_number, "| type:", type(threshold_number))

# Task 6: Add a second flower using _2 suffix
# It is important to keep the _2 suffix so Session 3 can convert them into a dictionary
sepal_length_2 = 4.9
sepal_width_2 = 3.0
petal_length_2 = 1.4
petal_width_2 = 0.2
species_2 = "setosa"

petal_area_2 = petal_length_2 * petal_width_2
print("\n=== Flower 2 ===")
print("Petal Area 2:", petal_area_2)
