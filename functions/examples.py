def this_example(example_param):
    print(example_param + " < is an example")


def _hidden_example(hidden_param):
    print(hidden_param + " < is an example")


def i_like_cheese(amount_of_cheese="1"):
    print(f"You got {amount_of_cheese} cheese" if int(
        amount_of_cheese) <= 10 else "You got too much cheese, you are now dead. sadge..")
