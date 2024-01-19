from setuptools import setup

setup(
    name='suno-bark',
    packages=['bark'],
    install_requires=['encodec', 'funcy', 'tqdm', 'transformers']
)
