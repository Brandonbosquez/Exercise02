print("Compare 5 numbers")
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
num3 = input("Enter a number: ")
num4 = input("Enter a number: ")
num5 = input("Enter a number: ")

nums = [num1,num2,num3,num4,num5]
nums.sort()
print(nums)
i = 0
i2 = 1
sum = nums[i] + nums[i2]
while i2 < 5 :
    if sum < nums[4] :

        if i2 > 4 :
            break
        print(f"The sum of {nums[i]} and {nums[i2]} is less than {nums[4]}")
        i2 += 1
        sum = nums[i] + nums[i2]