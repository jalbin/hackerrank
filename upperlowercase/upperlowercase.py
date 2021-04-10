
def swap_case(s):
    result ="" 
    for x in s:
        if (x.isupper()) == True: 
            result+=(x.lower()) 
        elif (x.islower()) == True: 
            result+=(x.upper()) 
        else: 
            result+= x 
            
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)