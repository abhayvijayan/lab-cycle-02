
import csv

# Data
data = [
    ["SN", "Name", "Country", "Innovation", "Year"],
    [1, "Geoffrey Hinton", "Canada", "Deep Learning", 1986],
    [2, "Yann LeCun", "France", "Convolutional Neural Nets", 1989],
    [3, "Andrew Ng", "USA", "Online ML Courses", 2011],
    [4, "Phila Suoni", "UK", "Artificial Intelligence", 2023],
    [5, "Yemehi Yathi", "France", "Data Analytics", 2025]
]

with open("tech_innovators.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")

# Read the CSV file and print innovators before 2000
with open("tech_innovators.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    print("\nInnovators who contributed before 2000:")

    for row in reader:
        if int(row["Year"]) < 2000:
            print(row["Name"])
