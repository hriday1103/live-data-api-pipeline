import requests
import pandas as pd
import matplotlib.pyplot as plt


url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1"
response = requests.get(url)
data = response.json()


df = pd.DataFrame(data)


filtered_df = df[['name', 'current_price', 'price_change_percentage_24h']]


print("--- Top 5 Assets Digital Report ---")
print(filtered_df)


plt.figure(figsize=(8, 5))
plt.bar(filtered_df['name'], filtered_df['current_price'], color='skyblue')
plt.title('Top 5 Crypto Assets by Current Price (USD)')
plt.xlabel('Asset Name')
plt.ylabel('Price ($)')


plt.savefig('market_report.png')
print("\nSuccess: 'market_report.png' has been generated and saved!")