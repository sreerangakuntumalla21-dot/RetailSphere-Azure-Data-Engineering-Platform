from extract import extract_all_data

data = extract_all_data()

print("Available datasets:\n")

for name, df in data.items():
    print(f"{name}: {df.count()}")