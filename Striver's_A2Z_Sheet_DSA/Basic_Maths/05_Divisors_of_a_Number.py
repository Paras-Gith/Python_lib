def divisors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

def main():
    n = int(input("enter the number: "))
    divisors(n)
if __name__=="__main__":
    main()

