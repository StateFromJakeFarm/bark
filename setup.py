from setuptools import setup

setup(
    name='bark',
    packages=['bark'],
    install_requires=['encodec', 'funcy', 'tqdm', 'transformers']
)
