
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("sales_data.csv")

# a) Monthly profit using a line chart
plt.plot(df["month"], df["profit"], marker="o")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit")
plt.grid(True)
plt.show()

# b) Electronics and Clothing sales using a grouped bar chart
x = range(len(df["month"]))
width = 0.4

plt.bar([i - width/2 for i in x], df["electronics"],
        width=width, label="Electronics")
plt.bar([i + width/2 for i in x], df["clothing"],
        width=width, label="Clothing")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Electronics and Clothing Monthly Sales")
plt.xticks(list(x), df["month"])
plt.legend()
plt.show()

# c) Total yearly sales for each category using a pie chart
categories = ["electronics", "clothing", "groceries", "furniture"]
total_sales = df[categories].sum()

plt.pie(total_sales, labels=categories, autopct="%1.1f%%")
plt.title("Total Yearly Sales by Category")
plt.show()
