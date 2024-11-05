def move_zeros(numbers):

    new_array = []                          #define new array where we will append the values of the array that are not zero
    
    for numb in numbers:
        if numb != 0:
            new_array.append(numb)          #if the number is not equal to zero, append it to the new array
        
    zero_count = numbers.count(0)           #count the number of zeros in the original array
    return new_array + [0]*zero_count       #return the array and concatinate to it the number of zeros that were counted

numbers = [1, 2, 0, 5, 0, 11, 3, 0, 56]
print(move_zeros(numbers))

