import pandas as pd

# Load only needed columns
# Read the voice usage part of the file
df = pd.read_csv("ReportAU_3945468001.txt", skiprows=11, low_memory=False)

# Show just the two rows columns we care about
print(df[["OriginatingNumber", "TerminatingNumber"]].head(20))

# Function to normalize numbers (i.e remove leading 1 if exist)
def normalize(num):
    num = str(num)
    if num.startswith("1") and len(num) == 11:
        return num[1:]
    return num

df["OriginatingNumber"] = df["OriginatingNumber"].apply(normalize)
df["TerminatingNumber"] = df["TerminatingNumber"].apply(normalize)

# Filter by client's number
print("Filter by client's number")
num_a = "2168678299"
num_b = "2164085717"

filtered = df[
    (df["OriginatingNumber"] == num_a) & (df["TerminatingNumber"] == num_b) |
    (df["OriginatingNumber"] == num_b) & (df["TerminatingNumber"] == num_a)
]


# Save result as a spreadsheet
# save as CSV
filtered.to_csv("Filtered_calls.csv", index=False)

filtered.to_excel("Filtered_calls.xlsx", index=False)

# Report summary
print(filtered.head(20))
print(f"Total calls found: {len(filtered)}")
