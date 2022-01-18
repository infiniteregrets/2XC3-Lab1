def are_valid_groups(student_number, group):
     solution = False
     for x in student_number:
         for y in group:
             if x == y:
                 solution = True
                 return solution

print(are_valid_groups([1,2,3,4,5], [5,6,7,8,9]))
print(are_valid_groups([1,2,3,4,5], [6,7,8,9]))