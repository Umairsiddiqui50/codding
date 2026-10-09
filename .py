git add .
git commit -m "Describe your changes"
git push# a = int(input ("enter low disite := "))
# b = int(input ("enter hightist disit := "))

# total = 0 

# for i in range(a , b + 1 ):
#     total += i
# print(total)



    
# d = 5 

# total = 0 

# for i in range (1, 500):
#     if i % 10 == d:

#         total += i 
# print(total)



    
# arr =  [1,2,3,4,5]
# arr.reverse()
# print(arr) 


# N = 6 
# for i in range (1 , N+1):
#     for k in range(1 , i+1):
#         print( k , end="")
#     print()



# num = [3, 3, 6, 1 , 8] 
# print (max(num))


# num = [3, 3, 6, 1 , 8] 
# larg = num[0]
# for i in num :
#     if i > larg :
#         larg = i 
# print (larg)          



# nums =[ 4, 5, 6, 8, 9 , 10]
# # nums = list(nums)
# nums.sort()
# print(nums[-2])


# nums =[ 4, 5, 6, 8, 9 , 10]
# largest = nums[0]
# secd_larg = -1

# for i in nums :
#     if i > largest :
#         secd_larg = largest 
#         largest = i 
#     elif  i < largest and i > secd_larg :
#         secd_larg = i 
# print(secd_larg)




# nums = [1, 2, 3, 4, 5]

# sorted = True 

# for i in range(1 ,len(nums) ):
#     if nums[i] < nums [i - 1 ]:
#         sorted = False 
#         break
# print (sorted)





# nums = [-30, -30, 0, 0, 10, 20, 30, 30]
# nums = (list(set(nums)))
# print(len(nums))


# nums = [-30, -30, 0, 0, 10, 20, 30, 30]
# a = []
# for i in nums:
#     if i not in a :
#         a.append(i)
# print(a)
# print(len(a))














# num = [1, 2, 3, 4, 5]
# a = []
# for i in num :
#     if i 

# def rotateLeftByK(nums, k):
#     # Agar array khali hai toh kuch mat karo
#     if len(nums) == 0:
#         return
        
#     n = len(nums)
#     # Agar k ki value array ki length se badi ho (jaise array 5 ka hai aur k 7 hai), 
#     # toh usko limit mein laane ke liye remainder (modulo) nikalte hain.
#     k = k % n 
    
#     # Array ko do hisson mein kaat kar wapas jod do
#     nums[:] = nums[k:] + nums[:k]

# # Test karke dekhte hain
# my_array = [-30, -30, 0, 0, 10, 20, 30, 30]
# rotateLeftByK(my_array, 3) # 3 baar ghumaya
# print(my_array)




# def rotateLeft(nums):
#     first = nums.pop(0)  # 1. Aage wale ko bahar nikala
#     nums.append(first)   # 2. Piche chipka diya

# # Test:
# nums = [1, 2, 3, 4, 5]
# rotateLeft(nums)
# print(nums)  # [2, 3, 4, 5, 1]




# def change (aree , a):
#     a = a %len(aree)
#     aree[:] =aree[a:] + aree[:a]

# aree = [1,2,3,4,5]
# change (aree , 3) 
# print(aree)


# a = [1,2,3,4,5]
# b = []
# for i in range(4):
#     x = a.pop(0)
#     b.insert(0,x)
# b = a+b
# print(b)
    












# nums = [0, 0, 1,-2 , -1, -3, 4, 5 , 2 ,]
# a = []



# for i in nums:
#     if i < 0 :
#         a.insert(0,i)
#     elif i == 0 : 
#         a.append(i)
#     else :
#         a.append(0,i)
# print(a)








# a =  [ 1,2,3,3,4,654,63,2432,463]

# b = a[0]

# for i in a:
#     if i > b  :
#         b = i 
# print (b)


# n = 5832
# sum = 0


# for i in str(n):
#     sum = sum + int(i)
# print(sum)  


# a =  [ 1,2,3,3,4,654,63,2432,463]
# print(len(a))


# n =["1","2","3","4",'5']
# n.reverse() 
# print(n)






# a = [1,2,23,3,45,6,4,4,5,22,22,32,21] 

# b = [] 

# for i in a :
#     if i not in b :
#         b.append(i)
# print(b)



# a = [1,2,23,3,45,6,4,4,5,22,22,32,21] 
# b =[ ]
# for i in a :

#     if  i not in b :

#         print(i ,  "->" , a.count(i))

#         b.append(i)






a = [2, 5, 2, 8, 5, 2, 9, 8, 8, 1]
b = []

for i in a:
    if i not in b:
        count = 0

        for j in a:
            if i == j:
                count += 1

        print(i, "→", count)
        b.append(i)