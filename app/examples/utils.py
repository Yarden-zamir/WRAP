#!/usr/bin/env python3
import os
import webbrowser
from enum import Enum
from os import system
from time import sleep

import typer as typer
from requests import get
from requests.compat import integer_types
from rich import traceback

# suppress self
traceback.install(extra_lines=0)


class sugar_level(Enum):
    low = "low"
    medium = "medium"
    high = "high"


class _cheese_type(Enum):
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
def give_cheese(person, sugar_level: sugar_level, amount: int = 0,
                cheese_type: _cheese_type = _cheese_type.cheddar.value,
                should_give: bool = False, am_I_a_good_person=False, how_much_to_take_away: int = 0):
    """
    Give cheese to someone
    :param person: A person you like, or don't like that may get cheese
    :param amount: How much cheese should be given
    :param cheese_type: The type of cheese to give
    :param should_give: Should the cheese be given in the first place?
    """
    print(
        f"Here is {amount - how_much_to_take_away} of {cheese_type} cheese for {person} {'but you should not give it to them' if not should_give else ''}")


def get_current_time(area="Asia/Jerusalem"):
    from datetime import datetime
    json = get("http://worldtimeapi.org/api/timezone/" + area).json()
    if "error" in json: raise Exception(json["error"])
    return datetime.strptime(json["datetime"], "%Y-%m-%dT%H:%M:%S.%f%z").isoformat()


def list_issues(repo=""):
    system(f"gh issue list {f'--repo {repo}' if repo else ''} ")


def call_person(person):
    print(f"Calling {person}")
    sleep(4)
    return f"{person} Didn't answer, they must not like you"


def add_two(arg1: int, arg2: int):
    return f"{arg1} and also {arg2} together make {arg1 + arg2}"


def ask_open_ai(question, api_key=None, model="text-davinci-003", temperature:float=0.7,
                max_tokens: int = 300, top_p:float=1, frequency_penalty:float=0, presence_penalty:float=0):
    import openai
    openai.api_key = api_key or os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model=model,
        prompt=f"{question}\n\n",
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    return response.choices.pop().text


def explain(command, api_key=None, model="text-davinci-003", temperature:float=0.7,
                max_tokens: int = 300, top_p:float=1, frequency_penalty:float=0, presence_penalty:float=0):
    return ask_open_ai(
        f"Explain the following shell command in a very condescending way using heavy hood slang. Be as funny as possible\n\n{command}\n\n",
        api_key, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty)


class yarden:
    @staticmethod
    def website(page=""):
        page = f"/docs/{page}" if page else ""
        webbrowser.open(f"https://yarden-zamir.com{page}")

    @staticmethod
    def github():
        webbrowser.open("https://github.com/yarden-zamir")

    class email_types(Enum):
        dev = "dev"
        work = "work"
        personal = "personal"

    @staticmethod
    def email(type: email_types):
        webbrowser.open(f"mailto:{type.value}@yarden-zamir.com")

    @staticmethod
    def name():
        print("Yarden Zamir")

    class food:
        @staticmethod
        def cheese():
            print("yarden likes cheese")

        @staticmethod
        def pizza():
            print("yarden doesn't like pizza that much")
