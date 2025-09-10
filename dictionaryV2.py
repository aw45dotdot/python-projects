#creating a nested dictionary
classroom = {"Student1":{"name":"Muhammad",
                         "age":13,
                         "marks":[68,73,80,91,94]},
             
             
             "Student2":{"name":"Dan",
                         "age":14,
                         "marks":[60,70,80,90,100]},
             
             
             "Student3":{"name":"Daniel",
                         "age":15,
                         "marks":[55,65,75,85,95,]}}

print('\n',classroom,'\n')
print(f'STUDENT 1 AGE IS = {classroom["Student1"]["age"]}\n')
print(f'STUDENT 2 MARKS ARE {classroom["Student2"]["marks"]}\n')
