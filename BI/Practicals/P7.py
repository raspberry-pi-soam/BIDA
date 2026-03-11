import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Load the Data ---
try: 
    df = pd.read_csv('sales_data.csv')
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    print("--- Dataset Preview ---")
    print(df.head(), "\n")
except FileNotFoundError:
    print("Error: The file was not found")

# --- Step 2: Basic Data Exploration ---
print("--- Data Info ---")
print(df.info()) # Shows col types & missing values
print("\n--- Statistical Summary ---")
print(df.describe())

# --- Step 3: Data Analysis & Insights ---
# Insight 1: Total revenue
total_revenue = df['TotalPrice'].sum()

# Insight 2: Sales by category (Region)
category_sales = df.groupby('Region')['TotalPrice'].sum()

# Insight 3: Most popular product (by Quantity)
popular_product = df.groupby('Product')['Quantity'].sum().idxmax()

# --- Step 4: Display Results ---
print("\nFinal Insights")
print(f"Total Revenue Generated: {total_revenue}")
print(f"Revenue by Region:\n{category_sales}") 
print(f"Best Selling Product: {popular_product}")

# --- Step 5: Line Graph - Yearly Sales Trend ---
df['Year'] = df['Date'].dt.year
# Group by 'Year' and calculate the sum of 'TotalPrice'
yearly_sales = df.groupby('Year')['TotalPrice'].sum().reset_index()

# Sort the data by year to ensure line graph is plotted correctly
yearly_sales = yearly_sales.sort_values(['Year']) 

# Create the line graph
plt.plot(yearly_sales['Year'], yearly_sales['TotalPrice'], marker='o', linestyle='-', color='b')

# Adding titles and labels
plt.title('Yearly sales performance')
plt.xlabel('Year') 
plt.ylabel('Total sales ($)') 
plt.xticks(yearly_sales['Year'].unique())

# Ensure x-axis only shows existing years
plt.grid(True, linestyle='--', alpha=0.7)

# Save the plot
plt.savefig('Yearly_sales_performance.png')
plt.clf() # Clears the invisible canvas so the next chart doesn't overlap!

# --- Step 6: Bar chart - Total sales by category ---
category_data = df.groupby('Region')['TotalPrice'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
category_data.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Total Revenue by product category", fontsize=14)
plt.xlabel('Region', fontsize=12) 
plt.ylabel('Total Sales ($)', fontsize=12) 
plt.xticks(rotation=0) # Keeps labels horizontal
plt.tight_layout()

plt.savefig('Sales_bar_chart.png')
plt.show()