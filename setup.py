from setuptools import setup


setup(
    name='random_yt_playlist',
    version='0.1',
    py_modules=['script'],
    install_requires=[
        'click','requests','click_default_group','browser_cookie3'
    ],
    entry_points='''
        [console_scripts]
        random_yt_playlist=random_yt_playlist.script:cli
    ''',
)