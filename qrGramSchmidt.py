def vectorValid(vector): 
    """[This function will be used through out our code to check if the input we use is actually a vector by making sure that the type is a list and by checking to see if that list contains either integers or floats.This helps us by making sure that all of our inputs are correct before they are used ]
    
    Arguments:
        vector {[list]} -- [this is the vector that we are going to be checking to see if it is the correct type and if it contains integers]
    
    Returns:
        [True or False] -- [if the vector is not a list that contains integers or floats then it is invalid and returns False if it is then it is valid and returns True]
    """
    if type(vector)== list:
        'This if statement takes the vector and determines if it is a list'
        if type(vector[0]) is int or float:
            'if the vector is a list then it runs through the second if statement and checks if all the elements are integers or floats'
            return True
    else: 
        return False 

def scalarValid(scalar):
    """[This function will be used through out our code to check if the input we use is actually a scalar by making sure that the scalar is either integers or floats.This helps us by making sure that all of our inputs are correct before they are used ]
    
    Arguments:
        scalar {integer or float} --[this is the input that we will be checking =]
    
    Returns:
        [True or False] -- [if the inputed scalar is in fact an int or float then it will return True if it is not then it will return False]
    """
    if type(scalar) is int or float: 
        #this if statement tests to see if the scalar is a integer or float 
            return True
    else: 
        return False 

def vectorMultValid(vector,vector2):
    """[this function is responsible for taking two vectors and seeing if thier dimensions are compatible and able to be used in vector multiplication]
    
    Arguments:
        vector {[list]} -- [the first vector we will be testing ]
        vector2 {[list]} -- [the second vector we will be testing]
    
    Returns:
        [True or False] -- [if the lengths of the vectors are equivalent then it will return True meaning that they are able to be multiplied and if they are not the same then it will return False and they will not be valid for multiplication]
    """
    if len(vector) == len(vector2):
        #this if statement compares the lengths of the two vectors, if they are equivalent it will return True
        return True 
    else:
        return False

def matrixValid(matrix): 
    """[This function is responsible for taking the inputed matrix, and verifying that it is a list of lists and the elements within each list is in fact an integer or a float. This is done to make sure that the input being used in the function is in fact a matrix]
    
    Arguments:
        matrix {[list of lists]} -- [These matrices will be lists of lists containing integers or floats]
    Returns:
    {True or False} --[This function returns True if the matrix is in fact a list that contains a list that contains a set of numbers and returns False if any of these conditions are not met]
    """
    if type(matrix)== list:
        if type(matrix[0]) == list:
            if type(matrix[0][0]) is int or float: 
                return True
    else: 
        return False 

def vecSubtract(vector1, vector2):
    """[This vector takes two vectors and then iterates through each element of each vector and then subtracts them together and returns their subtraction result]
    
    Arguments:
        vector1 {[list]} -- [this is a list of numbers]
        vector2 {[list]} -- [this is a list of numbers]
    
    Returns:
        [ans] -- [this is the new vector that was created from the subtraction of our first two vectors]
    """
    ans = []
    "this is where we will store the new vector"
    vectorValid01 = vectorValid(vector1)
    vectorValid02 = vectorValid(vector2)
    if vectorValid01 == True:
        if vectorValid02 == True:

            for i in range(len(vector1)):
                for j in range(len(vector2)):
                    "this loops through each element in each vector and subtracts them together"
                    ans.append(vector1[i]- vector2[j])
            return ans
    else:
        return "Invalid Input" 
def scalarVecMulti(scalar,vector):
    """["This function takes a scalar and a vector and iterates through each element of the vector and multiplies it by the scalar, the new result is then added to the empty vector ans, and then returns the result as the new vector ans"]
    
    Arguments:
        scalar {[integer]} -- [this is a single integer]
        vector {[list]} -- [this is a list of numbers]
    
    Returns:
        [ans] -- [this is the new vector created from the multiplication of the scalar with the vector]
    """
    vectorValid1 = vectorValid(vector)
    scalarValid1 = scalarValid(scalar)
    if vectorValid1 == True:
        if scalarValid1 == True:
            ans =[]
            "we create a new empty list in which to place the new results"
            for i in range(len(vector)):
                "This loops through all the different elements of the vector and multiplies it by the scalar"
                ans.append(vector[i]*scalar)
            return ans 
    else:
        return "Invalid Input"

