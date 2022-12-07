import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pymysql
from sqlalchemy import create_engine
db_connection_str = 'mysql+pymysql://root:Ponnu @123mysql@localhost/gnits'
db_connection = create_engine(db_connection_str)
df = pd.read_sql('SELECT * FROM fbstatus', con=db_connection)
#print(df)
numeric_columns=['status_id','s_text','t_status']
sns.heatmap(df[numeric_columns].corr(),annot=True,cmap='terrain',linewidths=0.1)
fig=plt.gcf()
fig.set_size_inches(8,6)
print(plt.show())