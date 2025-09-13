dict1 = {"Employee1":{"name":"Muhammad",
                      "Job":"lawyer",
                      "Pay":700},
         
         "Employee2":{"Name":"Dan",
                      "Job":"therapist",
                      "Pay":650}}

dict2 = {"Employee3":{"name":"daniel",
                      "job":"psyciatrist",
                      "Pay":675}}

dict3 = {}

for i in(dict1,dict2):
    dict3.update(i)
    
print(dict3)
