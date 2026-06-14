import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch live data from a public API
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1"
response = requests.get(url)
data = response.json()

# Step 2: Transform raw JSON data into a structured DataFrame
df = pd.DataFrame(data)

# Step 3: Clean and filter the data to keep only what we need
filtered_df = df[['name', 'current_price', 'price_change_percentage_24h']]

# Step 4: Display the structured data table in the terminal
print("--- Top 5 Assets Digital Report ---")
print(filtered_df)

# Step 5: Visualize the data using a bar chart
plt.figure(figsize=(8, 5))
plt.bar(filtered_df['name'], filtered_df['current_price'], color='skyblue')
plt.title('Top 5 Crypto Assets by Current Price (USD)')
plt.xlabel('Asset Name')
plt.ylabel('Price ($)')

# Step 6: Save the chart automatically as an image file
plt.savefig('market_report.png')
print("\nSuccess: 'market_report.png' has been generated and saved!")