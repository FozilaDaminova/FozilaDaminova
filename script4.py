import pandas as pd
import math

# Load file and skip first 2 header rows to get actual column names
file_path = r"C:\Users\user\Desktop\pythonnn\sagatave_eksamenam.xlsx"
df = pd.read_excel(file_path, skiprows=2)

# Strip spaces from column names just in case
df.columns = df.columns.str.strip()

# Filter products containing "Laserjet" (case-insensitive)
laserjet_df = df[df['Produkts'].str.contains('Laserjet', case=False, na=False)]

# Calculate average price
average_price = laserjet_df['Cena'].mean()

# Round down to nearest integer
rounded_down = math.floor(average_price)

print("Average price (rounded down):", rounded_down)