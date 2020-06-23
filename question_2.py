# Our brain can read texts even if letters are jumbled, like the following sentence: 
# “ Yuo cna porbalby raed tihs esaliy desptie teh msispeillgns.” Given two strings, 
# write a method to decide if one is a partialpermutation of the other. Consider a
# partialpermutation only if:
#   The first letter hasn’t changed place  
#   If word has more than 3 letters, up to 2/3 of the letters have changed place
  

 
def partialPermutation(str1, str2): 
    """ function to decide if one is a partialpermutation of the other"""

    # Get lenghts of both strings 
    n1 = len(str1) 
    n2 = len(str2) 
  
    # The length must be the same 
    if (n1 != n2): 
        return False
             
    # The first letter must be the same 
    if str1[0] != str2[0]:
        return False
    else:
        count = 0           
      
        for i in range(1, n1):
          # Find how many letters are differents
          if str1[i] != str2[i]:
            count = count + 1

        if n1 > 3:
          aux = n1 * (2/3)
          if count < aux:
            return True
          else:
            return False
        elif count > 0:
          return True
        else:
          return False 
  
# Driver Code 
if __name__ == '__main__': 
    
    if (partialPermutation("you", "yuo")): 
        print("true") 
    else: 
        print("false")

    if (partialPermutation("probably", "porbalby")): 
        print("true") 
    else: 
        print("false")

    if (partialPermutation("despite", "desptie")): 
        print("true") 
    else: 
        print("false")

    if (partialPermutation("moon", "nmoo")): 
        print("true") 
    else: 
        print("false")

    if (partialPermutation("misspellings", "mpeissngslli")): 
        print("true") 
    else: 
        print("false")


"""
The algorithm complexity is O(n^2), because two strings are being compared. 
The space complexity of this algorithm depends of string length. 
"""