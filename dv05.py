import pandas as pd

sd = pd.read_csv('static/starbucks.csv', delimiter='|', encoding='utf-8')
print(sd.head())

nm = sd['Store_nm']
ad = sd['Address']
te = sd['Telephone']
ca = sd['Category']
lo = sd['Ycoordinate']
la = sd['Xcoordinate']