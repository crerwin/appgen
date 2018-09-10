from setuptools import setup

setup(
    name='appgen',
    version='1.0.3',
    packages=['appgen'],
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'appgen = appgen.appgen:main'
        ]
    }
)
