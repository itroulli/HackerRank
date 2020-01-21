# Name: Validating Email Addresses With a Filter
# Problem: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# Score: 20


def fun(s):
    # return True if s is a valid email, else return False
    try:
        user, domain = s.split('@')
        web, ext = domain.split('.')
    except ValueError:
        return False
    if not user.replace('-', '').replace('_', '').isalnum():
        return False
    elif not web.isalnum():
        return False
    elif not 0 < len(ext) <= 3:
        return False
    else:
        return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)