#!/usr/bin/python3

print('#-------------------------------------------------------------------------#')
print('#                               コメント                                   #')

print('XXXXX')
"""
test
test
test
test
"""
print('XXXXX')

print('#-------------------------------------------------------------------------#')
print('#                           一行が長くなる時                                #')


s = 'aaaaaaaaaaaaa' + 'bbbbbbbbbbbbbbb'

print(s)

s = 'aaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbbbbb'


X = 1 + 1 + 1 + + 1 + 1 + 1 + 1 \
    + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
print(X)

print('#-------------------------------------------------------------------------#')
print('#                              if文                                       #')

x = 10
if x < 0:
    print('Negative')
elif x == 0:
    print('zero')
else:
    print('Positive')


