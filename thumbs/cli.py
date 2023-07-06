from typer import Typer

from thumbs.utils import build_banner, build_template
from thumbs import settings
from thumbs.meetup import Meetup
from thumbs.inputs import MeetupInputs


app = Typer()


@app.command()
def meetup_banner():
    inputs = MeetupInputs()
    selected_meetup = Meetup(inputs.meetup.ask())
    template_name = inputs.template.ask()

    interpolations = {
        '{meetup_title}': selected_meetup.title.upper(),
        '{meetup_location}': selected_meetup.location.upper(),
        '{meetup_date}': selected_meetup.date.upper(),
        '{project_repo}': settings.MEETUPS_REPO,
        '{logo_url}': settings.LOGO_URL,
        '{custom_image_src}': inputs.custom_image.ask(),
        '{meetup_time}': inputs.meetup_time.ask(),
    }

    template = build_template(template_name, interpolations)
    build_banner(template)
