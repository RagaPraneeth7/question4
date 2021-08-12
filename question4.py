for _ in range(int(input())):       #read nunber of test cases
    n = int(input())                # read input number
    activity = input().split()      # split the given input string

    ans = "YES"                     # store yes in ans
    if activity[-1] == "cookie":    # if last element of activity is cookie, ans equals to no
        ans = "NO"
    else:                           # else for every element in range 0 to n-1
        for i in range(n-1):        # if element of activity equals to cookie
            if activity[i] == "cookie":    
                if activity[i+1] != "milk":     # and activity next element is not equals to 1 
                    ans = "NO"      #store no in ans and break
                    break

    print(ans)                      # print ans
