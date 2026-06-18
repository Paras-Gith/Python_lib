def number(i, sum):
    if(i<1):
        print(sum)
        return
    number(i-1, sum+i)
    
def main():
    n = int(input("enter the number: "))
    number(n, 0)
if __name__=="__main__":
    main()