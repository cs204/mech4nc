def main():
    r = feet2meter(input("Сколько футов:"))
    print(f"Это будет {r:.2f} метров.")

def feet2meter(r):
    return(float(r.strip('ft')))*0.3048
main()