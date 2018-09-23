from camelsplit import camelsplit


def test_basic():
    assert camelsplit('') == []
    assert camelsplit('123') == ['123']
    assert camelsplit('test') == ['test']
    assert camelsplit('camelCase') == ['camel', 'Case']
    assert camelsplit('CamelCase') == ['Camel', 'Case']
    assert camelsplit('camel-123-case') == ['camel', '-123-', 'case']
    assert camelsplit('HTTPRequest') == ['HTTP', 'Request']
    assert camelsplit('HTTPRequest2') == ['HTTP', 'Request', '2']
    assert camelsplit('IEEE 802.11ac') == ['IEEE', ' 802.11', 'ac']
