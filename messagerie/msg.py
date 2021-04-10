import email.utils
import re
for i in range(int(input())):
	a = email.utils.parseaddr(input())
	if re.match('^[a-zA-Z][\w\-\.\_]*\@[a-zA-Z]+\.[a-zA-Z]{1,3}$',a[1]):print(email.utils.formataddr((a[0],a[1])))