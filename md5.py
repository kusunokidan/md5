import sys
import hashlib

# 入力したメッセージのMD5ハッシュを表示します。
# 
# 使い方:
# python md5.py メッセージ
# python md5.py -f メッセージファイル
# python md5.py -l メッセージファイル（複数行)
#
# メッセージファイルはUTF-8を想定

args = sys.argv

# まとめて処理
if len(args) > 2 and args[1] == '-l':
    textlist = [str]
    f = open(args[2], 'r', encoding='utf_8_sig')
    textlist = f.readlines()
    for txt in textlist:
        if txt[-1] == '\n':
            txt = txt[:-1]
        print(txt)
        hash = hashlib.md5(txt.encode()).hexdigest()
        print(hash)
    exit()


# 一つだけ処理
if len(args) > 2 and args[1] == '-f':
    # ファイルから
    f = open(args[2], 'r', encoding='utf_8_sig')
    text = f.read()
elif len(args) == 2:
    # コマンドラインから
    text = args[1]
else:
    text = ''
print(text)
hash = hashlib.md5(text.encode()).hexdigest()
print(hash)


