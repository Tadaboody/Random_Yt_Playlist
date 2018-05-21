from setuptools import setup


setup(
    name='random-yt-playlist',
    version='0.1',
    py_modules=['script'],
    install_requires=[
        'click','requests',
    ],
    entry_points='''
        [console_scripts]
        random_yt_playlist=script:cli
    ''',
)