#! python3
# pw.py パワスード管理プログラム

PASSWORDS = {
    'email': 'jfalsjaenfckajfaeiofkae',
    'blog': 'fjaweu-32t9-4/fl:ck4optok',
    'luggage': '12345',
}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方:python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()
    
account = sys.argv[1] #コマンドライン引数

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました。')
else:
    print(account + 'というアカウント名はありません')
    
    