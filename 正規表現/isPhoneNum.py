#正規表現を使わない場合
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(is_phone_number('344-444-3434'))

#正規表現(regex)を使う場合
import re
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #r''とすることでエスケープさせている。\\dのように書かなくて良い
mo = phone_num_regex.search('私の電話番号は415-555-3333です')
mo.group() #groupでマッチした箇所を返す

## グルーピング機能
phone_num_regex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #\( \)と書けば本来の丸かっこの文字とマッチするようにな
mo = phone_num_regex1.search('私の電話番号は415-555-3333です')
mo.group(0) #'415-555-3333'
mo.group(1) #'415'
mo.group(2) #'555-3333'
mo.groups(0) #('415', '555-3333')
 
## or の対応するもの   |
## あってもなくても良い場合 ()? 疑問符を使う
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('Batman')
mo1.group()

## ＊　アスタリスクで0回以上のマッチを表す
## +  1回以上のマッチを表す
## 波括弧を用いて繰り返し回数を指定できる
ha_regex = re.compile(r'(Ha){3,5}')
mo1 = ha_regex.search('HaHa') #該当するものがない場合Noneを返す
mo1==None


## 貪欲マッチと非貪欲マッチ  貪欲マッチは、複数の可能性がある場合最も長いものにマッチするのに対して、非貪欲マッチは最も短いものにマッチする

#findall serachが最初にマッチした文字列だけ返すのに対して、findallは全てのマッチした文字列を返す

## キャレット(^)とドル記号($)  先頭と末尾を表す。
##　ワイルドカード文字 (.) 改行以外の任意の文字とマッチする
###何でもマッチする文字を作りたい場合は .* と表す


#改行がある場合の対応
s = """fdsfkl
fdsfasa

fdsfs"""
regex = re.compile('.*')
regex.search(s).group() #改行に対応できていない
regex = re.compile('.*', re.DOTALL) #これでよし
regex.search(s).group()


#小文字大文字を区別したい場合
rebocop = re.compile(r'rebocop', re.I)

#コメントをつけてみやすくする
phone_regex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?))')

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #3桁の市外局番,()がついてもよい
    (\s|-|\.)? #スペースか区切りかハイフンが入る
    \d{3}      #３けたのしない局番
    (\s|-|\.)  #区切り
    \d{4}      #4桁の番号
    (\s*(ext|x|ext.)\s*\d{2,5})?  #2~5桁の内線番号
    )''', re.VERBOSE)
    """
    123-4567（3桁の数字）
    (123) 456-7890（丸括弧で囲まれた3桁の数字）
    """





