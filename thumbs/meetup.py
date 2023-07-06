from re import search, Match
from github.Issue import Issue


class Meetup:

    def __init__(self, issue: Issue):
        self.issue = issue

    def _get_str_from_regex(self, regex: str) -> str:
        string_found: Match = search(regex, self.issue.body) # type: ignore
        return string_found.group()

    @property
    def title(self) -> str:
        return self._get_str_from_regex(r'(\d{2})º encontro d(o GruPy Blumenau|e Python)')

    @property
    def date(self) -> str:
        return self._get_str_from_regex(r'(\d{2}) de (.*) de (\d{4})')

    @property
    def location(self) -> str:
        start_to_remove = 'Local do encontro\r\n\r\n'
        end_to_remove = '\r\n\r\n'
        regex_match = self._get_str_from_regex(start_to_remove + r'(.*)' + end_to_remove)

        start_position = len(start_to_remove)
        end_position = len(regex_match)-len(end_to_remove)

        return regex_match[start_position:end_position]
