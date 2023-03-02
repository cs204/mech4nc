def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s
def main():
    s = input()
    a = convert(s)
    print(a)
main()