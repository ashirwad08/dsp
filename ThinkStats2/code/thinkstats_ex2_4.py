import pandas as pd
import numpy as np
import nsfg
import math


def cohensd(firstBorn_wgts,laterBorn_wgts):
  """Takes in two series: First born baby weight observations and later born baby weights. Computes the Cohen's D effect size between the groups and makes a determination as to which group is heavier than the other"""
  
  
  #cohens d = (mean1-mean2)/pooled std. dev.
  #pooled std. dev., s = sqrt( (n1*v1 + n2*v2)/(n1+n2) )
  
  cohensd = (firstBorn_wgts.mean()-laterBorn_wgts.mean())/(math.sqrt((len(firstBorn_wgts)*firstBorn_wgts.var() + len(laterBorn_wgts)*laterBorn_wgts.var())/(len(firstBorn_wgts)+len(laterBorn_wgts)) ))
  
  #print(cohensd)
  
  return cohensd
  
  
  


def readData():
  """
  Uses nsfg module's Read and Clean functions to load the CDC's NSFG survey data; returns a dataframe.
  """  
  
  df = nsfg.ReadFemPreg()
  nsfg.CleanFemPreg(df)
  return df


def createGroups(df):
  """ 
  Extract from the pregnancy data frame two Series of total baby weights, each representing first born babies and non-first born babies. Return two groups as series in a tuple.
  """
  
  
  frstBorn_wgts = pd.Series()
  ltrBorn_wgts = pd.Series()
  
  frstBorn_wgts = df[(df.birthord == 1)&(~pd.isnull(df.totalwgt_lb))]['totalwgt_lb']
  
  ltrBorn_wgts = df[(df.birthord > 1)&(~pd.isnull(df.totalwgt_lb))]['totalwgt_lb']
  
  return frstBorn_wgts,ltrBorn_wgts


def main():
  
  df = readData()
  first,later = createGroups(df)
  d = cohensd(first,later)
  
  if d < 0:
    print "\nFirst Born babies are typically lighter than later borns by approximately " + str(round(abs(d),3)) + " standard deviations."
  elif d > 0:
    print "\nFirst Born babies are typically heavier than later borns approximately " + str(round(abs(d),3)) + " standard deviations."
  else:
    print "\nThere is no variation between the weights of First Born and Later Born babies. The Cohens D measure is 0, indicating no deviations from the mean difference in both groups."
  
  
if __name__=="__main__":
  main()
  
