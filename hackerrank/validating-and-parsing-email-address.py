import re
import email.utils

regex_pattern = r'^([a-z]{1})([a-z,1-9,\.,\-,\_])*(@){1}([a-z])*(\.){1}[a-z]{1,3}$'

for _ in range(int(input())):
    email_full = input()
    parsed_email = email.utils.parseaddr(email_full)
    clean_email = parsed_email[1]
    if str(bool(re.match(regex_pattern, clean_email))) == 'True':
        print(email_full)
    else:
        pass