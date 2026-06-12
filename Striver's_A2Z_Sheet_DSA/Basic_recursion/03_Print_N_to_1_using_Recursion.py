def fun(i,n):
    if i < 1:
        return
    print(i)
    fun(i-1, n)

def main():
    n = int(input("enter n: "))
    fun(n, n)
main()