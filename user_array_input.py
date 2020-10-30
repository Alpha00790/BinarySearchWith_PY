def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i+1 
  
    return -1

arr = []

n = int(input("Enter the number of elements:"))

for i in range(0,n):
	element = int(input())
	arr.append(element)

key = int(input("Enter the key:"))

result = search(arr,key)

if result != -1:
    print(str(result))
else:
    print("not found! 404");