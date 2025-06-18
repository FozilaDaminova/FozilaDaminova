import pandas as pd

# Load the Excel file (skip top 2 rows to get real headers)
file_path = r"C:\Users\user\Desktop\pythonnn\sagatave_eksamenam.xlsx"
df = pd.read_excel(file_path, skiprows=2)

# Clean up column names
df.columns = df.columns.str.strip()

# Filter based on conditions
filtered = df[
    df['Adrese'].str.contains('Adulienas iela', case=False, na=False) &
    df['Pilsēta'].isin(['Valmiera', 'Saulkrasti'])
]

# Show the count
print("Matching entries:", len(filtered))