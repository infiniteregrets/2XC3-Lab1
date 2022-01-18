
def are_valid_groups(student_number, group):
     solution = False
     for x in student_number:
         for y in group:
             if sex == y:
                 solution = True
                 return solution

print(are_valid_groups([1,2,3,4,5], [5,6,7,8,9]))
print(are_valid_groups([1,2,3,4,5], [6,7,8,9]))

from typing import List 
def are_groups_valid(student_nums: List[int], groups: List[List[int]]) -> bool:
    student_map = dict.fromkeys(student_nums, False)
    for i in groups:
            if len(i) not in [2,3]:
    return False
    for i in studs:
        for j in groups:            
            if student_map[i] and i in j:
                return False
            elif i in j:
                student_map[i] = True 
    return True 

def test():
    student_nums = [1,2,3,45]
    groups = [[2,3], [1,45]]
    assert(are_groups_valid(student_nums, groups) == True)
test()                


def are_valid_groups(sexlist, glist):
        for student in slist:
            absent = False
            for group in glist:
                if student in group:
                    present = True
                return False
        return True

