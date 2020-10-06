def smart_divide(func):
    def inner(a, b):
        print(f'I aam going to divide {a} and {b}')
        
        if b == 0:
            print('Whoo[ss! cannot divide')
            return
        
        return func(a, b)
    
    return inner


@smart_divide
def divide(a, b):
    
    return a/b

