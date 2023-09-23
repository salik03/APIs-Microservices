import pandas as pd


try:
    existing_data = pd.read_csv('address_data.csv')
except FileNotFoundError:
    
    existing_data = pd.DataFrame(columns=[
        'Type', 'Name', 'Company/House Name', 'Address 1', 'Address 2',
        'Select City', 'Zip Code', 'Country', 'Contact no', 'Email'
    ])


sender_data = pd.DataFrame(columns=existing_data.columns)
print("Enter Sender's Address:")
sender_data['Type'] = ['Sender']
sender_data['Name'] = [input("Name: ")]
sender_data['Company/House Name'] = [input("Company/House Name: ")]
sender_data['Address 1'] = [input("Address 1: ")]
sender_data['Address 2'] = [input("Address 2: ")]
sender_data['Select City'] = [input("Select City: ")]
sender_data['Zip Code'] = [int(input("Zip Code: "))]
sender_data['Country'] = [input("Country: ")]
sender_data['Contact no'] = [int(input("Contact no: "))]
sender_data['Email'] = [input("Email: ")]


receiver_data = pd.DataFrame(columns=existing_data.columns)
print("\nEnter Receiver's Address:")
receiver_data['Type'] = ['Receiver']
receiver_data['Name'] = [input("Name: ")]
receiver_data['Company/House Name'] = [input("Company/House Name: ")]
receiver_data['Address 1'] = [input("Address 1: ")]
receiver_data['Address 2'] = [input("Address 2: ")]
receiver_data['Select City'] = [input("Select City: ")]
receiver_data['Zip Code'] = [int(input("Zip Code: "))]
receiver_data['Country'] = [input("Country: ")]
receiver_data['Contact no'] = [int(input("Contact no: "))]
receiver_data['Email'] = [input("Email: ")]


combined_data = pd.concat([existing_data, sender_data, receiver_data], ignore_index=True)


combined_data.to_csv('address_data.csv', index=False)

print("\nAddress data has been saved to address_data.csv")
