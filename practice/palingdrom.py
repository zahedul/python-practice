def infinite_sequence():
    num =0
    while True:
        yield num
        num += 1

#for i in infinite_sequence():
#    print(i, end=' ')

def is_palindrome(num):
    # Skip single-digit inputs
    
    if num // 10 == 0:
        return False
    
    temp = num
    reverse_num = 0
    
    while temp != 0:
        reverse_num = (reverse_num * 10) + (temp % 10)
        temp = temp // 10
        
    if num == reverse_num:
        return num
    else:
        return False