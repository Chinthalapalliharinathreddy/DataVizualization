import pandas as pd
data={
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Marks":[30,45,35,67,96,78,89,90,95,100]
}
df=pd.DataFrame(data)
print(df.corr())