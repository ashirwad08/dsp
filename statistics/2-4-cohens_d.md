[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

# Analyze Effect Size of Weight Between First and Later Babies  

This report uses the *CDC's* *National Survey of Family Growth* (NSFG) dataset. More info about the dataset is [here](http://cdc.gov/nchs/nsfg.htm). For this exercise I will investigate the following:  
> Using the variable totalwgt_lb, investigate whether first babies
are lighter or heavier than others. Compute Cohen’s d to quantify the
difference between the groups. How does it compare to the difference in
pregnancy length?  

# Reading Data
Allen Downey provides the functions to read in the dataset. I'll simply import his module and read in the dataset:  
```python
def readData():
  """
  Uses nsfg module's Read and Clean functions to load the CDC's NSFG survey data; returns a dataframe.
  """  
  
  df = nsfg.ReadFemPreg()
  CleanFemPreg(df)
  return df
```  

# Extracting Baby Weights Based on Birth Order  
Downey's ` CleanFemPreg()` function above has already computed total baby weights in lbs for us. We make use the ` birthorder` column to filter our total weights into two Series: One containing the weights of babies with ` birthorder == 1` and the other containing weights of babies born later, that is ` birthorder > 1`:  
```python
def createGroups(df):
  """ 
  Extract from the pregnancy data frame two Series of total baby weights, each representing first born babies and non-first born babies. Return two groups as series in a tuple.
  """
  
  
  firstBorn_wgts = pd.Series()
  ltrBorn_wgts = pd.Series()
  
  frstBorn_wgts = df[(df.birthord == 1)&(~pd.isnull(df.totalwgt_lb))]['totalwgt_lb']
  
  ltrBorn_wgts = df[(df.birthord > 1)&(~pd.isnull(df.totalwgt_lb))]['totalwgt_lb']
  
  return firstBorn_wgts,ltrBorn_wgts
```  

# Compute Cohen's D  
Using Cohen's d as the effect size between each group, we compute this:  
```python
def cohensd(firstBorn_wgts,laterBorn_wgts):
  """Takes in two series: First born baby weight observations and later born baby weights. Computes the Cohen's D effect size between the groups and makes a determination as to which group is heavier than the other"""
  
  
  #cohens d = (mean1-mean2)/pooled std. dev.
  #pooled std. dev., s = sqrt( (n1*v1 + n2*v2)/(n1+n2) )
  
  cohensd = (firstBorn_wgts.mean()-laterBorn_wgts.mean())/(math.sqrt((len(firstBorn_wgts)*firstBorn_wgts.var() + len(laterBorn_wgts)*laterBorn_wgts.var())/(len(firstBorn_wgts)+len(laterBorn_wgts)) ))
  
  #print(cohensd)
  
  return cohensd
```   

# Result  

The Cohen's D of approximately **-0.089 lbs.** when comparing first born babies to later born babies suggests that the standard deviation between means of the two groups is rather trivial. So no inferences can be confidently made around any probable hypothesis that compares weights of First borns to later borns.  

The very trivial mean difference between pregnancies of 0.078 suggests that although first time pregnancies take slightly longer whereas the birth weights of babies are slightly lesser. These are both very trivial effects.   

---  
**End of Report**  
 
