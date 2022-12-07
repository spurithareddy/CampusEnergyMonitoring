import datetime
import time
import re ## for splitting
import os
import errno
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import date, timedelta


connection = mysql.connector.connect(host='localhost',
                                     database='gnits',
                                     user='root', # your database user name
                                     password='Ponnu @123mysql') # your database passord
print("connection established")

cursor = connection.cursor()


date_time=datetime.datetime.now()
if date_time.hour==00 and date_time.minute==00:
   line_number=1
   f_line=open('C:/Users/Siri/Sample_codes/gnits_line_number.txt','w') # line number filepath and line number file name
   f_line.write(str(datetime.datetime.now())+','+str(line_number))
   f_line.close()
#print(cursor)
f_line_number=open('C:/Users/Siri/Sample_codes/gnits_line_number.txt','r')# line number filepath and line number file name
line_read=f_line_number.readline().split(',')
line_number=int(line_read[1])
print(line_number)
f_line_number.close()
#file_path="C:/Users/EEE005/Dropbox/CEMS/GN/GN_" # dropbox folder where the data is being stored
filename="C:/ProgramData/MySQL/MySQL Server 5.7/Data/gnits/GN_2020-02-19.txt"
f=open(filename,'r')

for x in f.readlines():
   f.seek(line_number,0)
   x=f.readline()
   line_number=f.tell()
   data_raw=re.split(',',x)
   p=len(data_raw)
   if p!=1:
    time=str(data_raw[0])
    if(len(time)>19):
	    time=time[-19:]   
    P_total=str(data_raw[2])
    P_r=str(data_raw[3])
    P_y=str(data_raw[4])
    P_b=str(data_raw[5])
    Pf_avg=str(data_raw[6])
    Pf_r=str(data_raw[7])
    Pf_y=str(data_raw[8])
    Pf_b=str(data_raw[9])
    S_t=str(data_raw[10])
    S_r=str(data_raw[11])
    S_y=str(data_raw[12])
    S_b=str(data_raw[13])
    Vl_avg=str(data_raw[14])
    V_ry=str(data_raw[15])
    V_yb=str(data_raw[16])
    V_br=str(data_raw[17])
    Vln_avg=str(data_raw[18])
    V_r=str(data_raw[19])
    V_y=str(data_raw[20])
    V_b=str(data_raw[21])
    I_t=str(data_raw[22])
    I_r=str(data_raw[23])
    I_y=str(data_raw[24])
    I_b=str(data_raw[25])
    freq=str(data_raw[26])
    Energy=str(data_raw[27])
    Vah=str(data_raw[28])
    query="""INSERT INTO `mdata`(`tstamp`, `meter_ID`, `Ptot`, `Pr`, `Py`, `Pb`, `PFa`, `PFr`, `PFy`, `PFb`, `St`, `Sr`, `Sy`, `Sb`, `VLa`, `Vry`, `Vyb`, `Vbr`, `Va`, `Vr`, `Vy`, `Vb`, `It`, `Ir`, `Iy`, `Ib`, `freq`, `Energy`, `VAh`, `Area`) VALUES """
    query+="('"+time+"'"+","+str(data_raw[1])+","
    query+=P_total+","+P_r+","+P_y+","+P_b+","+Pf_avg+","+Pf_r+","
    query+=Pf_y+","+Pf_b+","+S_t+","+S_r+","
    query+=S_y+","+S_b+","+Vl_avg+","+V_ry+","+V_yb+","+V_br+","+Vln_avg+","+V_r+","+V_y+","+V_b+","+I_t+","+I_r+","+I_y+","+I_b+","+freq+","
    query+=Energy+","+Vah+","+"'GNITS'"")"
    print(query)
    result  = cursor.execute(query)
    connection.commit()
   f_line=open("D:/Sample_Codes/gnits_line_number.txt","w")
   f_line.write(str(datetime.datetime.now())+','+str(line_number))
   f_line.close()
print("data_inserted")