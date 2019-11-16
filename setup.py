from setuptools import setup

setup(
    name='brachiograph_utils',
    version='0.1',
    py_modules=['brachiograph_utils'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        brachiograph-utils=brachiograph_utils.cli:cli
    ''',
)

