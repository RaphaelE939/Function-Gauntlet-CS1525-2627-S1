def is_even(number:int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: An integer the player inputs
    :return: If the integer is even or odd
    """
    if number % 2 == 0:
        return True
    else:
        return False


def count_vowels(text:str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: A word or sentence the player inputs
    :return: The amount of vowels in the word or sentence
    """
    amount_of_vowels = 0
    for character in text:
        if character == "a" or character == "A":
            amount_of_vowels += 1
        if character == "e" or character == "E":
            amount_of_vowels += 1
        if character == "i" or character == "I":
            amount_of_vowels += 1
        if character == "o" or character == "O":
            amount_of_vowels += 1
        if character == "u" or character == "U":
            amount_of_vowels += 1
    return amount_of_vowels


def celsius_to_fahrenheit(celsius:int) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: integer degree input from user
    :return: The integer converted into a fahrenheit measurement
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def reverse_text(text:str)-> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: string input from user
    :return: string input spelled in reverse
    """
    reverse = ""
    for letter in text:
        reverse = letter + reverse
    return reverse


def larger_number(a:int, b:int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: an integer the player inputs
    :param b: an integer the player inputs
    :return: the greater integer
    """

    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return a



def average_two(a:int, b:int) -> float:
    """Calculate and return the average of two integers.

    :param a: first integer the player inputs
    :param b: second integer the player inputs
    :return: the average value of the 2
    """
    average_two = (a+b)/2
    return average_two


def can_afford(balance:int, cost:int) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: the amount of money the player has
    :param cost: The cost of the item the player wants to buy
    :return: whether they player can or cannot afford the item
    """
    if balance > cost:
        return True
    elif balance < cost:
        return False
    elif balance == cost:
        return True



def repeat_text(text:str, times:int) -> str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: the text use wants repeated
    :param times: the amount of times the user wants to repeat the text
    :return: repeated text the desired amount of
    """
    return text * times


def contains_word(sentence:str, word:str)-> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: the sentence the user inputs
    :param word: the word the program checks for in player sentence
    :return: if word is in sentence
    """
    if word in sentence:
        return True
    else:
        return False


def calculate_tip(cost:int, percent:int) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: random integer value the user inputs representing the cost of something
    :param percent: the percent of the cost the user is willing to tip
    :return: tip amount
    """
    decperc = percent/100
    tip_amount = cost * decperc
    return tip_amount


def make_initials(first_name:str, last_name:str)-> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: random first name the user inputs
    :param last_name: random last name the user inputs
    :return: first character from each parameter combined to make initials
    """
    Initial = first_name[0] + last_name[0]
    return Initial.upper()



def percent_score(points:int, possible:int) ->float:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: the amount of points the player has gotten
    :param possible: the amount of points the player could gget
    :return: percentage of acquired points
    """

    if possible <= 0:
        return None
    else:
        return (points/possible) * 100


def is_between(number:int, minimum:int, maximum:int)-> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: the desired number the player wants to check
    :param minimum: the minimum number the value can be equal or greater than
    :param maximum: the maximum number the value can be less than or equal to
    :return: True if the number is between the minimum and maximum.
    """
    if number >= minimum and number <= maximum:
        return True
    else:
        return False


def all_different(a:str, b:str, c:str)-> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a: first string input
    :param b: second string input
    :param c: third string input
    :return: True if all 3 strings are different and False if not
    """
    if a == b or a == c or b==c:
        return False
    else:
        return True


def average_three(a:int, b:int, c:int) -> float:
    """Calculate and return the average of three integers.

    :param a: first integer input
    :param b: second integer input
    :param c: third integer input
    :return: average of all 3 inputs
    """
    return (a+b+c)/3


def describe_temperature(temperature:int, cold_limit:int, hot_limit:int)->str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: the temperature
    :param cold_limit: amount of cold that can be handled
    :param hot_limit: amount of heat that can be handled
    :return: cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"

if __name__ == "__main__":
    print(is_even(4))
    print(is_even(5))

    print(count_vowels("hello"))
    print(count_vowels("AEIOU"))

    print(celsius_to_fahrenheit(0))
    print(celsius_to_fahrenheit(28))

    print(reverse_text("robot"))
    print(reverse_text("Blanco"))

    print(larger_number(10, 5))
    print(larger_number(28, 100))

    print(average_two(10, 20))
    print(average_two(5, 6))

    print(can_afford(20, 15))
    print(can_afford(30, 5))

    print(repeat_text("Go!", 3))
    print(repeat_text("Hi", 2))

    print(contains_word("Hello world", "world"))
    print(contains_word("Python is fun", "sixseven"))

    print(calculate_tip(20, 15))
    print(calculate_tip(50, 20))

    print(make_initials("Cool", "Kidd"))
    print(make_initials("Aura", "King"))

    print(percent_score(18, 20))
    print(percent_score(45, 50))

    print(is_between(5, 1, 10))
    print(is_between(15, 1, 10))

    print(all_different("a", "b", "c"))
    print(all_different("a", "a", "c"))

    print(average_three(10, 20, 30))
    print(average_three(3, 6, 9))

    print(describe_temperature(5, 10, 30))
    print(describe_temperature(20, 10, 30))
