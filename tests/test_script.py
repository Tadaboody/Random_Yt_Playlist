import pytest
import os
currnet_dir = os.path.abspath(os.path.dirname(__file__))

from random_yt_playlist import parse
import random_yt_playlist
@pytest.fixture
def html():
    with open(os.path.join(currnet_dir,'webpage.html'),encoding='utf-8') as fp:
        return fp.read()

@pytest.fixture
def dynamic_html():
    """ A fixture that returns the html for youtube.com according to your current cookies """
    return random_yt_playlist.get_yt_html()

def test_html(html):
    assert html

def test_parser_returns_playlists(html):
    assert all('list' in playlist for playlist in parse(html))

def test_logged_in(dynamic_html):
    assert 'sign in' not in dynamic_html