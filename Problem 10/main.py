
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Load the Iris dataset into Pandas
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=[
        "sepal_length", "sepal_width",
        "petal_length", "petal_width"
    ]
)

df["species"] = [iris.target_names[i] for i in iris.target]

# Clean the dataset
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print("Dataset loaded and cleaned successfully.")
print(df.head())

# 2. Split into training and testing sets (80:20)
X = df[["sepal_length", "sepal_width",
        "petal_length", "petal_width"]]
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 3. Display the number of samples for each species
print("\nNumber of samples for each species:")
print(df["species"].value_counts())

# 4. Plot histograms of sepal length and petal length
plt.hist(df["sepal_length"], bins=10, edgecolor="black")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")
plt.show()

plt.hist(df["petal_length"], bins=10, edgecolor="black")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.title("Distribution of Petal Length")
plt.show()

# 5. Bar chart of species distribution
species_count = df["species"].value_counts()

species_count.plot(kind="bar", edgecolor="black")
plt.xlabel("Species")
plt.ylabel("Number of Samples")
plt.title("Distribution of Iris Species")
plt.xticks(rotation=0)
plt.show()
