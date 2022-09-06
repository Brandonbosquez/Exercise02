#For Loops practice/Integer
number = int(input("Enter an integer: "))
list = []
var = 1
factor = 1

if number <= 0 :
    print("thanks and bye!")
else :
    for x in range(1, number + 1 ):
        list.append(var)
        factor = var * factor
        var = var + 1
print(list)
print(factor)
