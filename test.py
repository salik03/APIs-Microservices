import pandas as pd

df_country_data = pd.read_csv("COUNTRY_DATA.csv")

country_name = input("Enter Country Name: ")
product_type = input("Enter Product Type: ")

if country_name in df_country_data.columns:
    if df_country_data.at[0, country_name] == 1 and product_type in df_country_data['PRODUCT TYPE'].values:
        print("True")
    else:
        print("False")
else:
    print("False")
