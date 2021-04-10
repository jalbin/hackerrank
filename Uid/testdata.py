import re

pattern = '[a-z0-9A-Z{5}A-Z{2}0-9{3}]{1}'

# uid = '2TB1YVIGNM'

h = open("cases", "r")
# g = open("datauid", "r")
f = open("resultuid", "w")
# for i in range(int(input())):
	# uid = input().strip()
i = 0
for k in h:
	i = i + 1
	uid = k.strip()
	if re.match(pattern,uid) and  (len(uid) == 10 and len(set(list(uid))) == 10):
		print(uid,'Valid',i)
		f.write("Valid\n")
	else:
		print(uid,'Invalid')
		f.write("Invalid\n")
f.close()
h.close()











# pattern = '[A-Z{2,10}0-9{3,10}a-z{0,10}]+'

# pattern = '[A-Z{2,10}0-9{3,10}a-z{0,10}]+'

# # uid = 'wU8g8C7XrN90'
# # uid = 'AhBYw9r675' # l6 valid
# uid = 'yDO9Ee83fJ' # l8 valid
# 96R5ZDJg72 # l11 valid
# print(	'uid:',uid									)
# print(	'len(uid):',len(uid)						)
# print(	'list(uid):',list(uid)						)
# print(	'len(list(uid)):',len(list(uid))			)
# print(	'set(list(uid)):',set(list(uid))			)
# print(	'len(set(list(uid))):',len(set(list(uid)))	)

# if re.match(pattern,uid)  and  len(uid) == 10 and len(set(list(uid)) == 10:
# 	print('Valid')
# else:
# 	print('Invalid')