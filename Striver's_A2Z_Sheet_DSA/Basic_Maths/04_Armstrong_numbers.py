def Armstrong(n):
    sum = 0
    dup = n
    digits = len(str(n))
    while n > 0:
        last_digit = n % 10
        sum += last_digit**digits
        n //=10
    return dup==sum

def main():
    n = int(input("Enter the number: "))
    if Armstrong(n):
        print("Armstrong")
    else:
        print("Not Armstrong")

if __name__ == "__main__":
    main()
