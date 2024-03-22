import pandas as pd
print(pd.__version__)
# Second- Series Are Like Column
data = [1,12,114,141]
result  = pd.Series(data)
print(result)
# Work with Dictionary
data = {"Ak": 1,"Ck": 44,"Tk": 11}
result  = pd.Series(data)
print(result)
# Label
data = [1,12,114,141]
result  = pd.Series(data,["x","y","A","a"])
print(result)
# Data Set
data = {"Marks": [1,2,45,65],"Name": ["Ali","Hassan","Akram","Faizan"]}
result  = pd.Series(data)
print(result)
#3rd - Dataframe
data = {"Marks": [1,2,45,65],"Name": ["Ali","Hassan","Akram","Faizan"]}
result  = pd.DataFrame(data)
print(result)
