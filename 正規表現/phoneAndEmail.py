#! python3
# phoneAndEmail.py

import pyperclip, re

#電話番号の正規表現
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #3桁の市外局番,()がついてもよい
    (\s|-|\.)? #スペースか区切りかハイフンが入る
    (\d{3})      #３けたのしない局番
    (\s|-|\.)  #区切り
    (\d{4})      #4桁の番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #2~5桁の内線番号
    )''', re.VERBOSE)


#電子メールの正規表現
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #ユーザー名
    @  #@記号
    [a-zA-Z0-9.-]+ #ドメイン名
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

#クリップボードのテキストを検索
text = str(pyperclip.paste())
print(text)
matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#検索結果の貼り付け
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました')
    print('\n'.join(matches))
else:
    print("該当するものがありません")






























