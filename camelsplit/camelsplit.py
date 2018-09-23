def camelsplit(camel_string):
    """Splits 'camel_string' at 'camel case aware' word boundaries and
    returns the result a list of strings.

    >>> camelsplit('CamelCase')
    ['Camel', 'Case']

    >>> camelsplit('HTTPRequest')
    ['HTTP', 'Request']

    >>> camelsplit('IEEE 802.11ac')
    ['IEEE', ' 802.11', 'ac']
    """
    res = []
    w = ''
    last_upper = False
    last_alpha = True
    for c in camel_string:
        if c.isalpha():
            if last_alpha:
                if c.isupper():
                    if len(w) > 0 and not last_upper:
                        res.append(w)
                        w = ''
                    last_upper = True
                else:
                    if len(w) > 1 and last_upper:
                        res.append(w[0:-1])
                        w = w[-1]
                    last_upper = False
            else:
                if w != '':
                    res.append(w)
                    w = ''
                last_upper = c.isupper()
            last_alpha = True
        else:
            if last_alpha and w != '':
                res.append(w)
                w = ''
            last_alpha = False
        w += c
    if w != '':
        res.append(w)
    return res
