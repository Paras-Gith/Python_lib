def Palindrome(n):
    reversed = 0
    dup = n
    while n > 0:
        last_digit = n % 10
        n //=10
        reversed = reversed * 10 + last_digit
    if dup == reversed:
        return True
    else: 
        return False

def main():
    n = int(input("Enter the number: "))
    if Palindrome(n):
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()