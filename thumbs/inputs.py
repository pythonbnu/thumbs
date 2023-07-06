from questionary import select, text, Choice, Question
from thumbs.utils import get_meetups
from thumbs import settings


class MeetupInputs:

    def __init__(self):
        self.open_meetups = get_meetups()


    @property
    def meetup(self) -> Question:
        return select(
            message='Para qual meetup você deseja criar o banner?',
            choices=[
                Choice(meetup.title, meetup)
                for meetup in self.open_meetups
            ]
        )


    @property
    def custom_image(self) -> Question:
        return text(
            message='Insira o caminho ou URL para uma imagem customizada:',
            default=settings.DEFAULT_CUSTOM_IMAGE
        )


    @property
    def meetup_time(self) -> Question:
        return text(
            message='Qual o horário do evento?',
            default=settings.DEFAULT_MEETUP_TIME
        )


    @property
    def template(self) -> Question:
        return text(
            message='Template deseja usar?',
            default=settings.DEFAULT_MEETUP_TEMPLATE
        )
    