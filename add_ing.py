string=input("Enter a string:")
if len(string)<3:
    print(string)
elif string[-3:]=='ing':
    string += 'ly'
else:
    string+='ing'
print(string)
    
