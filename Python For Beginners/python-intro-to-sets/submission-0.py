from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    return set(nums)
    list1=[1,2,3,4,5]
    list2=[1,1,2,2,3,3]
    list3=[1,2,3,4,5,5,5,3,4,5]
    

# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
