import pandas as pd

# Define the mandatory column names
mandatory_columns = [
    'Country', 'Product_Type', 'prd_gross_wt', 'articletype', 'id',
    'producttype', 'servicecat', 'articleweight', 'nondeliveryinst',
    'nameofreceipient', 'receipientaddressline1', 'receipientcity', 'receipientpincode',
    'receipientcountry', 'selffilling', 'totalval', 'hscode', 'prd_desc',
    'prd_qty_unit', 'count', 'prd_wgt_net', 'origincountry'
]

# Define the optional column names
optional_columns = [
    'senderref', 'receipientref', 'receipientcompname', 'receipientaddressline2',
    'receipientemail', 'receipientmobile', 'insurancevaluesdr', 'invoiceno',
    'prd_inv_date', 'ecomm', 'tax_inv_date', 'tax_inv_sno', 'tax_inv_val',
    'asbl_fob', 'asbl_curr', 'expo_duty_rate', 'expo_duty_amt', 'cess_rate',
    'cess_amt', 'lut_bond_det', 'comp_cess_rate', 'comp_ces_amt', 't_duty', 't_cess'
]

# Try to load existing data from the CSV file if it exists
try:
    existing_data = pd.read_csv('bulk.csv')
except FileNotFoundError:
    existing_data = pd.DataFrame(columns=mandatory_columns + optional_columns)

# Create a new DataFrame for user input
new_data = pd.DataFrame(columns=mandatory_columns + optional_columns)

# Get user input for each column value (mandatory columns)
for column in mandatory_columns:
    new_data[column] = [input(f"Enter {column}: ")]

# Get user input for optional columns (user can leave them empty)                
for column in optional_columns:
    user_input = input(f"Enter {column} (press Enter to skip): ")
    if user_input.strip() != '':
        new_data[column] = [user_input]

# Concatenate the new data with the existing data
combined_data = pd.concat([existing_data, new_data], ignore_index=True)

# Save the combined data to a CSV file
combined_data.to_csv('bulk.csv', index=False)

print("Data has been saved to bulk.csv")


def checkAvail(country, service, wt):
    comp = pd.read_csv('CountryData.csv')
    serviceData = pd.read_csv('ServiceDetails.csv')
    index = list(comp['Country'].values).index(country)
    
    availability= comp.iloc[index,service]
    weight = serviceData.iloc[0,service-1]
    
    if(availability == 0):
        return(-1)
    
    if(wt>weight):
        return(weight)
    
    else:
        return(1)
    
data = pd.read_csv('bulk.csv')



for i in range(len(data['Country'])):
    a = list(data.iloc[i,:3])
    z = checkAvail(a[0],a[1],a[2])
    if(z == -1):
        print(*a,end=" ")
        print("Service not available for this country.")
    if(z > 1):
        print(*a,end=" ")
        print("Exceeded max weight (",z,")")
    if(z == 1):
        print("Available")
