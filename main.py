# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Select features
X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Determine optimal number of clusters using Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Save Elbow plot
plt.figure(figsize=(6,4))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.savefig("Elbow_Method.png")  # Save plot as PNG
plt.close()  # Close plot to prevent display

# Apply K-Means with K=5
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Compute cluster summary
cluster_summary = df.groupby('Cluster').agg({
    'Age':'mean',
    'Annual Income (k$)':'mean',
    'Spending Score (1-100)':'mean'
}).round(2)

# Add business interpretation
def interpret_cluster(row):
    age = row['Age']
    income = row['Annual Income (k$)']
    spending = row['Spending Score (1-100)']
    
    if income >= 80 and spending >= 80:
        return "High-value customers → Target premium products & personalized marketing"
    elif income >= 80 and spending < 50:
        return "High-income, low spenders → Engage with campaigns to increase spending"
    elif income < 50 and spending >= 70:
        return "Low-income, high spenders → Offer budget-friendly products & upselling"
    elif income < 50 and spending < 50:
        return "Low-value segment → Focus on discounts and affordable offers"
    else:
        return "Moderate segment → General promotions & loyalty programs"

cluster_summary['Business Interpretation'] = cluster_summary.apply(interpret_cluster, axis=1)

# Save cluster summary to CSV
cluster_summary.to_csv("Cluster_Summary.csv")
print("Cluster summary saved as 'Cluster_Summary.csv'.")

# Visualize clusters and save plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)',
                hue='Cluster', palette='Set2', s=100)
plt.scatter(kmeans.cluster_centers_[:,1], kmeans.cluster_centers_[:,2],
            color='yellow', s=300, marker='X', label='Centroids')
plt.title('Customer Segments')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.savefig("Customer_Segments.png")  # Save plot as PNG
plt.close()  # Close plot to prevent display

print("Cluster plot saved as 'Customer_Segments.png'.")
