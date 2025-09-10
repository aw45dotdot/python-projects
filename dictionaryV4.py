#how ot merge 2 dictionaries

d1 = {"Person1":"ab",
      
      "Person2":"ab"}

d2 = {"Person3":"b+",
      
      "Person4":"a+"}

d3 = {}


for i in (d1,d2):  #i = item
    d3.update(i)
    
print(f'd1 is {d1}\n')
print(f'd2 is {d2}\n')
print(f'd3 is {d3}\n')
