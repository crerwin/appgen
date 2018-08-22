from setuptools import setup

setup(
    name='appgen',
    version='0.1.0',
    packages=[],
    entry_points={
        'console_scripts': [
            'appgen = appgen.appgen:main'
        ]
    }
)
