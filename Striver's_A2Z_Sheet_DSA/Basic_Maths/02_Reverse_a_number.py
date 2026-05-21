def reverseNumber(n):
    reversed = 0
    while n > 0:
        last_digit = n % 10
        n //=10
        reversed = reversed * 10 + last_digit
    return reversed

def main():
    n = int(input("enter the number: "))
    result = reverseNumber(n)
    print("reversed: ", result)
if __name__=="__main__":
    main()