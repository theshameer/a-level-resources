"""
 create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
"""

def filter_list(l):
    arr = []
    for i in l:
        if isinstance(i,int) ==True:
            arr.append(i)
            
    return arr
    
