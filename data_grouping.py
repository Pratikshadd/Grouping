import pandas as pd 
import numpy as np

def data_subset(filename = 'filename.xlsx', sheet_name='sheet_name') :
    data = pd.read_excel(filename,sheet_name = sheet_name) #reading excel file
    data = data[['Date','Tier','Country','Total # of Users']] #selecting required columns 
    return data #returning excel


def data_analysis(data, tier_value = '30 Day Trial') :
    #selecting rows whose tier value is given
    data1 = data[data['Tier'] == tier_value] 
    #creating date format to year-month format
    data1['month'] = data1['Date'].apply(lambda x:str(x).split('-')[0]+'-'+str(x).split('-')[1])
    #initating empty dataframe to collate values
    df_collated = pd.DataFrame()
    for country in data1['Country'].unique() :
        #selecting rows whose country is given
        data2 = data1[data1['Country']==country]
        #grouping users based on month-year values
        df = data2.groupby(['month'])['Total # of Users'].sum()
        df = df.to_frame()
        df.reset_index(inplace = True)
        df['Tier'] = tier_value
        df['Country'] = country 
        print (df.head())
        df_collated = df_collated.append(df)
    return df_collated


if __name__ == '__main__':
    data = data_subset()
    df_collated = data_analysis(data,'30 Day Trial')
    print (df_collated.head(10))
    df_collated = data_analysis(data,'7 Day Trial')
    print (df_collated.head(10))
