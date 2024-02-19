#!/usr/bin/env python3

def triple(x):
    return x * 3

def square(x):
    return x ** 2

def main():
    for i in range(1, 11):
        s_triple = triple(i)
        s_square = square(i)
        if s_square > s_triple:
            break
        else:
            print(f"triple({i})=={s_triple} square({i})=={s_square}")

if __name__ == "__main__":
    main()
