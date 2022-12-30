import pandas as pd
import numpy as np
import json
import pymongo
df=pd.read_excel('C:/Deep Neuron/pandas dataset/Superstore_USA.xlsx')
df.reset_index(drop=True,inplace=True)
json_record=list(json.loads(df.T.to_json()).values())
#print(json_record[0])

client = pymongo.MongoClient("mongodb+srv://prabhat:mongodb123@cluster0.iean9di.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
mydb=client['store']
coll=mydb['superstore_USA']
coll.insert_many(json_record)
print('successfully inserted')
