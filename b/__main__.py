#!/usr/bin/env python3


import os

print(os.getcwd())

import b as bb_main

def main():
    print('main function in module b.__main__')
    fun()

def fun():
    print('fun in module b.__main__')
    print('invoke b.b.fun')
    bb_main.fun()
    
var1 = 789
var2 = 'hij'
    
print('this is module b.__main__!')

if __name__ == '__main__':
    main()
