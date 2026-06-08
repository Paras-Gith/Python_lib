def fun(i,n):
    if i > n:
        return
    print("paras")
    fun(i+1, n)

def main():
    n = int(input("enter n: "))
    fun(1, n)
main()