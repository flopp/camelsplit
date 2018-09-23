[![Build Status](https://travis-ci.org/flopp/camelsplit.svg?branch=master)](https://travis-ci.org/flopp/camelsplit)
![License MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat)

# camelsplit
Camel case aware word splitting.

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
