# There are three types of typos that can 
# remove a character, or replace a character.  
# Given two strings, write a function to
# check if they are one typo (or zero typos) away. 
      
def areThereOneTypo(str1, str2):
    """Check if they are one typo (or zero typos) away."""
      
    # Get lenghts of both strings 
    n1 = len(str1) 
    n2 = len(str2) 
  
    #The length difference must not be greater than one
    if n1-n2>1 or n2-n1>1: 
        return False
    
    i = 0
    j = 0
    count = 0         
    
    #Loop until the last position
    while i < n1 and j < n2:
        string_1 = str1[i]
        string_2 = str2[j]

        #Compare "chars" of both strings
        if string_1 != string_2:
            count = count + 1
            if n1 > n2:
                i = i + 1
            if n2 > n1:
                j = j + 1
            if n1 == n2:
                i = i + 1
                j = j + 1
        else:
            i = i + 1
            j = j + 1
        
        # The count must not be greater than one (One Typo)
        if count > 1:
            return False
    
    #Condition to compare Strings with differents lengths. 
    if count == 1 and n1 != n2 and (i != n1 or j != n2):
        return False
    
    return True

        
if __name__ == '__main__': 
    
    if (areThereOneTypo("pale", "ple")): 
        print("true") 
    else: 
        print("false")

    if (areThereOneTypo("pales", "pale")): 
        print("true") 
    else: 
        print("false")

    if (areThereOneTypo("pale", "bale")): 
        print("true") 
    else: 
        print("false")

    if (areThereOneTypo("pale", "bake")): 
        print("true") 
    else: 
        print("false")

"""
The algorithm complexity is O(n^2), because two strings are being compared. 
The space complexity of this algorithm depends of string length. 
"""