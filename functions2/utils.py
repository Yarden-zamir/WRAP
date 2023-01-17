import os


def get_current_time(area="Asia/Jerusalem", time_format="%Y-%m-%d %H:%M:%S"):
    from datetime import datetime
    from requests import get
    json = get("http://worldtimeapi.org/api/timezone/" + area).json()
    print(datetime.strptime(json["datetime"], "%Y-%m-%dT%H:%M:%S.%f%z").strftime(time_format))


def give_potato(amount_of_potatoes=1):
    """

    :param amount_of_potatoes:
    """
    if amount_of_potatoes > 10:
        print("You got too many potatoes, you are now dead. sadge..")
    else:
        print(f"You got {amount_of_potatoes} potato" + ("s" if amount_of_potatoes > 1 else ""))
        exit(1)
    os.system("gh issue list")


def list_issues(repo=""):
    if repo:
        os.system("gh issue list --repo " + repo)
    else:
        os.system("gh issue list")

def withargs(arg1, arg2):
    print(arg1, "and also",arg2)
def ls_py():
    os.system("ls")
