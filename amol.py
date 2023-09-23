num=int(input("please input the number :"))
index=0
for index in range(0, num , 10):
    if (index % 10 == 0):
        print(index)
#     Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned. These are the steps we need to complete this:

# Define the function to accept one input parameter called nums
# Initialize a counter to 0
# Loop through every number in nums
# Within the loop, if any of the numbers are divisible by 10, increment our counter
# Return the final counter value  