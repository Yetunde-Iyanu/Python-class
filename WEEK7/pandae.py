#TASK 1 : Load and Explore the Dataset
# Importing pandas as pd to run our code on
import pandas as pd
import matplotlib.pyplot as plt

#choosing the dataset in CSV format using Iris dataset, Note:- To use the iris_csv, I needed download the iris_csv dataset, opened a file
#and paste the dataset inside the created iris_csv file
df = pd.read_csv("iris.csv")

#Display the first few rows of the dataset
print("first 10 rows of the dataset")
print(df.head())

#Explore the structure of the dataset by checking the data types
print("\nSummary statistics")
print(df.describe())
#any missing values
print("\nMissing values:")
print(df.isnull().sum())
#Clean the dataset by either filling or dropping any missing values
df_cleaned = df.dropna()


# TASK 2: Basic Data Analysis
# Compute the basic statistics of the numerical columns
print("Basic Statistics:\n")
print(df.describe())

# Perform groupings on a categorical column
print("\nMean values for each species:\n")
print(df.groupby("species").mean(numeric_only=True))

# Interesting findings i identify from my analysis.
# Setosa flowers have much smaller petals (both length and width) compared to Virginica, which has the largest petals.
# This makes petal size a very strong distinguishing factor.


# TASK 3 :- Creating four different types of visualizations; line, bar chart, histogram, scatter plot.
# Line chart
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], color="blue", label="Sepal Length")
plt.title("Line Chart - Sepal Length Trend")
plt.xlabel("Index (Flower Sample)")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# Bar chart
plt.figure(figsize=(7,5))
df.groupby("species")["petal_length"].mean().plot(kind="bar", color=["purple","orange","blue"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# Histogram
plt.figure(figsize=(7,5))
plt.hist(df["sepal_width"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram - Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
plt.figure(figsize=(7,5))
for species in df["species"].unique():
    subset = df[df["species"] == species]
    plt.scatter(subset["sepal_length"], subset["petal_length"], label=species)
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
