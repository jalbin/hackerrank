import re
for i in range(int(input())):
    uid = input().strip()
    if re.match('\w{10}',uid) and  (sum(u.isupper() for u in uid)>= 2 and sum(c.isdigit() for c in uid) >= 3 and len(list(uid)) == 10 and len(set(list(uid))) == 10):
        print('Valid')
    else:
        print('Invalid')