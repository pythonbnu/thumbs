from github.PaginatedList import PaginatedList
from github.Repository import Repository
from github.Issue import Issue

from thumbs.dependencies import get_repository


def get_meetups(_repo: Repository = get_repository()) -> PaginatedList[Issue]:
    return _repo.get_issues()
