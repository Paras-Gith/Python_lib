def fun(i,n):
    if i > n:
        return
    fun(i+1, n)
    print(i)

def main():
    n= int(input("enter n: "))
    fun(1, n)
if __name__=="__main__":
    main()