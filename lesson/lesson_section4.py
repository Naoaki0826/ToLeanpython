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


















