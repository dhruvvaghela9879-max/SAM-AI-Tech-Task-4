import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("E:\Python\project\Zomatodata.csv")

# Find restaurant chains
chain_count = df["Restaurant_Name"].value_counts()

# Restaurants appearing more than once
chains = chain_count[chain_count > 1]

print("Restaurant Chains:")
print(chains.head(10))

# Average rating of each chain
ratings = df.groupby("Restaurant_Name")["Avg_Rating_Restaurant"].mean()

print("\nTop Rated Restaurant Chains:")
print(ratings.sort_values(ascending=False).head(10))

# Total votes (popularity)
votes = df.groupby("Restaurant_Name")["Votes"].sum()

print("\nMost Popular Restaurant Chains:")
print(votes.sort_values(ascending=False).head(10))

# Plot top 10 chains
chains.head(10).plot(kind="bar", figsize=(10,5))
plt.title("Top 10 Restaurant Chains")
plt.xlabel("Restaurant Name")
plt.ylabel("Number of Menu Items")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Most Popular Chains
votes.sort_values(ascending=False).head(10).plot(kind="bar", figsize=(10,8))
plt.title("Most Popular Restaurant Chains")
plt.xlabel("Restaurant Name")
plt.ylabel("Total Votes")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()