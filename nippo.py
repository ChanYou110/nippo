# coding: utf-8
import sys

i = 1
format = '## やったこと\n| 開始時間 | 終了時間 | 内容 | 詳細メモ |\n| :-- | :-- | :-- | :-- |\n'
endtime = ''
while endtime != '1830':

    print ('やったこと', i)

    try:
        a, b = input('開始時間(HH mm)：').split()
        c, d = input('終了時間(HH mm)：').split()
    except ValueError:
        print (format)
        sys.exit()
    e = input('内容：')
    f = input('詳細メモ：')

    format += '| ' + a + ':' + b + ' | ' + c + ':' + d + ' | ' + e + ' | ' + f + ' |\n'

    endtime = c + d

    print ('\n')

    i += 1

print ('')

format += '\n## 改善点/今後に向けて\n- \n- \n'

print (format)