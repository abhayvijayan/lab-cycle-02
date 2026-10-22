
import pandas as pd

# Read
df = pd.read_csv("students.csv")

# 1. Remove duplicate rows and handle missing values
df.drop_duplicates(inplace=True)
df.dropna(subset=["name", "subject", "marks", "grade"], inplace=True)

print("Cleaned Student Data:")
print(df)

# 2. Find the student with maximum marks in each subject
print("\nStudent with Maximum Marks in Each Subject:")
max_marks = df.loc[df.groupby("subject")["marks"].idxmax()]
print(max_marks[["subject", "name", "marks"]])

# 3. Calculate average marks for each grade
print("\nAverage Marks for Each Grade:")
average_marks = df.groupby("grade")["marks"].mean()
print(average_marks.round(2))

# Save the cleaned data
df.to_csv("students_cleaned.csv", index=False)
print("\nCleaned data saved successfully.")
