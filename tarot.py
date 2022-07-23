""""
tarot.py
========

Script interface for the tarot corpus.

"""

import corpora

# Set up the CorpusObject
card_corpus = corpora.CorpusObject()
card_corpus.import_corpus("tarot")


def get_data_from_cardnames(names_list: list):
    """
    Returns raw data (as list of dicts) for the given card names in <names_list>
    """
    matching_cards = card_corpus.get_field_matches("name", names_list)
    return matching_cards


def display_card_data(card_data: dict):
    """LOL"""
    print(str(card_data))


def menu_cardinfo(names_list=[]):
    if len(names_list) == 0:
        print("CARDINFO: Enter blank card name to finish.")
        add_more = True
        while add_more:
            user_input = str(input("Card name: "))
            if user_input == '':
                add_more = False
            else:
                names_list.append(user_input)
    display_card_data(get_data_from_cardnames(names_list))



def menu_main():
    """
    A simple interactive menu for tarot.py features.
    """
    print("Available Commands:")

    menu_commands = ["cardinfo", "help", "quit"]

    for cmd_str in menu_commands:
        print("> %s" % cmd_str)

    menu_active = True
    while menu_active:
        user_input = str(input("tarot> "))
        if user_input == '':
            pass
        elif not user_input in menu_commands:
            print("Command '%s' not recognized" % user_input)
        else:
            if user_input == 'help':
                print("Available commands:")
                print(str(menu_commands))
            if user_input == 'quit':
                print("Goodbye!")
                menu_active = False
            if user_input == 'cardinfo':
                menu_cardinfo([])


if __name__ == '__main__':
    with open('banner.txt', 'r') as f:
        print(f.read())
    print("Tarot Interface\n\n")
    menu_main()
