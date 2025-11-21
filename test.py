try:
#input x, n
    x=int(input("Input the value of x:"))
    n=int(input("Input the value of n:"))
#declare S, i
    S=0
    i=1
#while loop
    while i<=n:
    #computer operation
        S = S + (x**i)
    #increase couter variable 
        i=i+1
    print("The result of the power summation calculation S:")
    print(S)
except ValueError:
    print("Invalid value")