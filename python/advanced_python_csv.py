# this function is called from advanced_python_regex.py
def emails2CSV(emailList):
  """Receive a list of emails and write to a csv file"""
  import csv
 
  #insert extra newline characters in list
  #for i in range(len(emailList)):
   # emailList[i]=emailList[i]+'\n'
  
  try:
    with open("emails.csv","w") as csvfile:
      emailWriter = csv.writer(csvfile, delimiter='\n')
      print('\n5. Writing emails to csv "emails.csv"\n')
      emailWriter.writerow(emailList)
  except IOError:
    print('cannot open/create/rwite '+csvfile)
    
  csvfile.close()
  
      
  
    
  
  
