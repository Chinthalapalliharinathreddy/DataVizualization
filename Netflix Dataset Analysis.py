
# Netflix Dataset Analysis Project


# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\DELL\Downloads\netflix_titles.csv")

# Step 3: Display First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

# Step 4: Display Last 5 Rows
print("\nLast 5 Rows:")
print(df.tail())


# Step 5: Dataset Information
print("\nDataset Information:")
print(df.info())

# Step 6: Shape of Dataset
print("\nDataset Shape:")
print(df.shape)

# Step 7: Column Names
print("\nColumn Names:")
print(df.columns)


# Step 8: Summary Statistics
print("\nSummary Statistics:")
print(df.describe())


# Step 9: Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 10: Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows (optional)
df = df.drop_duplicates()


# Step 11: Movies vs TV Shows
print("\nMovies vs TV Shows:")
print(df["type"].value_counts())

plt.figure(figsize=(6,4))
df["type"].value_counts().plot(kind="bar", color=["skyblue","orange"])
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Step 12: Most Common Ratings
print("\nRatings:")
print(df["rating"].value_counts())

plt.figure(figsize=(10,5))
df["rating"].value_counts().plot(kind="bar", color="green")
plt.title("Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Step 13: Top 10 Countries
print("\nTop 10 Countries:")
print(df["country"].value_counts().head(10))

plt.figure(figsize=(10,5))
df["country"].value_counts().head(10).plot(kind="bar", color="purple")
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()


# Step 14: Top 10 Directors
print("\nTop 10 Directors:")
print(df["director"].value_counts().head(10))

plt.figure(figsize=(10,5))
df["director"].value_counts().head(10).plot(kind="bar", color="red")
plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Titles")
plt.show()


# Step 15: Release Year Distribution
plt.figure(figsize=(10,5))
plt.hist(df["release_year"], bins=20, color="orange", edgecolor="black")
plt.title("Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.show()


# Step 16: Most Common Genres
print("\nTop Genres:")
print(df["listed_in"].value_counts().head(10))

plt.figure(figsize=(12,5))
df["listed_in"].value_counts().head(10).plot(kind="bar", color="teal")
plt.title("Top Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# Step 17: Content Added Per Year
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

print("\nContent Added Per Year:")
print(df["year_added"].value_counts().sort_index())

plt.figure(figsize=(10,5))
df["year_added"].value_counts().sort_index().plot(kind="line", marker="o")
plt.title("Content Added to Netflix Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()


# Step 18: Movie Duration Distribution
movies = df[df["type"] == "Movie"].copy()

movies["duration"] = movies["duration"].str.replace(" min", "", regex=False)
movies["duration"] = pd.to_numeric(movies["duration"], errors="coerce")

plt.figure(figsize=(10,5))
plt.hist(movies["duration"].dropna(),
         bins=20,
         color="cyan",
         edgecolor="black")
plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")
plt.ylabel("Number of Movies")
plt.show()


# Step 19: Correlation (Numeric Columns)
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))


# Step 20: Final Conclusions
print("\n========== PROJECT COMPLETED ==========")
print("Basic Conclusions:")
print("1. Counted Movies and TV Shows.")
print("2. Identified the most common ratings.")
print("3. Found the top countries producing Netflix content.")
print("4. Listed the top directors.")
print("5. Analyzed release year distribution.")
print("6. Examined the most popular genres.")
print("7. Analyzed content added each year.")
print("8. Studied movie duration distribution.")
print("9. Checked missing values and duplicates.")
print("10. Calculated correlation among numeric columns.")