# Hint:  use Google to find python function

from datetime import datetime



def dt(start,stop,format):
  dstart = datetime.strptime(start,format)
  dstop = datetime.strptime(stop,format)
  print((dstop-dstart).days,'days!')


####a) 
start = '01-02-2013'  
stop = '07-28-2015'
dt(start,stop,'%m-%d-%Y')  

####b)  
start = '12312013'  
stop = '05282015'  
dt(start,stop,'%m%d%Y')

####c)  
start = '15-Jan-1994'  
stop = '14-Jul-2015'  
dt(start,stop,'%d-%b-%Y')




