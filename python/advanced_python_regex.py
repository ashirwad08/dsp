import csv
import re
from pprint import pprint
import advanced_python_csv

def degrees(faculty):

  """Receive the faculty dictionary, normalize the 'degree' values, and print the unique number of degrees and their frequencies"""



  #Data shows the following set:
  #MD MPH PhD ScD BSEd MS JD MA

  #iterate through the list for "degree" and count total subs
  cleaner = {'MD':'[mM]\.*[dD]\.*', 'MPH':'[mM]\.*[pP]\.*[hH]\.*', 'PhD':'[pP]\.*[hH]\.*[dD]\.*','ScD':'[sS]\.*[cC]\.*[dD]\.*', 'MS':'[mM]\.*[sS]\.*', 'JD':'[jJ]\.*[dD]\.*','MA':'[mM]\.*[aA]\.*'}

  deg_freq = {'degree': [], 'freq': []}

  for cleanVal,regEx in cleaner.iteritems():
    deg_freq['degree'].append(cleanVal)
    s = 0
    for deg in faculty[' degree']:
      s += (re.subn(regEx, cleanVal, deg))[1]
    
    deg_freq['freq'].append(s)
    
  print('\n1. Degrees and Frequencies: \n')  
  pprint(deg_freq)




def titles(faculty):
  """Receive the faculty dictionary, normalize the 'title' values, and print the unique number of titles and their frequencies"""
   
  #Data shows the following set:
  #"Assistant Professor", "Professor", "Associate Professor"
  #iterate through the list for "degree" and count total subs
  
  cleaner = {'Assistant Professor': '^Assistant.+$', 'Professor': '^Professor.+$', 'Associate Professor': '^Associate.+$'}
  
  title_freq = {'title': [], 'freq': []}


  for cleanVal,regEx in cleaner.iteritems():
    title_freq['title'].append(cleanVal)
    s = 0
    for title in faculty[' title']:
      s += (re.subn(regEx, cleanVal, title))[1]
    
    title_freq['freq'].append(s)
    
  print('\n2. Titles and Frequencies: \n')  
  pprint(title_freq)




def emailaddys(faculty):
  """Receive faculty dictionary, get all email addresses, and store them in a list; return this list"""
  
  emails = []
  for email in faculty[' email']:
    emails.append(email)
  
  print('\n3. The list of emails are: \n')
  pprint(emails)
  
  return emails


def emailDomains(emailList):
  """Receive a list of emails, and print the various unique email domains"""
  
  domains = []
  
  for email in emailList:
    domains.append(re.search('@\S+', email).group())
  
  print('\n4. Here are the UNIQUE email domains: \n')
  pprint(list(set(domains)))
  



  
  



def main():

  faculty = {}
  emailList = []

  with open('faculty.csv') as rawfile:
    reader = csv.DictReader(rawfile)
    for row in reader:
      for column, values in row.iteritems():
        faculty.setdefault(column, []).append(values)
        
  rawfile.close()
  degrees(faculty)  
  titles(faculty)
  emailList = emailaddys(faculty)
  emailDomains(emailList)
  advanced_python_csv.emails2CSV(emailList)
  
  




if __name__ == '__main__':
    main()
      
