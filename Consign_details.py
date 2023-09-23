import pandas as pd
import math


try:
    existing_data = pd.read_csv('consignment_data.csv')
except FileNotFoundError:
    
    existing_data = pd.DataFrame(columns=[
        'Product type', 'Category of item', 'No. of Types of items in Consignment',
        'Gross weight', 'Total value (INR)', 'Instructions in case of Non-Delivery',
        'No. of Licenses', 'No. of Invoices', 'No. of Certificates', 'SELECT PBE', 'Self filling', 'Senders Custom Ref No', 'Receivers Import Ref No'
    ])


new_data = pd.DataFrame(columns=existing_data.columns)
new_data['Product type'] = [input("Enter Product type: ")]
new_data['Category of item'] = [input("Enter Category of item: ")]
new_data['No. of Types of items in Consignment'] = [int(input("Enter No. of Types of items in Consignment: "))]
new_data['Gross weight'] = [float(input("Enter Gross weight: "))]
new_data['Total value (INR)'] = [float(input("Enter Total value (INR): "))]
new_data['Instructions in case of Non-Delivery'] = [input("Enter Instructions in case of Non-Delivery: ")]
new_data['No. of Licenses'] = [int(input("Enter No. of Licenses: "))]
new_data['No. of Invoices'] = [int(input("Enter No. of Invoices: "))]
new_data['No. of Certificates'] = [int(input("Enter No. of Certificates: "))]
new_data['SELECT PBE'] = [str(input("Enter SELECT PBE: "))]
new_data['Self filling'] = [input("Enter Self filling: ")]
new_data['Senders Custom Ref No'] = [int(input("Enter Senders Custom Ref No: "))]
new_data['Receivers Import Ref No'] = [int(input("Enter Senders Custom Ref No: "))]

#SDR CALCULATOR
new_data['SDR'] = new_data['Total value (INR)'].apply(lambda x: math.ceil(0.01 * x))

#TARIFF CALCULATOR


combined_data = pd.concat([existing_data, new_data], ignore_index=True)


combined_data.to_csv('consignment_data.csv', index=False)

print("Data has been saved to consignment_data.csv")
print(f"Calculated SDR value: {new_data['SDR'].values[0]}")



