'''Start
Input the dictionary (let's call it my_dict)
Input the list of queries (let's call it query_list)
For each element key in query_list, do the following:
If key is in my_dict, then:
Print my_dict[key]
Else:
Print "None"
End'''


my_dict = {'a': 2, 'b': 3, 'c': 4}
query_list = ['a', 'd', 'b', 'z']

for key in query_list:
    if key in my_dict:
        print(my_dict[key])
    else:
        print("None")
