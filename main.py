## Calculator
# num_1 = float(input("What is your first number? "))
# operator = input("What is your operation? -, +, /, *, **: ")
# num_2 = float(input("What is your second number? "))
# if operator == '-':
#   result = num_1 - num_2

# elif operator == '+':
#   result = num_1 + num_2

# elif operator == '/':
#   result = num_1 / num_2

# elif operator == '*':
#   result = num_1 * num_2

# elif operator == '**':
#   result = num_1 ** num_2

# print(result)

##Print range backwards
# for i in range(10, 0, -2):
#     print(f"{i}")

##EXERCISE 6
# 1.Write a program to demonstrate to get index and value of the element from the list .
# 2.Using iterations in the list,Print Happy New year message to all the members in the list Friends:
# Friends=[“john’,Frank”,”gitty”,”oliver”]
# Add Sam and garry also to your list after john and before Frank.
# 3..Write a program to calculate the average of items in the list.
# Hint:Use len() and sum() functions.
# 4.From the following list of numbers, write a script to remove the duplicates from the list.
# b = [5,6,4,7,2,9,10,5,6,7,101,11,51,9]
print("Question 1: ")
friends = ["john", "frank", "gitty", "oliver"]
for i in friends:
  print("Happy New Year", i)

print("Question 2:")
friends.insert(1, "Sam")
friends.insert(2, "garry")
print(friends)

print("Question 3:")
sum = 0
b = [5,6,4,7,2,9,10,5,6,7,101,11,51,9]
for i in b:
  sum = sum + i
length = len(b)
print(sum / length)
print("Question 4")
no_duplicates = list(dict.fromkeys(b))
print(no_duplicates)