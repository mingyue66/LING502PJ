# -*- coding: utf-8 -*
import pandas as pd 
import numpy as np

'''
Step1: extract accent from whole dict
'''
file = "unidic-cwj-3.1.0/lex_3_1.csv"

data = pd.read_csv(file,header=None)
data = data.to_numpy()

kana = data[,0].reshape(-1,1)
accent = data[,-5].reshape(-1,1)

dic = np.concatenate((kana,accent),axis=1)
print(dic)
print(dic.shape)


dic = pd.DataFrame(dic)
dic = dic.replace('*', np.nan)
dic_clean = dic.dropna(axis=0)

print(dic_clean.shape)

out = "accent_dic.csv"
pd.DataFrame(dic_clean).to_csv(out, header=False, index=False)


'''
Step2: keep only katakana dict
'''
katakana_list = ['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ','ン','ッ','ー','ー','ガ','ギ','グ','ゲ','ゴ','ザ','ジ','ズ','ゼ','ゾ','ダ','ヂ','ヅ','デ','ド','バ','ビ','ブ','ベ','ボ','ヴパ','ピ','プ','ペ','ポキャ','キュ','キョ','シャ','シュ','ショ','チャ','チュ','チョ','ニャ','ニュ','ニョ','ヒャ','ヒュ','ヒョ','ミャ','ミュ','ミョ','リャ','リュ','リョ','ギャ','ギュ','ギョ','ジャ','ジュ','ジョ','ビャ','ビュ','ビョ','ピャ','ピュ','ピョ','ヴァ','ヴィ','ヴェ','ヴォ','ヴャ','ヴュ','ヴョ','ミェ','ヒェ','ピェ','ビェ','ニェ','チェ','ギェ','キェ','シェ','リェ','ジェ','イェ','ディ','デャ','デュ','デョ','テャ','ティ','テュ','テョ','ツァ','ツィ','ツェ','ツォ','ウィ','ウェ','ウォ','グヮ','クヮ','ドォ','トォ','ズィ','スィ','ファ','フィ','フェ','フォ','トゥ','ドゥ','ァ','ィ','ゥ','ェ','ォ','ャ','ュ','ョ','ヮ','ヶ','クァ','クィ','クェ','クォ','グァ','グィ','グェ','グォ','スァ','スェ','スォ','トァ','トィ','トェ','ドァ','ドィ','ドェ','ウァ']

file = "accent_dic.csv"
f = pd.read_csv(file,header=None)
f_list = f.values.tolist()
#print(f_list)

remain = []
out_file = "katakana_accent_dic.txt"
out = open(out_file,"w")

cnt = 0 
for i in f_list:
	kana = i[0]
	accent = i[1]
	print(kana)

	flag = 0
	for j in kana:
		if j in katakana_list:
			continue
		else:
			flag += 1

	if flag ==0:
		remain.append(i)
		line = str(kana) + ',' + str(accent)+ '\n'
		out.write(line)
		cnt += 1
	
# print(remain)
print("All: " + str(cnt))

'''
Step3: mora
'''
# file = 'katakana_accent_dic.txt'
# out_2 = 'mora_2.txt'
# out_3 = 'mora_3.txt'
# out_4 = 'mora_4.txt'
# out_5 = 'mora_5.txt'
# out_6 = 'mora_6.txt'

# two_mora = []
# three_mora = []
# four_mora = []
# five_mora = []
# six_mora = []

# f = open(file,"r").readlines()
# for line in f:
# 	i = line.strip().split(',',1)
# 	kana = i[0]
# 	if len(kana) == 2:
# 		two_mora.append(i)
# 	elif len(kana) == 3:
# 		three_mora.append(i)
# 	elif len(kana) == 4:
# 		four_mora.append(i)
# 	elif len(kana) == 5:
# 		five_mora.append(i)
# 	elif len(kana) >= 6:
# 		six_mora.append(i)

# j = [out_2,out_3,out_4,out_5,out_6]
# k = [two_mora, three_mora, four_mora, five_mora, six_mora]

# for i in range(5):
# 	out = open(j[i],"w")
# 	for p in k[i]:
# 		line = p[0] + ',' + p[1] + '\n'
# 		out.write(line)
		




