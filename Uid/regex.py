import re

pattern = '[A-Z{2,7}0-9{3,8}A-Za-z{0,5}]+'

uid = '2TB1YVIGNM'

regex = re.match(pattern,uid)

# if re.match(pattern,uid) and  (len(list(uid)) == 10 and len(set(list(uid))) == 10):
numcount = sum(c.isdigit() for c in uid)
uppercount = sum(u.isupper() for u in uid)
if regex:
	print(	'num of integer:',numcount					)
	print(	'num of upper:',uppercount					)
	print(	'regex:',regex.group(0)						)
	print(	'uid:',uid									)
	print(	'len(uid):',len(uid)						)
	print(	'list(uid):',list(uid)						)
	print(	'len(list(uid)):',len(list(uid))			)
	print(	'set(list(uid)):',set(list(uid))			)
	print(	'len(set(list(uid))):',len(set(list(uid)))	)
else:
	print(uid,'Invalid')
