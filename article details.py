import pandas as pd


csv_file_name = "ArticleData.csv"
try:
    existing_data = pd.read_csv(csv_file_name)
except FileNotFoundError:
    existing_data = None


if existing_data is None:
    data = pd.DataFrame(columns=["AID", "Article", "NAME", "INSURED", "PRODUCT TYPE", "GROSS WT", "COUNTRY"])
else:
    data = existing_data


new_row = {}
for column in data.columns:
    value = input(f"Enter {column}: ")
    new_row[column] = value


data = data.append(new_row, ignore_index=True)


data.to_csv(csv_file_name, mode='w', index=False)

print(f"Data has been saved to {csv_file_name}")
