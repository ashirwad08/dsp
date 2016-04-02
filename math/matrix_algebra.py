# Matrix Algebra

import numpy as np
#from pprint import pprint

def main():
  #Matrices dict
  Mat = {'A': np.array([[1,2,3],[2,7,4]]), 'B': np.array([[1,-1],[0,1]]), 'C': np.array([[5,-1],[9,1],[6,0]]), 'D': np.array([[3, -2, -1],[1,2,3]]), 'u': np.array([6,3,-3,5]), 'v': np.array([3,5,-1,4]), 'w': np.array([(1),(8),(0),(5)])}
  
  
  # SOLUTIONS
  
  ##1 Dimensions
  print('\n Matrix Dimensions:')
  for k,v in Mat.iteritems():
    print(k + "=" + str(v.ndim))
    
  """
   Matrix Dimensions:
  A=2
  C=2
  B=2
  D=2
  u=1
  w=1
  v=1
  """
  
  #2 Vector Operations
  print('\n Vector Operations: ') 
  print("u+v = "+str(Mat['u']+Mat['v'])) #u+v = [ 9  8 -4  9]
  print("u-v = "+str(Mat['u']-Mat['v'])) #u-v = [ 3 -2 -2  1]
  print("6*u = "+str(6*Mat['u'])) #6*u = [ 36  18 -18  30]
  print("u.v = "+str(Mat['u'].dot(Mat['v']))) #u.v = 56
  print("||u|| = "+str(np.sqrt(sum(Mat['u']**2)))) #||u|| = 8.88819441732
  
  #3 Matrix Operations
  print('\n Matrix Operations: ')
  try:
    #print("A+C = ", (Mat['A']+Mat['B'])) #invalid
    
    print("A-C' = ", (Mat['A']+Mat['C'].T))
    """
    ("A-C' = ", array([[ 6, 11,  9],
      [ 1,  8,  4]]))
    """

    print("C'+3D = ", (Mat['C'].T+3*Mat['D']))
    """
    ("C'+3D = ", array([[14,  3,  3],
       [ 2,  7,  9]]))
    """
    
    print("BA = ", (Mat['B'].dot(Mat['A'])))
    """
    ('BA = ', array([[-1, -5, -1],
       [ 2,  7,  4]]))
    """
    
    #print("BA' = ", (Mat['B'].dot(Mat['A'].T))) #invalid
    
    #print("BC = ", (Mat['B'].dot(Mat['C']))) #invalid
    
    print("CB = ", (Mat['C'].dot(Mat['B'])))
    """
    ('CB = ', array([[ 5, -6],
       [ 9, -8],
       [ 6, -6]]))
       """
       
    print("B^4 = ", (Mat['B']**4))
    """
    ('B^4 = ', array([[1, 1],
       [0, 1]]))
       """
       
    print("AA' = ", (Mat['A'].dot(Mat['A'].T)))
    """
    ("AA' = ", array([[14, 28],
       [28, 69]]))
       """
       
    print("D'D = ", (Mat['D'].T.dot(Mat['D'])))
    """
    ("D'D = ", array([[10, -4,  0],
       [-4,  8,  8],
       [ 0,  8, 10]]))
       """
    
  except ValueError as e:
    print("Invalid Operation: ",e)
  
  
















if __name__=='__main__':
  main()
