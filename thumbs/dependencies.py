from functools import lru_cache
from pathlib import Path
from os import getcwd
from os.path import abspath

from github import Github
from github.Repository import Repository
from html2image import Html2Image

from thumbs import settings


@lru_cache
def get_tmp_dir() -> str:
    return f'{getcwd()}/{settings.TEMP_DIR_NAME}'


@lru_cache
def get_module_path() -> str:
    return str(Path(abspath(__file__)).parent)


@lru_cache
def get_repository() -> Repository:
    github = Github()
    return github.get_repo(settings.MEETUPS_REPO)


@lru_cache
def get_html2image(_tmp_dir: str = get_tmp_dir()) -> Repository:
    return Html2Image(
        size=settings.BANNER_SIZE,
        custom_flags=[
            '--no-sandbox'
            '--remote-allow-origins=*',
            '--hide-scrollbars'
        ],
        temp_path=_tmp_dir
    )
