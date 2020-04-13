""""Supermarket"""
dict1={}
l=0
list2=[]
while(1):
    str1=input("Enter the item with cost:")
    if(str1=="end"):
        break
    list1=str1.split()
    value=int(list1[-1])
    key=" ".join(list1[:-1])
    list2.append(key)
    l=list2.count(key)
    if l>1:
        value=value*l
        dict1[key]=value
    else:
        dict1[key]=value
    
print(dict1)
