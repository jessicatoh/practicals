def get_rows(n):
    if n == 1:
        return 1
    else:
        return n + get_rows(n-1)
def main():
    input_rows = int(input("Input rows:"))
    num = get_rows(input_rows)
    print("You need {} blocks. ".format(get_rows(num)))
main()