# 1) Write a program that: 
# 1. Finds the largest element in an 
# array. 
# 2. Finds the smallest element in 
# an array. 
# 3. Calculates the sum of all 
# elements in the array. 
# 4. Prints only the even numbers 
# from the array. 
# 5. Prints only the odd numbers 
# from the array. 
# 6. Counts the number of odd and 
# even numbers in the array. 
# 7. Calculates the sum of odd 
# numbers in the array. 
# 8. Calculates the sum of even 
# numbers in the array. 

size=int(input("Enter the size of the array: "))
while True:
  li=list(map(int,input(f"enter {size} elemenmts:").split()))
  if len(li)==size:
      break
  else:
      print(f"please enter exactly {size} elements")
print(size)
print("List:",li)


def num():
     largest=li[0]
     smallest=li[0]
     total=0
     even=[]
     odd=[]
     counteven=0
     countodd=0
     sumodd=0
     sumeven=0

     for i in li:
          if i>largest:
               largest=i
          if i<smallest:
               smallest=i
          total+=i
          if i%2==0:
               even.append(i)
               counteven+=1
               sumeven+=i
          else:
             odd.append(i)
             countodd+=1
             sumodd+=i
          
             
            
     

        
     return largest,smallest,total,even,odd,counteven,countodd,sumodd,sumeven
largest,smallest,total,even,odd,counteven,countodd,sumodd,sumeven=num()    
print("largest element : ",largest)
print("smallest element: ",smallest)
print("sum of all elements: ",total)
print("even number in the list",even)
print("Counts  of even number in list:",counteven)
print("sum of even numbers in the list:",sumeven)
print("odd number in the list",odd)
print("Counts  of odd number in list:",countodd)
print(" sum of odd numbers in the list:",sumodd)

# output:
# Enter the size of the array: 5
# enter 5 elemenmts:1 2 3 4 5
# 5
# List: [1, 2, 3, 4, 5]
# largest element :  5
# smallest element:  1
# sum of all elements:  15
# even number in the list [2, 4]
# Counts  of even number in list: 2
# sum of even numbers in the list: 6
# odd number in the list [1, 3, 5]
# Counts  of odd number in list: 3
#  sum of odd numbers in the list: 9


#      2) Write a program to generate the 
# following number pyramid for a given 
# integer n: 



n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

# output:

# Enter the number of rows: 5
# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3 
#    1 2 
#     1 