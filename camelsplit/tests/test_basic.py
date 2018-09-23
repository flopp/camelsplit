import camelsplit


def test_basic():
    assert camelsplit.split('') == []
    assert camelsplit.split('123') == ['123']
    assert camelsplit.split('test') == ['test']
    assert camelsplit.split('camelCase') == ['camel', 'Case']
    assert camelsplit.split('CamelCase') == ['Camel', 'Case']
    assert camelsplit.split('camel-123-case') == ['camel', '-123-', 'case']
    assert camelsplit.split('HTTPRequest') == ['HTTP', 'Request']
    assert camelsplit.split('HTTPRequest2') == ['HTTP', 'Request', '2']
