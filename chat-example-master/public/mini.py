import numpy as np
import pandas as pd

from sqlalchemy import create_engine
import pymysql
db_connection_str ='mysql+pymysql://root:Ponnu @123mysql@localhost/gnits'
db_connection = create_engine(db_connection_str)
df=pd.read_sql('select * from mdata ',con=db_connection)
print("1")
df['hour'] = [d.strftime("%H") for d in df['tstamp']]
df['date'] = [d.strftime("%d") for d in df['tstamp']]
df['time'] = [d.time() for d in df['tstamp']]
df['weekday'] = [d.weekday() for d in df['tstamp']]
conditions = [
    ((df['hour'].astype(int))< 5),
    (df['hour'].astype(int) >= 5) & (df['hour'].astype(int) < 9),
    (df['hour'].astype(int) >= 9) & (df['hour'].astype(int) < 12),
    (df['hour'].astype(int) >= 12) & (df['hour'].astype(int) < 16),
    (df['hour'].astype(int) >= 16) & (df['hour'].astype(int) < 21),
    (df['hour'].astype(int) >= 21) & (df['hour'].astype(int) <24)
    ]

# create a list of the values we want to assign for each condition
#values = ['ln', 'em', 'm', 'a','e','n']
values = [0, 1, 2, 3, 4, 5]

# create a new column and use np.select to assign values to it using our lists as arguments
df['part'] = np.select(conditions, values)
#df.drop(columns=['tstamp','hour'])
df['month'] = df['tstamp'].dt.month
df['year'] = df['tstamp'].dt.year
#df.drop(columns=['tstamp','hour'],inplace=True)
df.to_sql('mldata' ,db_connection, if_exists = 'replace')
print("2")
new_df=pd.read_sql('select month,date,AVG(Energy),part,meter_ID,weekday from mldata GROUP BY month,date,meter_ID,weekday,part',con=db_connection)
print("3")
X = df.iloc[:,[3,4,5]].values   # select input columns weekday(column# 4), part(column# 5)
y = df.iloc[:,[2]].values    # lablel Energy(column#)
y = y.reshape((-1,))
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=2)
import lightgbm as lgb

d_train = lgb.Dataset(x_train, label=y_train)
d_test = lgb.Dataset(x_test, label=y_test)

params = {}
params['learning_rate'] = 0.003
params['boosting_type'] = 'gbdt'
params['objective'] = 'regression'
params['metric'] = 'rmse'
params['sub_feature'] = 0.5
params['num_leaves'] = 20
params['min_data'] = 50
params['max_depth'] = 20
#clf = lgb.train(params, d_train, 1000,valid_sets=d_test, categorical_feature=[0,1,2])
clf = lgb.train(params, d_train, 1000,valid_sets=d_test)
y_pred = clf.predict(x_test)
list(zip(y_test, y_pred))
print("4")
y_pred1 = clf.predict(0,2,3)
print(y_pred1)