import os
from typing import Sequence

import pytest

import random_yt_playlist
from random_yt_playlist import parse

currnet_dir = os.path.abspath(os.path.dirname(__file__))

@pytest.fixture(scope="session")
def dynamic_html():
    """ A fixture that returns the html for youtube.com according to your current cookies """
    with open(os.path.join(currnet_dir,'dynamic_webpage.html'),'w',encoding='utf-8') as fp:
        fp.write(random_yt_playlist.get_yt_html())
    return random_yt_playlist.get_yt_html()

def test_parser_returns_on_dynamic(dynamic_html):
    assert_is_playlist_list(parse(dynamic_html))

def test_logged_in(dynamic_html):
    assert 'sign in' not in dynamic_html.lower()
    assert 'list=' in dynamic_html

def assert_is_playlist_list(playlist_list : Sequence[str]):
    assert all('list' in playlist for playlist in playlist_list)
    assert len(playlist_list) > 0

def test_get_playlist_list():
    playlist_list = random_yt_playlist.get_playlist_list(cache=False)
    assert_is_playlist_list(playlist_list)