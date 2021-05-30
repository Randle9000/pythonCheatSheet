def first_word(text: str) -> str:
    # my solution
    # list = []
    # trigger = False
    # counter = 0
    # for character in text:
    #     if not trigger and character.isalpha():
    #         list.append(counter)
    #         trigger = True
    #     if trigger and not character.isalpha() and character is not """'""":
    #         list.append(counter)
    #         break
    #     counter += 1
    # else:
    #     list.append(counter)
    # return text[list[0]:list[1]]
    #

    # or better solution:
    text = text.replace('.', ' ').replace(',', ' ').strip()
    return text.split()[0]

    # or the best ale do rozkminienia
    # def first_word(text: str) -> str:
    #     return re.search("([\w']+)", text).group(1)

    #another good one:
#    return re.search("[a-zA-Z']+", text).group()


if __name__ == '__main__':
    print("Example:")

    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")