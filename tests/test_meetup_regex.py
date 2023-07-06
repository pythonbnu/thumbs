from unittest.mock import MagicMock
from pytest import fixture

from thumbs.meetup import Meetup


@fixture
def issue():
    return MagicMock(
        body='## 32º encontro do GruPy Blumenau\r\n\r\n### Data do encontro\r\n\r\n29 de julho de 2023\r\n\r\n### Local do encontro\r\n\r\nFURB Campus 1, Bloco S, Sala s412\r\n\r\n---\r\n\r\n'
    )


def test_meetup_title_ok(issue):
    meetup = Meetup(issue)
    expected_value = '32º encontro do GruPy Blumenau'
    assert meetup.title == expected_value # nosec


def test_meetup_date_ok(issue):
    meetup = Meetup(issue)
    expected_value = '29 de julho de 2023'
    assert meetup.date == expected_value # nosec


def test_meetup_location_ok(issue):
    meetup = Meetup(issue)
    expected_value = 'FURB Campus 1, Bloco S, Sala s412'
    assert meetup.location == expected_value # nosec
