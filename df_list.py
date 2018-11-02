import pandas as pd

def df_to_list(dataframe):
    output=dataframe.values.tolist()
    return output
df=pd.DataFrame({"name":["Vipin","Gupta"]})
print(df_to_list(df))