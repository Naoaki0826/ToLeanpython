#!/usr/bin/python3
# セクション4 データ構造

print('#-------------------------------------------------------------------------#')
# リスト型

l = [1, 20, 30, 40, 50, 1, 3]

print(l)
print(l[2])
print(l[:3])

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 一つ飛ばしで表示
print(n[::2])

# 後ろから表示
print(n[::-1])

# ネストさせる　→リストの中にリストを作る
a = ['a', 'b', 'c']
m = [1, 2, 3]
x = [a, n]

print(x)
print(x[0])
print(x[1])

# 要素を取り出す　'b' & '3'
print(x[0][1])
print(x[1][2])

print('#                                                                         #')
print('#-------------------------------------------------------------------------#')
# リストの操作

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
print(s[0])
# 配列の書き換え、文字列はダメだったが、配列だと以下の書き換えができる
s[0] = 'X'
print(s)

# 連続書き換え
s[2:4] = ['C', 'D', 'E']
print(s)
# 空にしたいとき
s[2:5] = []
print(s)
s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 最後に結合させる
n.append(100)
print(n)

# 最初に結合させる
n.insert(0, 200)
print(n)

# １００を取り出す
n.pop()
print(n)

# 先頭を取り出す時はインデックスを指定する
n.pop(0)
print(n)

# 消したい時
del n[0]
print(n)


# del n  <----nが消える
# print(n) #<---エラー

n = [1, 2, 2, 2, 3]
# 2を消す
n.remove(2)
print(n)

# リストの結合
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]


X = a + b
print(X)

# 付け足したい場合
a += b
print(a)

a.extend(b)
print(a)


print('#                                                                         #')
print('#-------------------------------------------------------------------------#')
# リストのメソッド

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))  # 3番目のインデックスから検索

print(r.count(3))
# rの中に５がある場合表示させる
if 5 in r:
    print('exist')

if 100 in r:
    print('exist')

# ソートさせる
r.sort()
print(r)

# 逆にそーとする
r.sort(reverse=True)
print(r)

# 逆になったので元に戻す
r.reverse()
print(r)

# スプリット
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

# joinはリストを受け付ける
x = ' '.join(to_split)
print(x)

x = ' ### '.join(to_split)
print(x)
# helpでlistのメソッドを表示
# print(help(list))


print('#                                                                         #')
print('#-------------------------------------------------------------------------#')
# リストのコピー

i = [1, 2, 3, 4, 5]
j = i #これはアドレスをJに入れてくださいという意味になる。値渡しと参照渡しが起きている

#この書き方だとiの方にも100が入ってしまう。
j[0] = 100
print('j =', j)
print('i =', i)

#避け方
x = [1, 2, 3, 4, 5]
y = x.copy()  #このcopyメソッドを呼び出してから、yに入れる必要がある
#これでもいける
#y = x[:] 見落とししやす
y[0] = 100

print('x =', x)
print('y =', y)

X = 20
Y = X
Y = 5

print(id(X))
print(id(Y))

print(X)
print(Y)

X = ['a', 'b']
Y = X

Y[0] = 'p'
print(id(X))
print(id(Y))

print(X)
print(Y)

print('#                                                                         #')
print('#-------------------------------------------------------------------------#')
# リストの使い方
seat = []
min = 0
max = 5

print(min <= len(seat) < max)
seat.append('p')  #１人追加
print(min <= len(seat) < max)
seat.append('p')
print(len(seat))

seat.append('p')
seat.append('p')

print(min <= len(seat) < max)
print(len(seat))

print(min <= len(seat) < max)
seat.append('p')
print(len(seat))

print(min <= len(seat) < max)

seat.pop(0) #１人降りた
print(min <= len(seat) < max)


print('#                                                                         #')
print('#-------------------------------------------------------------------------#')
# タプルの使い方:値を入れたら、読み込むケースに使用する
t = (1,2,3,4,1,2)
print(t)
print(type(t)) #値を代入することをサポートしていない　ex) t[0] = 100
#他のとことは出来る
print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1,1))

print(t.count(1))

#タプルにリストを入れる
t = ([1,2,3],[4,5,6])
print(t)

#タプルの０番目と１番目は変更できないがタプルないのリストは変更可能
t[0][0] = 100 #タプル０番目のリスト野中の０番目　-->1
print(t)

#パレンティス（）がなくてもタプルは宣言できる
t = 1,2,3,4,5,6,7,8,9
print(t)
print(type(t))

