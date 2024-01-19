from setuptools import setup

setup(
    name='suno-bark',
    version='0.1.5',
    packages=['bark'],
    install_requires=['encodec', 'funcy', 'tqdm', 'transformers']
)
