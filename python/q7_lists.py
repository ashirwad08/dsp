# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    return len([s for s in words if len(s)>=2 and s[0]==s[len(s)-1]])



def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    words.sort()
    final = []
    length = len(words)
    i=0
    
    #iterate only once instead of twice with list comprehensions
    while i < length:
        if words[i][0]=='x':
            final.append(words.pop(i))
            length = len(words)
            i -= 1
        i += 1
      
    final.extend(words)
        
    
    #final.extend([w for w in words if w[0]=='x'])        
    #final.extend([w for w in words if w[0]!='x'])
    
    return final


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    def second(t):
        return t[len(t)-1]
    
    return sorted(tuples, key=second)


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    
    i = len(nums)-1
    #preserved = False
    
    while i > 0:
        if nums[i]-nums[i-1] == 0:
            nums.pop(i)
            #preserved = True
        #else:
            #preserved = False 
            
        i -= 1
    
    return nums
    
    

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """ 
    
    #stack = ()
    merged = []
    
    
    #boundary conditions since lists are laready sorted
    if list1[len(list1)-1] <= list2[0]:
        list1.extend(list2)
        return list1
    elif list1[0] >= list2[len(list2)-1]:
        list2.extend(list1)
        return list2
    else:
        i = 0
        j = 0
       
        while len(list1)>0 and len(list2)>0:
            if list1[i] < list2[j]:
                merged.append(list1[i])
                list1.remove(list1[i])
            else:
                merged.append(list2[j])
                list2.remove(list2[j])
        
        #append remaining from any list
        merged.extend(list1)
        merged.extend(list2)
                
        return merged
            
        
                
    
    
    
    
    
    
    
    
    
    
  
