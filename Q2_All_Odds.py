lst = [1,2,3,4,5,7]
def AllOdds(lst):
    '''Takes a list of integers as argutment Returns a list
    off all the odd numbers present'''
    lst_copy = lst[:]  # Clone the list
    for i in lst_copy:
        if i%2 == 0:
            lst_copy.remove(i) # removes all even integers
    return lst_copy

if __name__ == "__main__":
    print(AllOdds(lst))
