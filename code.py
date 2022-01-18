from typing import List 


def are_valid_groups(slist, glist):
        attendance = [False] * slist.length

        for sindex in range (0, slist.length - 1):
            present = False
            for group in glist:
                if group.size != 2 and group.size != 3:
                    return False
                    
                if slist[sindex] in group:
                    if attendance[sindex] == False:
                        attendance[sindex] = True
                    else:
                        return False
                    
        return True





def are_groups_valid(student_numms: List[int], groups: List[List[int]]) -> bool:
    student_map = dict.fromkeys(student_nums, False)
    for i in groups:
        if len(i) not in [2,3]:
                    return False
    for i in student_nums:
        for j in groups:            
            if student_map[i] and i in j:
                return False
            elif i in j:
                student_map[i] = True 
    return True 


def are_valid_groups(slist, glist):
        for studennt in slist:
            present = False
            for group in glist:
                    if studennt in group:
                        present = True
                    if present == False:
                        return False
        return True

