[![Build Status](https://travis-ci.org/flopp/camelsplit.svg?branch=master)](https://travis-ci.org/flopp/camelsplit)
![License MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat)

# camelsplit
Camel case aware word splitting.

## Usage

```
import camelsplit

# 'HTTPRequest' -> ['HTTP', 'Request']
camelsplit.split('HTTPRequest')

# 'JohnDoe123'-> ['John', 'Doe', '123']
camelsplit.split('JohnDoe123')
```

## License

[MIT](https://github.com/flopp/camelsplit/blob/master/LICENSE) &copy; 2018 Florian Pigorsch & contributors
