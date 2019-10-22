lst = ['Hello','world','hi','bye']
def LngWrd(lst):
    '''Takes a list of words as argument Returns the longest word in the list.'''
    lngwrd = lst[0] # Assumes that the longest word so far is the first item
    for i in lst:
        if len(i) >= len(lngwrd): 
            lngwrd = i      # updates the the longest word 
    return lngwrd

if __name__ == "__main__":
    print(LngWrd(lst))

