def recursive_linear_search(arr, target,index=0):

    if index == len(arr):

        return -1


    if arr[index] == target:

        return index

 
    return recursive_linear_search(arr, target,index+1)
 
 
emp_ids = [10, 20, 30, 40, 50]
 
print(recursive_linear_search(emp_ids, 40))  

print(recursive_linear_search(emp_ids, 70)) 
