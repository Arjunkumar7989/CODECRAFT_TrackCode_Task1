import pandas as pd

file_path = r"C:\Users\arjun\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_2590 (1)\API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv"

# Usually, this dataset has metadata in the first few rows, so we skip them
df = pd.read_csv(file_path, skiprows=4)

print(df.head())
df.head()
df.columns
india_data = df[df['Country Name'] == 'India']
print(india_data)

import matplotlib.pyplot as plt

india_years = india_data.loc[:, '1960':'2022'].T
india_years.index = india_years.index.astype(int)

plt.figure(figsize=(10, 5))
plt.plot(india_years, label='India')
plt.title('Population Growth - India')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv(r"C:\Users\arjun\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_2590 (1)\API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv", skiprows=4)

# Filter only latest year (e.g., 2022)
df_2022 = df[["Country Name", "2022"]].dropna()

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(df_2022["2022"] / 1_000_000, bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Country Populations (2022)")
plt.xlabel("Population (in millions)")
plt.ylabel("Number of Countries")
plt.grid(True)
plt.show()
