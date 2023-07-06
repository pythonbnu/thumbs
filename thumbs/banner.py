from html2image import Html2Image
from thumbs.dependencies import get_html2image


def build_banner(
    html: str,
    css: str = '',
    _hti: Html2Image = get_html2image()
):
    _hti.screenshot(
        html_str=html,
        css_str=css
    )
