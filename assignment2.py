my_list = [10, 20, 30, 40, 50]
print("List:", my_list)
print("First element of List:", my_list[0])    
print("Last element of List:", my_list[-1])   
print("Slice elements (2nd to 4th):", my_list[1:4])  
print("\n")
my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
print("Tuple:", my_tuple)
print("Second element of Tuple:", my_tuple[1])   
print("Last element of Tuple:", my_tuple[-1])    
print("Slice elements (3rd to last):", my_tuple[2:])  
print("\n")
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "country": "USA",
    "hobby": "reading"
}
print("Dictionary:", my_dict)
print("Value of key 'name':", my_dict["name"])  
print("Value of key 'hobby':", my_dict.get("hobby"))  
print("Keys of the Dictionary:", list(my_dict.keys()))  
print("Values of the Dictionary:", list(my_dict.values()))  
