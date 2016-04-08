[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

# Actual Vs. Biased Distributions 

This exercise uses the Female Respondents dataset found in the NSFG survey dataset. We're going to take a look at the survey respondents distribution and compare it to the biased distribution which occurs when the children are asked about how many children are in their family.  

## Read Data  

Use chapter 01's ReadFemResp() function to read in teh data:  
```python
def readData():
  """
  Uses ReadFemResp() in chapter 1 code to read the female respondents file.
  """  
  
  df = chap01soln.ReadFemResp()
  return df
```  

# Actual Distribution  
  
The first step is to isolate the target variable *numkdhh* - number of kids in household - and plot its distribution as a histogram of values.  

```python
#historgram code
```  

The distribution looks like this:  HIST IMAGE
