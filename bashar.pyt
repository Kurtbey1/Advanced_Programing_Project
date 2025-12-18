import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("SuperMarket Analysis.csv")
print("First rows:\n", dataset.head())
print("\nInfo:\n")
print(dataset.info())
print("\nDescribe:\n", dataset.describe())


#############################################################################
print(dataset.isnull().sum())
dataset.replace(["", " ", "NA", "N/A", "nan"], pd.NA, inplace=True)
print(dataset.isnull().sum())
print(dataset.duplicated().sum())

print(dataset.dtypes)


print(dataset['Customer type'].unique())
print(dataset['Branch'].unique())
print(dataset['City'].unique())
print(dataset['Product line'].unique())
print(dataset['Payment'].unique())

branches = dataset['Branch'].to_numpy()
sales = dataset['Sales'].to_numpy()
unique_branches = np.unique(branches)
print(unique_branches)
branch_sales = {}
for branch in unique_branches:
    total = np.sum(sales[branches == branch])
    branch_sales[branch] = total
highestBranch = max(branch_sales, key=branch_sales.get)
highestRevenue = branch_sales[highestBranch]




branchStatsNp = {}

for branch in branches:
    branchSales = sales[dataset['Branch'].to_numpy() == branch]
    branchStatsNp[branch] = {
        'total_sales': np.sum(branchSales),
        'average_sales': np.mean(branchSales),
        'max_sales': np.max(branchSales),
        'min_sales': np.min(branchSales),
        'transaction_count': len(branchSales)
    }


print("Branch with highest revenue:", highestBranch)
print("Revenue:", highestBranch)
print(branchStatsNp)
print(highestRevenue)
################################################################################################################
Branch_stats = dataset.groupby(['Branch', 'Customer type', 'Gender', 'Payment']).agg(
    mean_sales=('Sales', 'mean'),
    median_sales=('Sales', 'median'),
    max_sales=('Sales', 'max'),
    min_sales=('Sales', 'min')
)


print(Branch_stats)


##################################################################################################
Genders = dataset['Gender'].to_numpy()
uniqueGenders = np.unique(Genders)


for gender in uniqueGenders:
    count = np.sum(Genders == gender)
    print(f"Number of {gender}s: {count}")
####################################################################

totalSales = dataset.groupby('Customer type')['Sales'].sum()
print(totalSales)


mostPayment = dataset.groupby('Payment')['Quantity'].sum()
print(mostPayment)

##########################################################


avgRating = dataset.groupby('Product line')['Rating'].mean()
print(avgRating)

highestProductLine = avgRating.idxmax()
highestRating = avgRating.max()

print("\nProduct line with highest average rating:", highestProductLine)
print("Average rating:", highestRating)
####################################################################################

product_lines = dataset['Product line'].to_numpy()
ratings = dataset['Rating'].to_numpy()

unique_products = np.unique(product_lines)

highest_rating = 0
highest_product = ""

for product in unique_products:
    product_ratings = ratings[product_lines == product]  
    avg = np.mean(product_ratings)                      
    print(f"{product} - Average rating: {avg:.2f}")

    if avg > highest_rating:
        highest_rating = avg
        highest_product = product

print("\nProduct line with highest average rating:", highest_product)
print("Average rating:", highest_rating)





################################################################

productStats = dataset.groupby('Product line').agg(
    total_sales=('Sales', 'sum'),
    average_sales=('Sales', 'mean'),
    max_sales=('Sales', 'max'),
    min_sales=('Sales', 'min'),
    transaction_count=('Sales', 'count'),
    average_rating=('Rating', 'mean'),
    max_rating=('Rating', 'max'),
    min_rating=('Rating', 'min')
)

print(productStats)
###################################################################

unitPrice = dataset['Unit price'].to_numpy()
quantity = dataset['Quantity'].to_numpy()

correlation = np.corrcoef(unitPrice, quantity)[0, 1]
print("Correlation (NumPy):", correlation)


###########################################################################################
branchSales = dataset.groupby('Branch')['Sales'].sum()
plt.plot(branchSales.index, branchSales.values, color='red', marker='*')
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.title("Total Sales per Branch")
plt.show()



dataset['Date'] = pd.to_datetime(dataset['Date'])

customer_counts = dataset['Customer type'].value_counts()
sales_over_time = dataset.groupby('Date')['Sales'].sum()
ratings_over_time = dataset.groupby('Date')['Rating'].mean()
numeric_cols = dataset.select_dtypes(include=np.number)
corr_matrix = numeric_cols.corr()
product_gross = dataset[['Product line', 'gross income']]

plt.figure(figsize=(20,18))

plt.subplot(3,3,1)
plt.bar(customer_counts.index, customer_counts.values, color='skyblue')
plt.title("Frequency of Customer Types")
plt.ylabel("Count")
plt.xlabel("Customer Type")

plt.subplot(3,3,2)
plt.plot(sales_over_time.index, sales_over_time.values, marker='o', color='blue')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)

plt.subplot(3,3,3)
plt.plot(ratings_over_time.index, ratings_over_time.values, marker='o', color='green')
plt.title("Average Rating Over Time")
plt.xlabel("Date")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.grid(True)

plt.subplot(3,3,4)
plt.scatter(dataset['Sales'], dataset['Rating'], color='purple')
plt.title("Sales vs Rating")
plt.xlabel("Sales")
plt.ylabel("Rating")
plt.grid(True)

plt.subplot(3,3,5)
im = plt.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.colorbar(im, fraction=0.046, pad=0.04)
plt.xticks(ticks=range(len(corr_matrix.columns)), labels=corr_matrix.columns, rotation=45)
plt.yticks(ticks=range(len(corr_matrix.columns)), labels=corr_matrix.columns)

plt.subplot(3,3,6)
product_lines = product_gross['Product line'].unique()
data_to_plot = [product_gross[product_gross['Product line']==pl]['gross income'] for pl in product_lines]
plt.boxplot(data_to_plot, labels=product_lines)
plt.title("gross Income Distribution by Product Line")
plt.xlabel("Product Line")
plt.ylabel("gross Income")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

