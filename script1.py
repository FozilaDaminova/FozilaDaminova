import pandas as pd

# Correct full path to your file
file_path = r"C:\Users\user\Desktop\pythonnn\sagatave_eksamenam.xlsx"

# Skip first 2 rows to get real headers
df = pd.read_excel(file_path, skiprows=2)

# Optional: print to verify column names
print("Actual columns:", df.columns)

# Fix column names for filtering
df = df.rename(columns={
    'Adrese': 'Address',
    'Skaits': 'Count'
})

# Filter records
filtered_df = df[df['Address'].str.startswith('Ain', na=False) & (df['Count'] < 40)]

# Final result
print("Number of records:", len(filtered_df))