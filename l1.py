# Question 1: Find the Missing Number 
# Write a program that finds the missing number in a list containing distinct integers from 1 to 
# N, where exactly one number is missing. 

input = [1, 2, 4, 5, 6] 

n=len(input)+1

expected=n*(n+1)//2
actual=sum(input)

missing=expected-actual
print(missing)

# output=3

num=[2, 3, 4, 5] 
l=len(num)+1

nog=l*(l+1)//2
og=sum(num)

m=nog-og
print(m)

# output=1


# Question 2: Find the Most Frequent Element 
# Write a program that finds the element that appears most frequently in a list of integers. 

numbers = [2, 3, 2, 5, 2, 3]

most_frequent = max(numbers, key=numbers.count)

print(most_frequent)


numbers = [4, 4, 7, 7, 9]

max_count = max(numbers.count(num) for num in numbers)

result = []

for num in numbers:
    if numbers.count(num) == max_count and num not in result:
      result.append(num)
      print(result)
