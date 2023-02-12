def main():
    with open("bad_words.txt", "r") as file:
        bad_words = list(map(lambda x: x.strip(), file.readlines()))

    with open("raw_text.txt", "r") as file:
        raw_text = file.read()
        for word in bad_words:
            new_text = raw_text.replace(word, "*"*len(word))

    with open("censored_text.txt", "w") as file:
        file.write(new_text)


if __name__ == "__main__":
    main()