#タプルの場合値が一つだけでもカンマがあればタプルになる
t = 1,
print(t)
print(type(t))

#空のタプル
t = ()
print(t)
print(type(t))

#()の中に１だけ入れた場合, イント型になる
t = (1)
print(t)
print(type(t))

#新しいタプルの場合は、繋げることができる
new_tuple = (1,2,3) + (4,5,6)
print(new_tuple)

new_tuple = (1,) + (4,5,6)
print(new_tuple)

print('#                                                                         #')
print('#-------------------------------------------------------------------------#')
# タプルのアンパッキング

num_tuple = (10, 20)
print(num_tuple)
x, y = num_tuple # --> x, y = (10, 20) :同じ意味
#tupleではパレンティスの鉤括弧はいらないので、以下のようにかける
#x, y = 10, 20
print('x = ', x)
print('y = ', y)

min, max = 0, 100
print(min, max)

#数字の入れ替え
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

#tupleを使った数字の入れ替え
a = 100
b = 200
print(a,b)
a, b = b, a
print(a,b)

print('#-------------------------------------------------------------------------#')
print('#                   　　　   タプルの使い所                                 #')

#三つの選択肢の中から二つを選ぶ
chose_from_two = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)


print('#-------------------------------------------------------------------------#')
print('#                             辞書型                                       #')

d = {'x':10, 'y':20}
print(d)
print(type(d))

#dのxの値をとる
print(d['x'])
#dのyの値をとる
print(d['y'])

#dのxに１００を代入する
d['x'] = 100
print(d)

#文字列を代入
d['x'] = 'XXXXX'
print(d)

#新しく値を代入
d['z'] = 200
print(d)

#キーを数字に設定し値おを代入
d[1] = 10000
print(d)

#辞書型の生成方法
D = dict(a=10, b=20)
print(D)

#辞書型＋タプルの組み合わせ
dtuple=dict([('a',10),('b', 20)])
print(dtuple)

print('#-------------------------------------------------------------------------#')
print('#                           辞書型のメソッド                                 #')

d = {'x':10, 'y':20}
print(d)


print(d.keys())
print(d.values())


d2 = {'x': 1000, 'j': 500}
print('d2 =', d2)

#dにd2の情報を上書きする、オーバーライトする
d.update(d2)
print(d)

#dの値をとる
print(d['x'])
print(d.get('x'))

#ない場所を指定すると
r = d.get('z')
print(r)
print(type(r))


#中身を取り出す
print(d.pop('x'))
print(d)

print('#-------------------------------------------------------------------------#')
print('#                             辞書型のcopy                                 #')

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y) #参照渡しが起きてyにはxのアドレスが入ってる。

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)


print('#-------------------------------------------------------------------------#')
print('#                             辞書型の使い所                                #')
#リスト型
#appleをピックアップするときは、見つけるプログラムを書かないといけない。時間がかかる
l = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],
]


#辞書型
#キーで値を検索して値をとってきたい場合は、辞書型がいい。ハッシュテーブルを用いている。
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])


print('#-------------------------------------------------------------------------#')
print('#                                 集合型                                   #')

#辞書型のように{}で宣言した場合、重複している部分が消える.

a = {1,2,3,4,4,4,5,6}
print(a)

#型を見てみるとset型になっている
print(type(a))

b = {2,3,3,6,7}
print(b)


print(a-b)
print(b-a)
print(a & b)
print(a|b)
print(a^b)


print('#-------------------------------------------------------------------------#')
print('#                              集合型のメソッド                              #')

s = {1,2,3,4,5}
print('s = ', s)

#集合はインデックスがない、関係ない
#s[0] --> Error

s.add(6)
print('s = ', s)

#集合なので6を加えても変わらない
s.add(6)
print('s = ', s)

#消す
s.remove(6)
print('s = ', s)

s.clear()
print('s = ', s)

print(type(s))

print('#-------------------------------------------------------------------------#')
print('#                              集合型の使い所                              #')
#自分の友達がいて、その友達と他の友達の共通の友達探すとか
#何かの共通点を見つけ出すときに集合が使える

my_friends = {'A', 'C', 'D'}
A_friends = {'B','D', 'E', 'F'}

print(my_friends & A_friends)


#Listは集合へ型変換できる。重複を消せる
f = ['apple', 'bannana','apple', 'bannana']
kind = set(f)
print(kind)





