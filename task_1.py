import re


def email_parse(email_address):
    new_dict = {}
    re_email = re.compile(r'([a-z \d \S]+)\@')
    re_domain = re.compile(r'\@([a-z . a-z]+)')
    if not re_email.match(email_address) and re_domain.match(email_address):
        raise ValueError
    else:
        new_dict['username'] = re_email.findall(email_address)
        new_dict['domain'] = re_domain.findall(email_address)

    print(new_dict)


