# a = int(input ("enter low disite := "))
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



def rotateLeft(nums, k):
    k = k % len(nums)   # agar k list se bada ho to bhi sahi kaam kare
    nums[:] = nums[k:] + nums[:k]

# Test:
nums = [1, 2, 3, 4, 5]
rotateLeft(nums, 9)
print(nums)  # [3, 4, 5, 1, 2]