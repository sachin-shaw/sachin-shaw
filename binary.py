def binary_search(item_list,item):
    item_list.sort()
    first=0 
    last=len(item_list)-1
    found=False
    while(first<=last and not found):
        mid=(first+last)//2
        if item_list[mid]==item:
            found=True
        else:
            if item<item_list[mid]:
                last=mid-1
            else:
                first=mid+1
        #return found
    if found: 
        return print(mid,item_list[mid])

print(binary_search([23,34,45,12,24,78],24))

