#エスケープ
test = r'sSay hi to bob\'s mother'
print(test)

#raw文字列   文字列の中のエスケープ文字を無視してバックスラッシュをバックスラッシュとして扱う

#３連クゥートによる複数行文字列　\nというエスケープ文字を使わなくてもよくなる
print("""pfdsa
      fdsafas
      fdas""")

#startswith(),endswith()
print("hello".endswith("lo"))

#join　リストを指定した文字で繋げる 
# split 文字列を分割する。改行したい時なんかに使える
"""
>>> "".join(["sss","bb"])
'sssbb'
>>> ",".join(["sss","bb"])
'sss,bb'
"""

#rjust,ljust(),center()  表形式のデータを正しくスペースを開けて表示したい時に便利
a = 'Hello'.rjust(10)
print(a)
b = 'Hello'.rjust(10, "+")
print(b)

#strip()　文字列の冒頭と末尾の空白文字を除去した新しい文字列を返す.引数を渡すと、渡した文字列を両端から削除する
#rstrip() lstrip() 冒頭もしくは末尾の空白を除去して返すメソッド
spam = '     table   '
spam.strip()
spam.lstrip()

#pyperclip　クリップボードを操作する
import pyperclip
pyperclip.copy('hello world')
pyperclip.paste()
