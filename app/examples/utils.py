#!/usr/bin/env python3
import os
import webbrowser
from enum import Enum
from os import system
from time import sleep

import typer as typer
from rich.traceback import install

# suppress self
install(show_locals=False, extra_lines=0, )


class sugar_level(Enum):
    low = "low"
    medium = "medium"
    high = "high"

    # def __str__(self):
    #     return self.value


class cheese_type(Enum):
    cheddar = "cheddar"
    mozzarella = "mozzarella"
    feta = "feta"
    gouda = "gouda"
    swiss = "swiss"
    parmesan = "parmesan"
    brie = "brie"
    camembert = "camembert"
    havarti = "havarti"
    gorgonzola = "gorgonzola"
    blue = "blue"
    goat = "goat"
    cream = "cream"
    ricotta = "ricotta"
    cottage = "cottage"

    def __str__(self):
        return self.value


# print(DynamicEnum.foo.value)
def give_cheese(person, sugar_level: sugar_level, amount: int = 0, cheese_type: cheese_type = cheese_type.cheddar,
                should_give: bool = False, am_I_a_good_person=False, how_much_to_take_away: int = 0) -> object:
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

def call_person(person):
    print(f"Calling {person}")
    sleep(4)
    print(f"Done calling {person}")


def withargs(arg1, arg2):
    return f"{arg1} and also {arg2}"


class yarden:
    @staticmethod
    def website(page=""):
        page = f"/docs/{page}" if page else ""
        webbrowser.open(f"https://yarden-zamir.com{page}")

    @staticmethod
    def github():
        webbrowser.open("https://github.com/yarden-zamir")
