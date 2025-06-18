import pandas as pd

# Load the Excel file
file_path = r"C:\Users\user\Desktop\pythonnn\sagatave_eksamenam.xlsx"
df = pd.read_excel(file_path, sheet_name="Lapa_0")

# Set the correct header
df.columns = df.iloc[1]
df = df[2:]
df = df.rename(columns=lambda x: str(x).strip())

# Convert relevant columns to numeric
df["Klients"] = df["Klients"].astype(str)
df["Skaits"] = pd.to_numeric(df["Skaits"], errors="coerce")
df["Kopā"] = pd.to_numeric(df["Kopā"], errors="coerce")

# Filter and sum
filtered_df = df[
    (df["Klients"] == "Korporatīvais") &
    (df["Skaits"] >= 40) & 
    (df["Skaits"] <= 50)
]
total_sum = filtered_df["Kopā"].sum()
rounded_sum = int(total_sum)

print(f'"{rounded_sum}"') 