def number(n):
    count = 0
    while n > 0:
        last_digit = n % 10
        count += 1
        n //=10
    return count

def main():
    n = int(input("enter the number: "))
    result = number(n)
    print("Count: ", result)
if __name__=="__main__":
    main()