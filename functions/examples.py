
def this_example(example_param):
    """This is an example function.

    Args:
        example_param (str): This is an example parameter.

    Returns:
        str: This is an example return value.
    """
    print(example_param+" < is an example")
    return example_param

def _hidden_example(hidden_param):
    """This is an example function.

    Args:
        hidden_param (str): This is an example parameter.

    Returns:
        str: This is an example return value.
    """
    print(hidden_param+" < is an example")
    return hidden_param

def i_like_cheese(amount_of_cheese="1"):
    """Gives you cheese.

    Args:
        amount_of_cheese (str): The amount of cheese you want.

    Returns:
        str: The amount of cheese you got.
    """
    # make beep sound
    print("\a")
    if int(amount_of_cheese) > 10:
        print("You got too much cheese, you are now dead. sadge..")
        return "You got too much cheese, you are now dead. sadge.."
    print(f"You got {amount_of_cheese} cheese")
    return f"You got {amount_of_cheese} cheese"
