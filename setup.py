from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(
    name='arch-byte',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = app:main',
        ],
    },
)
