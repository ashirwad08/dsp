import re
import csv
from pprint import pprint


def createDictI(faculty):
  """Receives a dictionary and creates a new one with last name as keys and degree title and email as a list of values. Note all the values are  cleaned"""
  
  q6Dict = {}
  lnames = []
  
  #first, extract last names from faculty names
  for name in faculty['name']:
    lnames.append(re.search('\w+$',name).group())
  
  lnames=list(set(lnames)) #unique names
      
  
  #now, each lname is a key for the new dict. For each name, iterate through faculty['name'], and for every match, append a list containing degree, title, email
  
  
  for lname in lnames:
    i=0
    for fname in faculty['name']:
      if lname == re.search('\w+$',fname).group():
        q6Dict.setdefault(lname,[]).append(list((faculty[' degree'][i],faculty[' title'][i],faculty[' email'][i])))
      i += 1
      
  print('\n6. Dictionary: \n')
  for k in sorted(q6Dict.keys())[:3]:
    print(k, q6Dict[k][:3])
  
  #return q6Dict




def createDictII(faculty):
  """Receives a dictionary and creates a new one with first and last name as key tuple and degree title and email as a list of values. Note all the values are  cleaned"""
  
  q7Dict = {}
  flnames = []
  
  #first, extract last names from faculty names
  for name in faculty['name']:
    flnames.append( (re.search('^\w+',name).group(),re.search('\w+$',name).group()) )
  
  flnames=list(set(flnames)) #unique names
      
  
  #now, each flname is a key for the new dict. For each name, iterate through faculty['name'], and for every match, append a list containing degree, title, email
  
  
  for flname in flnames:
    i=0
    for fname in faculty['name']:
      if flname[1] == re.search('\w+$',fname).group() and flname[0] == re.search('^\w+',fname).group():
        q7Dict.setdefault(flname,[]).append(list((faculty[' degree'][i],faculty[' title'][i],faculty[' email'][i])))
      i += 1
      
  print('\n7. Dictionary, sorted by first name: \n')
  for k in sorted(q7Dict.keys())[:3]:
    print(k, q7Dict[k][:3])
  
  
  print('\n7. Dictionary, sorted by last name: \n')
  for k in sorted(q7Dict.keys(), key=lambda x: x[1])[:3]:
    print(k, q7Dict[k][:3])




def cleanFacDict(faculty):

  """Receive the faculty dictionary, normalize the 'degree' values, and print the unique number of degrees and their frequencies"""


  deg_cleaner = {'MD.':'[mM]\.*[dD]\.*', 'MPH.':'[mM]\.*[pP]\.*[hH]\.*', 'Ph.D.':'[pP]\.*[hH]\.*[dD]\.*','Sc.D.':'[sS]\.*[cC]\.*[dD]\.*', 'MS.':'[mM]\.*[sS]\.*', 'JD.':'[jJ]\.*[dD]\.*','MA.':'[mM]\.*[aA]\.*'}
  
  title_cleaner = {'Assistant Professor': '^Assistant.+$', 'Professor': '^Professor.+$', 'Associate Professor': '^Associate.+$'}
  

  for cleanVal,regEx in deg_cleaner.iteritems():
    for i in range(len(faculty[' degree'])):
      faculty[' degree'][i] = re.sub(regEx, cleanVal, faculty[' degree'][i]).strip()
      
   
  for cleanVal,regEx in title_cleaner.iteritems():
    for i in range(len(faculty[' title'])):
      faculty[' title'][i] = re.sub(regEx, cleanVal, faculty[' title'][i]).strip()
    









def main():

  faculty = {}
  emailList = []

  with open('faculty.csv') as rawfile:
    reader = csv.DictReader(rawfile)
    for row in reader:
      for column, values in row.iteritems():
        faculty.setdefault(column, []).append(values)
        
  rawfile.close()
  
  cleanFacDict(faculty)
  #answer to q6
  createDictI(faculty)
  #answer to q7
  createDictII(faculty)
  
  
  
if __name__ == '__main__':
    main()
