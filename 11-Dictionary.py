#  Elements in a dictionary are unordered
#  Dictionary's keys are immutable and hence not changeable
#  Dictionary's values are mmutable and hence are changeable
#  it does not allow multiple elements with same key (no duplicate keys).

info = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

print(f"{info} and type of {type(info)}")
print(info["key1"])

info["key1"] = "value10"
print(info["key1"])
print(info)

for x in info : 
    print(x)
    print(f"keys are : {x} and values are : {info[x]}")

for x in info.values():
    print(x)

info["key4"] ="value4"
print("adding key and value into info ", info)

# pop() - deletes specified key and it's value of the dictionary.
# popitem() - deletes last key-value pair of the dictionary. Please note that dictionary is an unordered data container, hence last key-value pair is not defined.
# clear() - deletes all key-value pairs of the dictionary.
# del - deletes a key-value pair of a dictionary. can be used to delete the dictionary itself.

Info = {
   "name": "John",
   "age": 25,
   "city": "London"
}
Info.pop("city")
print(Info)

Info = {
   "name": "John",
   "age": 25,
   "city": "London"
}
Info.popitem()
print(Info)

Info = {
   "name": "John",
   "age": 25,
   "city": "London"
}
Info.clear()
print(Info)

Info = {
   "name": "John",
   "age": 25,
   "city": "London"
}
del Info["city"]
print(Info)
del Info
# print(Info)

# = operator: Using dict2 = dict1, a reference of dict1 can be created into dict2. Any change to dict1 will be reflected in dict2 also.
# copy(): This will create an independent copy of a dictionary.

Info = {
   "name": "John",
   "age": 25,
   "city": "London"
}
Info_1 = Info
Info_2 = Info.copy()

# Info_1 dictionary is a reference of Info
print(Info_1) 
# Info_2 dictionary is a copy of Info   
print(Info_2,"\n")     

#deletes city key from the dictionary
Info.pop("city")  

# displaying result after operation
print(Info_1)   
print(Info_2)


# characters = input("enter the string").strip()
# frequency = {}

# for char in characters:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# max_frequency = 0 

# for char, freq in frequency.items():
#     if freq > max_frequency:
#         max_frequency = freq
#         max_char = char
# print(max_frequency, max_char)

string = input("ENTER THE STRING TO COUNT THE FREQUENCY OF EACH CHARACTER : ").strip()

stringFrequency = {}

for char in string : 
    if char in stringFrequency :
        stringFrequency[char] += 1
    else :
        stringFrequency[char] = 1

for char ,frequency in stringFrequency.items():
    print(f"The character '{char}' appears {frequency} times.")