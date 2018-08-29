from setuptools import setup

setup(
    name='appgen',
    version='0.1.1',
    packages=['appgen'],
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'appgen = appgen.appgen:main'
        ]
    }
)
