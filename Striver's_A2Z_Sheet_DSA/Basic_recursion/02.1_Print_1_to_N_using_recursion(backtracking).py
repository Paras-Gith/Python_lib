def fun(i,n):
    if i < 1:
        return
    fun(i-1, n)
    print(i)


def main():
    n = int(input("enter n: "))
    fun(n, n)
main()