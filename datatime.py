import sys
from datetime import date
import inflect


def main():
    birth_str = input("Date of Birth: ")

    try:
        birth_date = date.fromisoformat(birth_str)

    except ValueError:
        sys.exit("Invalid date")

    today = date.today()

    days_passed = (today - birth_date).days

    if days_passed < 0:
        sys.exit("Invalid date")

    minutes  = days_passed * 24 * 60

    output_text = number_to_words(minutes)

    print(f"{output_text} minutes")


def number_to_words(number):
    p = inflect.engine()

    words = p.number_to_words(number, wantlist = False)

    words = words.replace(" and ", " ")

    return words.capitalize()


if __name__ == "__main__":
    main()


    


