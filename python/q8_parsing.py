#The football.csv file contains the results from the English Premier League. 
# The columns labeled Goals and Goals Allowed contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
#  
#

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def read_data(datapath):
  gd = {}
  """read a csv of EPL season results into a dictionary, keyed by its header row"""
  with open('football.csv') as rawfile:
      reader = csv.DictReader(rawfile)
      for row in reader:
          gd[row['Team']] = int(row['Goals'])-int(row['Goals Allowed'])
  
  rawfile.close()
  return gd       
              

def get_team(gd):
  
  #reverse lookup the minimu value for the keys
  mingd=min(gd.values())
  for key in gd:
      if gd[key]==mingd:
          #print key
          print(key+" has the worst goal difference of %d goals. \n" % mingd)
              



def main():
    datapath = 'football.csv'
    get_team(read_data(datapath))
  

  
    
if __name__ == '__main__':
    main()