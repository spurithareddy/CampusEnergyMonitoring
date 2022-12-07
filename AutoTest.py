import os
import glob
import re

print("in")

#    with open(filepath) as f:
#        content = f.read()
#		for line in content:
#            print(line)
content=""
with open(os.path.join('C:/Users/Siri/Dropbox/CEMS/GN/FinalAccuTest', 'utthi.txt'),'a') as h:
    
    for filename in os.listdir('C:/Users/Siri/Dropbox/CEMS/GN/AutoTestFolder'):
        with open(os.path.join('C:/Users/Siri/Dropbox/CEMS/GN/AutoTestFolder', filename),'r') as f:
                  
            #content += f.read()
                #s = f.read()
                print(filename)
                for x in f.readlines():
                     #print(x)
                     data_raw=re.split(',',x)
                     p=len(data_raw)
                     #print(2)
                     if p!=1:
                         time=str(data_raw[0])              
                         if(len(time)>19):
                             #print("yes "+time+"lalalala")
                             tim=time[-19:]
                             #f.write(x.replace("14:33:00","hello"))
                             print("successs  "+tim)
                             #with open(os.path.join('C:/Users/Siri/Dropbox/CEMS/GN/AutoTestFolder', filename),'w+') as f:
                                 #for x in f.read
                                 #re.sub(time,tim,x)
                             #s=f.read()
                             x= re.sub(time,tim, x)
                             x=re.sub("\n","||"+"\n",x)
                             print(x)
                             #f.seek(0)  
                             #f.truncate()
                                 #print("---> "+s)
                             h.write(x)
                                 #f.write(re.sub("    ","\n",x))
                             print("changed "+filename)
                         else:
                             #print("in else")
                             x=re.sub("\n","||"+"\n",x)
                             h.write(x)
                          
              
              
  
            #print(filename)       
print(".. file")
#file_handle= open("C:/Users/Siri/Dropbox/CEMS/GN/FinalAccuTest/final.txt", "w")
#n = file_handle.write(content)
#file_handle.close()
		