import json
import os.path
import random
import re
import webbrowser
from typing import Sequence

import click
from click_default_group import DefaultGroup

LIST_JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'playlists.json')


def print(*args, **kwargs):
    click.echo(*args, **kwargs)


@click.group(cls=DefaultGroup, default='play', default_if_no_args=True)
def cli():
    pass


def get_yt_html():
    html = requests.get(yt_endpoint(), cookies=browser_cookie3.load()).content
    html = html.decode("utf-8")  # cast from bytes to strng
    return html


import requests
import browser_cookie3


@cli.command("parse")
def parse_command():
    get_random_playlist_link(cache=True)


def save_list(playlist_list: list, save_path: str):
    with open(save_path, 'w') as fp:
        json.dump(playlist_list, fp, indent=0)


def yt_endpoint(*args: Sequence[str]) -> str:
    return '/'.join(['https://www.youtube.com', *args])


@cli.command("play")
@click.pass_context
def play_command(ctx):
    webbrowser.open_new_tab(get_random_playlist_link())


def get_playlist_list(cache=True,*,cache_path=LIST_JSON_PATH):
    playlist_list = list()
    try:
        with open(LIST_JSON_PATH) as fp:
            playlist_list = json.load(fp)
    # in case the json doesn't exist, is empty or is an empty list
    except (FileNotFoundError, json.JSONDecodeError, ):
        ...
    if not playlist_list or not cache:
        playlist_list = parse(get_yt_html())
    if cache:
        save_list(playlist_list, cache_path)
    return playlist_list


def get_random_playlist_link(cache=True, cache_path=LIST_JSON_PATH) -> str:
    return yt_endpoint(random.choice(get_playlist_list(cache,cache_path=cache_path)))


def parse(html: str) -> Sequence[str]:
    playlist_re = r"(watch\?v=[^\"]+list=[^\"]+\")"
    return set(match.group().strip('\"') for match in re.finditer(playlist_re, html))


if __name__ == '__main__':
    play_command()
