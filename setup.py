from setuptools import setup, find_packages

with open("README.md", "r") as fh:
        long_description = fh.read()

setup(
    name = 'binance-connector-python',
    version = '0.1.3',
    license='MIT',
    description = 'This is a thin library that working as a connector to the Binance public API.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Jeremy',
    url = 'https://github.com/binance-exchange/binance-connector-python',
    keywords = ['Binance', 'Public API'],
    install_requires=[
        'requests'
    ],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    python_requires='>=3.5',
)
