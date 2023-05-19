my_list=[(1,2,3),(4,5,6),(7,8,9)]
for i in range(len(my_list)):
    my_list[i]=my_list[i][0],my_list[i][1],0
print(my_list)