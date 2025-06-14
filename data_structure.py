# """ Mutable and Immutable 
# Mutable: 
# List, Dictionary, Set

# Immutable: 
# Tuple, String, Integer, Float, Boolean


# Mutable objects can be changed after they are created.
# Immutable objects cannot be changed after they are created.

# """

#list 
fruits = ["Apple", "banana", "mango", "banana", "grapes"]

print(fruits)
fruits.sort(key=str.lower)
print(fruits)
fruits.append("orange")
print(fruits)

fruits.reverse()
fruits.sort(reverse=True)
print(fruits)

#tuple
nums = (1, 'apple', 'apple')

print(type(nums))
count = nums.count('apple')
print(count)

index = nums.index(1)
print(index)
# print(nums)

# print(type(nums[0]))

# print(type(nums[1]))

# to add a new element to the tuple
nums = nums + (2, 3, 4)
print(nums)

# to remove an element from the tuple
nums = nums[:-2]
print(nums)

(one, *two, three) = nums
print(one)
print(two)
print(three)



#array
# import array
# a = array.array('i', [1, 2, 3, 4, 5])
# string = array.array('u', ['a', 'b', 'c', 'd', 'e'])
# print(a)
# print(string)


# ---------------------------------------------------------------------------------------------------------
# dictionaries & set

# dictionaries
# pattern 1
band = {
    "vocals": "plant",
    "guitar" : "page"
}

#pattern 2 
band_2 = dict(vocals = "plant" , guitar = "page")

print(band)
print(band_2)

#word count 
text = "This is a sentence. This is another sentence. This is a third sentence."
words = text.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print (count)

#Methods in Dictionaries
#1. get() -> safe way to access a key
person = {
    'name' : 'Anoj',
    'age' : 21
}

print(person.get('name'))

print(person.get('name', 0)) #with default value

#2. update() -> merge dictionaries
person.update({
    'age' : 22
})
print(person)

new_info = {
    'name' : "paru",
    'age': 21
    }

person.update(new_info) # Update existing keys, adds new keys
print(person)

#3. pop() -> remove a key and get its value
print(person.pop('age')) # it remove the key and return the value

ages = person.pop('age', 0)
print("Your age" , ages)

#4. popitem() -> remove last item
print(person.popitem()) # it remove the key and return the value


#keys(), values(), items() -> return iterators
person_1 = {
    'name' : 'Rawal',
    'Qualification' : 'B.Tech'
}
print(list(person_1.keys()))
print(list(person_1.values()))
print(list(person_1.items()))


#6. setdefault() -> get a value or set a default value
#7. fromkeys() -> create a dictionary from a sequence of keys
#8. clear() -> remove all items
#9. copy() -> return a shallow copy of the dictionary

#Example ->
grade = {}
grade.setdefault('math', []).append(90) # auto create empty list
grade.setdefault('science', []).append(85)

grade.setdefault('math', []).append(95)
grade.setdefault('science', []).append(92)

for subject, score in grade.items(): # subject and score are the key and value automatically unpacked by the for loop key and value
    avg = sum(score) / len(score)
    print(f"Average score for {subject}: {avg}")

#nested dictionaries
mender1 ={
    'name' : 'Anoj',
    'age' : 21,
}

member2 = {
    'name' : 'Paru',
    'age' : 20,
}

nested_dict = {
    'member1' : mender1,
    'member2' : member2
}

print(nested_dict)





#----------------------------------Set--------------------------------
#Unordered collection of unique items, Mutable

#syntax :-> set_name = {item1, item2, item3}
# empty_set = set()  # Correct empty set
#it helps to remove duplicates

nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5}

print(nums)
