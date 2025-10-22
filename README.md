🛍️ Customer Segmentation Analysis

Segment mall customers using K-Means clustering to drive targeted marketing and business strategies.

📊 Dataset

Mall_Customers.csv includes:

CustomerID – Unique ID

Gender – Male/Female

Age – Customer age

Annual Income (k$) – Income in thousands

Spending Score (1-100) – Behavior score

🎯 Objective

Group customers based on Age, Annual Income, and Spending Score to:

Identify high-value customers

Design targeted promotions

Boost customer engagement

⚙️ Methodology

Feature Selection – Age, Annual Income, Spending Score

Elbow Method – Find optimal number of clusters

K-Means Clustering – Applied with 5 clusters

Cluster Analysis – Compute mean metrics and interpret business value

Visualization – Plot clusters and centroids

🗂️ Outputs
File	Description

Elbow_Method.png-Determines optimal cluster number

Cluster_Summary.csv	-Cluster metrics & business insights

Customer_Segments.png	-Visual cluster representation

💡 Business Insights

High-income, high spenders → Premium products & personalized marketing

High-income, low spenders → Campaigns to boost spending

Low-income, high spenders → Budget-friendly products & upselling

Low-income, low spenders → Discounts & offers

Moderate segment → General promotions & loyalty programs

🚀 How to Run

pip install pandas matplotlib seaborn scikit-learn

python customer_segmentation.py


Outputs will be saved in the project folder.

📂 Dataset Credits

The dataset used in this project is from Kaggle:
Mall Customers Dataset(https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

Used for educational and portfolio purposes only.
