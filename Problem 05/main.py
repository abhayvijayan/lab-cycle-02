
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "month_number": list(range(1, 13)),
    "facecream": [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    "facewash": [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "toothpaste": [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    "bathingsoap": [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    "shampoo": [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    "moisturizer": [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "total_units": [21100, 18330, 22470, 22270, 20960, 20150, 21500, 24380, 23400, 26670, 28700, 32180],
    "total_profit": [211000, 183300, 224700, 222700, 209600, 201500, 215000, 243800, 234000, 266700, 287000, 321800]
}

df = pd.DataFrame(data)
df.to_csv("company.csv", index=False)

df = pd.read_csv("company.csv")

# Scatter Plot
plt.scatter(df["month_number"], df["toothpaste"])
plt.xlabel("Month Number")
plt.ylabel("Toothpaste Sales")
plt.title("Toothpaste Sales per Month")
plt.show()

# Bar Chart
plt.bar(df["month_number"] - 0.2, df["facecream"],
        width=0.4, label="Face Cream")
plt.bar(df["month_number"] + 0.2, df["facewash"],
        width=0.4, label="Face Wash")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.title("Face Cream and Face Wash Sales")
plt.legend()
plt.show()

# Pie CHart
products = [
    "facecream", "facewash", "toothpaste",
    "bathingsoap", "shampoo", "moisturizer"
]

sales = df[products].sum()

plt.pie(sales, labels=products, autopct="%1.1f%%")
plt.title("Total Yearly Sales by Product")
plt.show()
