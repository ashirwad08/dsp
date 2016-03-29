# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists are mutable, whereas tuples are immutable. Conseuqnetly lists are typically used for homogenous elements and which are accessed by iterating over the list, whereas tuples are used for sequencing heterogenous elements that are accessed via unpacking or indexing. Tuples will work as keys in dictionaries because distionaries require immutable objects to compute the hash values. 


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

A set seems to be a list with a unique unordered collection of elements. If we were to find an element on a list, we have to iterate potentially over every element og the list which results in a O(n) performance order, however since sets use a hash function to map each unique element to a bucket, testing for presence in a set is significantly faster, no matter the size of the set, that is it is O(constant).   

* List search: _l = [1, 2, 3, 4, 5, 5, 6, 6, 7]_; _5 in l_   
* Set: s = set(l); 5 in s

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

lambda is a way to define and use a single expression anonymous function when required:  
```python
print sorted(l, key=lambda elm: elm/random.randint(1,100)) #sorts the above list based on each element being divided by a random number.   
```  

another example uses f to raise to any exponent: 
```python  
def ex(n): 
  return lambda(x)=x**n

f = ex(5)
f(2) #returns 32.
```  

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehension is a compact way to write an expression that expands into a whole list.Syntax: _[expr for var in list]_  

#### Sample Problem  
Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6].  

##### Solution Using List Comprehension  

```python
def cumsum(l):
  [sum(l[:i+1]) for i in range(len(l))] 
```  
  

##### Solution Using Map and Filter  
```python
def cumsum(l):
  csuml = []
  for i in range(len(l)):
    csuml.append(sum(l[:i+1])) #map using sum() and filter until the first i+1 elements
  return csuml
```
##### Set Comprehension Example  
```python
{sum(l[:i+1]) for i in range(len(l))} #same output as above except unordered (and unique, but not applicable here)
```  

##### Dict Comprehension Example
```python
#generate a dict of squares using dict comp.
{k:v**2 for k,v in l}

#iterate over existing dict
{key:expr for key,val in dict.iteritems()}
```  
 
---  


###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

_answer is 937 days_  
)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

_answer is 513 days_  


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

_answer is 7850 days._  


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





