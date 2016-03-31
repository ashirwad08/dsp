# this function is called from advanced_python_regex.py
def emails2CSV(emailList):
  """Receive a list of emails and write to a csv file"""
  import csv
 
  
  try:
    with open("emails.csv","w") as csvfile:
      emailWriter = csv.writer(csvfile, delimiter=',')
      print('\n5. Writing emails to csv "emails.csv"\n')
      emailWriter.writerow(emailList)
  except IOError:
    print('cannot open/create/rwite '+csvfile)
    
  csvfile.close()
  
      
  
    
  
  
