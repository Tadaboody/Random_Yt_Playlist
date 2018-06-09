from setuptools import setup

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name='random_yt_playlist',
    version='0.1',
    author="Tomer Keren",
    author_email="tomer.keren.dev@gmail.com",
    description="A utility to open a random youtube playlist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tadaboody/Random_Yt_Playlist",
    packages=['random_yt_playlist'],
    install_requires=[
        'click','requests','click_default_group','browser_cookie3'
    ],
    entry_points='''
        [console_scripts]
        random_yt_playlist=random_yt_playlist.script:cli
    ''',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)