how_many=int(input("how many numbers u want to input: "))
lst=[]
for i in range(how_many):
    lst.append(int(input("Your numbers please: ")))
print(lst)
def triple(lst):
    return lst * 3
result=list(map(triple,lst))
print(result)
