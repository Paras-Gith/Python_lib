def pattern3(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

def main():
    n = int(input("enter the value: "))
    pattern3(n)
if __name__=="__main__":
    main()