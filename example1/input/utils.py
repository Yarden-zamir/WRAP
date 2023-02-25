#!/usr/bin/env python3
import webbrowser
from os import system
from rich.traceback import install
# suppress self
install(show_locals=False, extra_lines=0, )
def give_cheese(person, amount: int = 0, cheese_type: str = "cheddar", should_give: bool = False, am_I_a_good_person= False, how_much_to_take_away:int = 0) -> object:
    """
    Give cheese to someone
    :param person: A person you like, or don't like that may get cheese
    :param amount: How much cheese should be given
    :param cheese_type: The type of cheese to give
    :param should_give: Should the cheese be given in the first place?
    """
    return f"Here is {amount - how_much_to_take_away} of {cheese_type} cheese for {person} {'but you should not give it to them' if not should_give else ''}"

def get_current_time(area="Asia/Jerusalem"):
    from datetime import datetime
    from requests import get
    json = get("http://worldtimeapi.org/api/timezone/" + area).json()
    if "error" in json: raise Exception(json["error"])
    print(datetime.strptime(json["datetime"], "%Y-%m-%dT%H:%M:%S.%f%z").isoformat())



def list_issues(repo=""):
    system(f"gh issue list {f'--repo {repo}' if repo else ''} ")


def withargs(arg1, arg2):
    return f"{arg1} and also {arg2}"

class yarden:
    @staticmethod
    def website(page=""):
        page= f"/docs/{page}" if page else ""
        webbrowser.open(f"https://yarden-zamir.com{page}")

    @staticmethod
    def github():
        webbrowser.open("https://github.com/yarden-zamir")
