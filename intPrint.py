#!/usr/bin/env python3

def int_maker(int_list: list) -> int:
    output = 0
    for i in range(len(int_list)):
        output += int_list[-i] * 10 ** i
    return output

if __name__ == '__main__':
    print(int_maker([8,3,5,1]))