def twoNorm(vector):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the 2-norm
  if inputStatus == True:
    result = 0
# This for loop will compute the sum of the squares of the elements of the vector. 
    for i in range(len(vector)):
      result += (vector[i]**2)
    result = result**(1/2)
    return result

def normalize(vector):
    """[This function takes a vector and uses its twoNorm to normalize the vector, we will be using the twoNorm function within this function]
    
    Arguments:
        vector {takes the vector of the different columns of the inputed matrix} 
    
    Returns:
        [normalized vector] -- [this is the result of each element within the given matrix being divided by the 2norm of that vector]
    """
    vectorValid1 = vectorValid(vector)
    if vectorValid1 == True:
        ans = [] 
        "this is where we will store the new vector"
        scalar = twoNorm(vector)
        "this will store the value for the TwoNorm of the vector"
        for i in range(len(vector)): 
            "this loops through each element in the vector and returns the value divided by the infinity norm"
            ans.append(vector[i]/scalar) 
        return ans 
    else:
        return 'Invalid Input'

def TransposeMat(matrix):
    """[This function will use the inputed values of the matrix, which are organized by columns and transpose each element in a way where the result will be the columns will equal the rows]
    
    Arguments:
        matrix {[list of lists]} -- [this will the matrix that we manipulate in order to swap the columns to equal the rows]
    
    Returns:
        [matrix] -- [This is the new matrix with all of its rows and columns switched]
    """
    validOrInvalid = matrixValid(matrix)
    if validOrInvalid == True: 
        cols = len(matrix)
        rows = len(matrix[0])
        #these variables will be used to calculate the number of elements in rows and columns and then use this number to create a new empty matrix a 
        a = [] 
        #this is the new matrix where we will store our converted original matrix
        for i in range(len(matrix)):
            a.append([0*cols]*rows)
            #here is where we create the dimensions of the new matrix
            for j in range(len(matrix[0])): 
                #here is where we swap the elements of the original matrix around by equaling the rows to columns inside of the new matrix a 
                a[i][j]= matrix[j][i]
            return a 
    else:
        return "invalid input"

def dotProd(vector, vector2):
  """[This function takes two vectors as its parameters and returns the dot product]
  
  Arguments:
    vector {[list]} -- [this will be a list of numbers ]
    vector2 {[list]} -- [this will be a list of numbers]
  
  Returns:
    [ans] -- [this is the new vector that was created after the dot product operation was taken]
  """
  vectorValid01 = vectorValid(vector)
  vectorValid02 = vectorValid(vector2)
  vectorValidOrInvalid = vectorMultValid(vector,vector2)
  if vectorValid01 == True:
      if vectorValid02 == True:
          if vectorValidOrInvalid == True:
            ans = []
            "this is where we store the new vector"
            y = 0 
            "this is where we will add each element that undergoes multiplication"
            for i in range(len(vector)):
                for j in range(len(vector2)):
                    "this loops through all elements of the two vectors and multiplies them and then adds them together "
                    y += vector[i]*vector2[j]
                    ans.append(y)
                "this adds the new value for y into the new vector"
            return ans 
  else:
    return "Invalid Input" 

