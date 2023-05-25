how_many=int(input("how many numbers u want to input: "))
lst=[]
for i in range(how_many):
    lst.append(int(input("Your numbers please: ")))
print(lst)
result=list(map(lambda x: x**2,lst))
print(result)