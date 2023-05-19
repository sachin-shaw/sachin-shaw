my_dict={'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
keys=list(my_dict.keys())
values=list(my_dict.values())
sorted_values=sorted(values, reverse=True)
top_3_values=sorted_values[:3]
top_3_keys=[]
for key, values in my_dict.items():
    if values in top_3_values:
        top_3_keys.append(key)
print("top_3_keys:",top_3_keys)
print("top_3_values:",top_3_values)