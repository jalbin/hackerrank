import re

# 100,000,000.000

regex_pattern = r"\,|\."	# Do not delete 'r'.


print("\n".join(re.split(regex_pattern, input())))