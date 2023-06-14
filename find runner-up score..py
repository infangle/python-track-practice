if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner = -100
    for num in arr: 
        if runner < num:
            runner = num
        elif num < runner or num == runner :
            runner = num
            
    print(runner)
    
