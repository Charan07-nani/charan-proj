import math,random

while True:
    try:
        print("Type a number to perform a task")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Find the square root of a number")
        print("6. Print first n numbers in fibanocci series")
        print("7. Find nth element in the fibanocci series")
        print("8. Find the factorial of a number")
        print("9. Find the square of a number")
        print("10. Find the cube of a number")
        print("11. Find the sum of first n natural numbers")
        print("12. Find the sum of squares of first n natural numbers")
        print("13. Check if the number is prime or not")
        print("14. Print prime numbers from 1 to N")
        print("15. Listen to a joke")
        print("999. To exit\n")

        x = int(input())
        match x:
            case 1:
                print("Enter two numbers to add")
                a,b=map(int,input().split())
                print(f"Addition of {a},{b} is {a+b}\n")
            case 2:
                print("Enter two numbers to subtract")
                a,b=map(int,input().split())
                print(f"Subtration of {a},{b} is {a-b}\n")
            case 3:
                print("Enter two numbers to multiply")
                a,b=map(int,input().split())
                print(f"Multiplication of {a},{b} is {a*b}\n")
            case 4:
                print("Enter two numbers to divide")
                a,b=map(int,input().split())
                if b==0:
                    print("Can't divide by zero\n")
                else:
                    print(f"Division of {a},{b} is {a/b}\n")
            case 5:
                print("Enter a number to find its square root")
                a = int(input())
                if a<0:
                    print("Please enter a positive number\n")
                else:
                    print(f"Square root of {a} is {math.sqrt(a)}\n")
            case 6:
                print("Enter a number to print first n fibanocci numbers")
                n= int(input())
                print(f"First {n} fibanocci numbers are:")
                a=0
                b=1
                print(a,b,end=" ")
                for i in range(n-2):
                    c=a+b
                    print(c,end=" ")
                    a=b
                    b=c
                print("\n")                
            case 7:
                def fib_n(n):
                    if n <= 2:
                        return n - 1
                    else:
                        return fib_n(n - 1) + fib_n(n - 2)
                print("Enter a number to print nth fibanocci number")
                n=int(input())
                print(f"{n}th number in fibanocci series is {fib_n(n)}\n")
            case 8:
                def fact(x):
                    if x == 1:
                        return 1
                    else:
                        return (x * fact(x-1))
                print("Enter a number to print its factorial")
                n=int(input())
                print(f"Factorial of {n} is {fact(n)}\n")
            case 9:
                print("Enter a number to print its square")
                n=int(input())
                print(f"Square of {n} is {n**2}")
            case 10:
                print("Enter a number to print its cube")
                n=int(input())
                print(f"Cube of {n} is {n**3}")
            case 11:
                print("Enter n")
                n= int(input())
                print(f"Sum of first {n} numbers is {(n*(n+1))//2}\n")
            case 12:
                print("Enter n")
                n= int(input())
                print(f"Sum of squares of first {n} numbers is {(n*(n+1)*(2*n+1))//6}\n")
            case 13:
                
                def checkprime(n):
                    prime_flag = 0
                    
                    if(n > 1):
                        for i in range(2, int(math.sqrt(n)) + 1):
                            if (n % i == 0):
                                prime_flag = 1
                                break
                        if (prime_flag == 0):
                            return True
                        else:
                            return False
                    else:
                        return False
                print("Enter a number to check if it is prime or not")
                n=int(input())
                if checkprime(n):
                    print(f"{n} is a prime number\n")
                else:
                    print(f"{n} is not a prime number\n")
            case 14:
                def checkprime(n):
                    prime_flag = 0
                    
                    if(n > 1):
                        for i in range(2, int(math.sqrt(n)) + 1):
                            if (n % i == 0):
                                prime_flag = 1
                                break
                        if (prime_flag == 0):
                            return True
                        else:
                            return False
                    else:
                        return False
                print("Enter n")
                n=int(input())
                print(f"Prime numbers between 1 and {n} are:")
                for i in range(1,n+1):
                    if(checkprime(i)):
                        print(i,end=" ")
                print("\n")
            case 15:
                jokes=["I was wondering why the frisbee kept getting bigger and bigger, but then it hit me."," Most people are shocked when they find out how bad I am as an electrician.","The problem isn’t that obesity runs in your family. It’s that no one runs in your family.","Today a man knocked on my door and asked for a small donation toward the local swimming pool. I gave him a glass of water."]
                print(random.choice(jokes)+"\n")
            case 999:
                break
    except KeyboardInterrupt:
        break
    except:
        print("There's some error try again\n")
        


