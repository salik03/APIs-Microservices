import pandas as pd
data = pd.read_csv("./CountryData.csv")
details = pd.read_csv("./ServiceDetails.csv")

country = input("Country : ")
service = int(input("1-5 : "))
index = list(data['Country'].values).index(country)

availability= data.iloc[index,service]
weight = details.iloc[0,service-1]
insurance = details.iloc[1,service-1]

print("Availability : ", availability)
if(availability==1):
     print("\nWeight : ", weight,"\nInsurance", insurance)