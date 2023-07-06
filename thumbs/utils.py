from typing import Dict

from github.PaginatedList import PaginatedList
from github.Repository import Repository
from github.Issue import Issue
from html2image import Html2Image

from thumbs.dependencies import get_html2image, get_repository, get_module_path
from thumbs import settings


def get_meetups(_repo: Repository = get_repository()) -> PaginatedList[Issue]:
    return _repo.get_issues()


def build_banner(html: str, css: str = '', _hti: Html2Image = get_html2image()):
    _hti.screenshot(
        html_str=html,
        css_str=css
    )


def build_template(template_name: str, interpolations: Dict[str, str]) -> str:
    template_path = f'{get_module_path()}/{settings.TEMPLATES_DIR}/{template_name}'
    template_content = ''

    with open(template_path, 'r', encoding='utf-8') as template:
        template_content = template.read()

    for key, value in interpolations.items():
        template_content = template_content.replace(key, value)

    return template_content
