import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='camelsplit',
    version='1.0.1',
    author='Florian Pigorsch',
    author_email='mail@florian-pigorsch.de',
    description='Camel case aware word splitting.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/flopp/camelsplit',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
