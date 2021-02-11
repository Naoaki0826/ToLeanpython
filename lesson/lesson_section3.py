#!/usr/bin/python3
import math
import sys

#print(sys.version)
#print(sys.path)

num = 1
name = 'Mike'
name_2 = '1'
is_ok = True

new_num = int(name_2)


print('HI', 'Mike', sep=' ', end='.\n') #\: option + ¥

print(num,type(num))
print(name,type(name))
print(is_ok,type(is_ok))

print(new_num,type(new_num))



print('#-------------------------------------------------------------------------#')


result = math.sqrt(25)
print(result)

y = math.log2(10)

print(y)

print('Hello')
print('I don\'t know')
print('say "I don\'t know" ')

print('Hello. \nhow are you?')

print(r'C:\name\name') #path の時は先頭にrをつけると改行されない

print("###############################################################################")

## \を入れると空白が消える
print("""\
Line1
Line2
Line3\
""")

print("###############################################################################")

print('Hi.'* 3 + 'Mike.')
print('Py' + 'thon')


print('#-------------------------------------------------------------------------#')
#文字列のインデックスとスライス

world = 'python'
print(world[0])
print(world[1])
print(world[-1])

print(world[0:2])
print(world[2:5])
print(world[:2])
print(world[2:])

# print(world[100]) error

#文字列のインデックスの代入
#world = 'j' #できない
world = 'j' + world[1:]
print(world)
print(world[:])

n = len(world)
print(n)

print('#-------------------------------------------------------------------------#')
#文字のメソッド
s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')
print(is_start)

print(s.find('Mike'))  #前かえら検索
print(s.rfind('Mike')) #後ろから検索

print(s.count('Mike'))
print(s.capitalize())
print(s.title())

print(s.upper())
print(s.lower())

print(s.replace('Mike', 'Nancy'))

print('#-------------------------------------------------------------------------#')
#文字列の代入
print('a is {}'. format('a') )
print('a is {}'. format('test') )
print('a is {} {} {}'. format(1,2,3) )
print('a is {0} {1} {2}'. format(1,2,3) )
print('a is {1} {0} {2}'. format(1,2,3) )
print('#                                                                         #')


print('My name is {0} {1}'. format('Naoaki','Udagawa'))
print('My name is {0} {1}.Watashi ha {1} {0}'. format('Naoaki','Udagawa'))

print('My name is {name} {family}.Watashi ha {family} {name}'. format(name = 'Naoaki',family = 'Udagawa'))

print('#-------------------------------------------------------------------------#')
#f-strigs

a = 'a'
print(f'a is {a}')

x,y,z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {x}, {y}, {z}')

name = 'Naoaki'
family = 'Udagawa'

print(f'My Name is {name} {family}. Watashi ha {family} {name}')






