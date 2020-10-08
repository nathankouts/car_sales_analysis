#this python file is going to replace all the missing values from our dataframe and save our dataframe as an *.xlsx file so we can import it in Tableau
#first import modules
import pandas as pd

#let's open the csv file
df = pd.read_csv(r'C:/Users/Nathan/Desktop/Car_sales.csv')

#Replace missing values with the average
df['Engine_size'].fillna((df['Engine_size'].mean()), inplace=True)
df['Horsepower'].fillna((df['Horsepower'].mean()), inplace=True)
df['__year_resale_value'].fillna((df['__year_resale_value'].mean()), inplace=True)
df['Price_in_thousands'].fillna((df['Price_in_thousands'].mean()), inplace=True)
df['Power_perf_factor'].fillna((df['Power_perf_factor'].mean()), inplace=True)
df['Fuel_capacity'].fillna((df['Fuel_capacity'].mean()), inplace=True)
df['Curb_weight'].fillna((df['Curb_weight'].mean()), inplace=True)

#now let's save it as an xlsx file
df.to_excel('C:/Users/Nathan/Desktop/car_tab.xlsx')