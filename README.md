[![Build Status](https://travis-ci.org/flopp/camelsplit.svg?branch=master)](https://travis-ci.org/flopp/camelsplit)
[![PyPI Package](https://img.shields.io/pypi/v/camelsplit.svg)](https://pypi.org/project/camelsplit/)
![License MIT](https://img.shields.io/github/license/flopp/camelsplit.svg)

# camelsplit 🐪🖖
Camel case aware word splitting.


## Install

Just grab the package from PyPI:

```
pip install camelsplit
```

## Usage


```
from camelsplit import camelsplit

# 'CamelCase' -> ['Camel', 'Case']
camelsplit('CamelCase')

# 'HTTPRequest' -> ['HTTP', 'Request']
camelsplit('HTTPRequest')

# 'IEEE 802.11ac' -> ['IEEE', ' 802.11', 'ac']
camelsplit('IEEE 802.11ac')
```

## License

[MIT](https://github.com/flopp/camelsplit/blob/master/LICENSE) &copy; 2018 Florian Pigorsch & contributors
