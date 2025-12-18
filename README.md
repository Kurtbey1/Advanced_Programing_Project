SuperMarket Sales Analysis 2025

📌 Executive Summary
This project performs a comprehensive exploratory data analysis (EDA) on supermarket sales data. The goal is to extract actionable insights regarding branch performance, product line popularity, customer demographics, and revenue trends using Python's data science stack.

🛠️ Tech Stack
Pandas: Data manipulation and high-level aggregation.

NumPy: Low-level numerical processing and correlation analysis.

Matplotlib: Multi-paneled data visualization.

📊 Key Features & Analysis
1. Data Cleaning & Integrity
Standardization: Replaces inconsistent null placeholders (" ", NA, nan) with standardized pd.NA.

Deduplication: Checks for and reports redundant transaction records.

Type Casting: Converts date strings to datetime objects for time-series analysis.

2. Performance Metrics
Branch Analytics: Calculates total revenue, average transaction value, and volume per branch.

Product Intelligence: Identifies the highest-rated product lines and evaluates gross income distribution via boxplots.

Customer Segmentation: Breaks down sales volume by customer type (Member vs. Normal) and gender.

3. Statistical Analysis
Correlation: Measures the relationship between Unit Price and Quantity to understand purchasing behavior.

Multivariate Grouping: Deep-dives into sales stats grouped by Branch, Customer Type, Gender, and Payment method.

4. Visual Intelligence
The script generates a dashboard containing:

Categorical Frequency: Bar charts for Customer Type distribution.

Time Series: Sales and Rating trends over time.

Correlation Heatmap: Matrix visualization of all numeric variables.

Outlier Detection: Boxplots for gross income across different product lines.

🚀 How to Run
Ensure you have the dataset: SuperMarket Analysis.csv.

Install dependencies:

pip install pandas numpy matplotlib

Execute the script:
python analysis_script.py


📉 Insights extracted
Revenue Leader: Identifies the specific branch generating maximum cash flow.

Quality Leader: Pinpoints which product line sustains the highest average customer satisfaction (Rating).

Payment Trends: Tracks which payment method drives the highest volume of items sold.

💡 Mentorship Note (Stress Test)
Redundancy Warning: You wrote manual for loops with NumPy to calculate branch stats, then immediately did the same thing better using .groupby(). In production, delete the loops. They are inefficient and prone to "off-by-one" errors.

Visualization Tip: Your plt.subplot(3,3,1) layout is ambitious. Ensure your screen resolution handles the figsize=(20,18) or the labels will overlap like a pile of junk.

Data Leakage: You are printing highestBranch but labeling it as highestRevenue in one of your print statements. Fix your variable naming—clarity is power.