def qrGramSchmidt(matrix):
    """[This is the first part of the QR factorization algorithm, it takes a matrix and creates two new matrices q and r which are the result of transpositions, normalizing of the vectors within each column of the given matrix, and the scalar vector multiplication, dot product, and vector subtraction]
    
    Arguments:
        matrix {[list of list]} -- [this matrix is organized as a list of a list of columns]
    
    Returns:
        [q and r ] -- [these are the two new matrices of the same dimenion as the inputed matrix which have gone through a series of functions]
    """
    v = matrix
    r = []
    q = []
    TransposeQ = []
    #these are the set of empty matrices which we will store are results in 
    for i in range(len(v)):
        #this is where we will use are dimensions of the given matrix to create new empty matrices q and r 
        r.append([0]*len(v))
        q.append([0]*len(v))
        r[i][i] = twoNorm(v[i])
        #this is where we store the result of the two norm of all of vectors inside of the matrix inside of elements of r this should be a diagonal of numbers with zeroes left outside of the diagonal
        q[i] = normalize(v[i])
        #this is where we will normalize the vectors by the two norm and then store them in elements of q 
    TransposeQ = TransposeMat(q)
    #this is where we will store the result of passing q through the transpose function so that we can access it in the next for loop 
    for i in range(len(v)):
       for j in range(i+1,len(v)):
           #we use the for loop in order to access the elements of r that are not in the diagonal and we will fill these spaces with the dot product of the transpose of q and v[2] the last vector in the matrix  
           r[i][j] = dotProd(TransposeQ[i],v[j])
           #temp = scalarVecMulti(r[i][j], q[i])
           #we take the new matrix r and access all of its elements and multiply them to the vectors in q 
           #v[j] = vecSubtract(v[j],temp)
           #we will then use the result of temp and the last vector in the matrix v[2] and perform matrix subtraction
           #these two variables are commented out because they had an out of range error that would not allow for q and r to be printed to the terminal 
    return [q,r]

def transposeQDotY(matrix):
    """[this function uses the q that was created in the qrGramSchmidt function and transposes it and then multiplies it to the vector Y which is a given set of points]

Returns:
    {ans} -- [this returns the list of all the vectors that have undergone the dot product with y]
"""
    y =  [1.102,1.099,1.017,1.111]
    #this is the hard coded y vector 
    qrMat = qrGramSchmidt(matrix)
    #this stores the GramSchmidt into a referencable object
    qMat = qrMat[0]
    #this references q by using only the first list inside of qMat
    ans = []
    #this is the empty list where we will store the result of the dot product of the qmat and y 
    for i in range(len(qMat)):
        #we use the for loop to access all of the vectors inside of qMat and then multiply each by the vector y 
        ans.append(dotProd(qMat[i],y))
    return ans

def coeffCalc(matrix):
    """[This is where we calculate the coefficient of the ax= b equation in this case the coefficients will be of x, and the a is the hard coded vandermonde matrix of the given data points of x]

Returns:
    [the original matrix, the q and r found from the gram schmidt function, the coefficient, and the polynomial which is the coefficients multiplied to the original matrix, a ] -- [This will print out all of the important results from the previous functions and from the current function]
"""
    c = []
    polynomial = []
    #these are empty lists where we will store the result of the coefficient and the polynomial respectively
    b = transposeQDotY(matrix)
    #this is where we will access the result of the transposeQDotY function so that we can utilize it for backsubstitution
    qrmat = qrGramSchmidt(matrix)
    #this the stored result of the gram schmidt function so that we can access the q and r individually
    r = qrmat[1]
    #this r will be used within the function in order to perform the back substituion 
    c.append([0]*len(b))
    #here we will create the dimensions of the coefficients and polynomial matrix 
    polynomial.append([0]*len(b))
    for i in reversed (range(len(b))):
        #here we use the reverse function to reverse the order of the numbers in the range of the length of the b
        c[i]= b[i]
        #then we take the reverse order and save it to the i elements of the coefficient matrix
        for j in range(i+1,len(b)):
            #we then iterate through the range of the numbes from i + 1 to len(b) 
            temp = dotProd(c[j],r[j][i])
            #we then take all the vectos from c and all the vectors from r and we perform the dot product function and store the results into a temporary variable 
            c[i] = vecSubtract(c[i],temp)
            #we then store the vector subtraction of the c vectors and the new temporary variable and store them in c as the columns of c 
            c[i] = c[i]/r[i][i]
            #we then finish the back substitution by replacing the elements of c by the division of the c vector by the vectors in r 
            polynomial[i]= dotProd(c,matrix[i])
            #using the new coefficients vector we can take the dot product of it and the original matrix's vectors and store the result as the polynomial variable 
        return [matrix,qrmat[0],r, c, polynomial]




        
   
  

   


  


matrix01= [[1,.55,.3025,.166],[1,.60,.36,.216],[1,.65,.4225,.275],[1,.70,.49,.343]]
print(coeffCalc(matrix01))

