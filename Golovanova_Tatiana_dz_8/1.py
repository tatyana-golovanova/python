import re


EMAIL_REGEXP = re.compile(r'(?P<username>[\w.-]+)@(?P<domain>[\w.-]+(?:\.[\w]+)+)')


def email_parse(email):
    match = EMAIL_REGEXP.search(email)
    if not match:
        raise ValueError(f'wrong email: {email}')

    return match.groupdict()


print(email_parse('someone@geekbrains.ru'))
email_parse('someone@geekbrainsru')
