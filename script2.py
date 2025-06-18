import pandas as pd

# Load the file (update path if needed)
file_path = r"C:\Users\user\Desktop\pythonnn\sagatave_eksamenam.xlsx"
df = pd.read_excel(file_path, skiprows=2)

# Rename columns
df = df.rename(columns={
    'Prioritāte': 'Priority',
    'Piegādes datums': 'Delivery Date'
})

# Convert delivery date to datetime
df['Delivery Date'] = pd.to_datetime(df['Delivery Date'], errors='coerce')

# Filter: High priority & year 2015
filtered = df[
    (df['Priority'] == 'High') &
    (df['Delivery Date'].dt.year == 2015)
]

# Print the count
print("Number of entries with High priority and delivery year 2015:", len(filtered))