class SentenceError(Exception):
    pass


class Sentence:
    def __init__(self, data=None):
        if isinstance(data, Sentence):
            self.words = data.words.copy()

        elif data is None:
            self.words = []

        elif isinstance(data, list):
            self.words = data.copy()

        elif isinstance(data, str):
            self.words = data.split()

        else:
            raise SentenceError("Expected Sentence object, list or string")

    def __len__(self):
        return len(self.words)

    def __getitem__(self, item):
        return self.words[item]

    def __setitem__(self, key, value):
        if not isinstance(value, str):
            raise SentenceError("The new word must be a string")

        self.words[key] = value

    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence(self.words + other.words)

        elif isinstance(other, str):
            new_words = self.words.copy()
            new_words.append(other)
            return Sentence(new_words)

        else:
            raise SentenceError(
                "Addition error: the right operand must be a string or a Sentence object"
            )

    def __sub__(self, other):
        new_words = []

        if isinstance(other, Sentence):
            for word in self.words:
                if word not in other.words:
                    new_words.append(word)

        elif isinstance(other, str):
            for word in self.words:
                if word != other:
                    new_words.append(word)

        else:
            raise SentenceError(
                "Subtraction error: the right operand must be a string or a Sentence object"
            )

        return Sentence(new_words)

    def __contains__(self, item):
        return item in self.words

    def __str__(self):
        return (
            f"Text: {' '.join(self.words)}\n"
            f"Sentence words: {self.words}\n"
            f"Number of words: {len(self.words)}"
        )


def readfile(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()


def replacements_from_file(file):
    replacements = []

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            words = line.split()

            if len(words) == 2:
                replacements.append((words[0], words[1]))

    return replacements


def read_delete_words(file):
    words = []

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip()

            if word != "":
                words.append(word)

    return words



def main():
    try:
        text = readfile("text.txt")

        sentence = Sentence(text)
        replacements = replacements_from_file("replace.txt")
        words_to_delete = read_delete_words("delete.txt")

        for old_word, new_word in replacements:
            for i in range(len(sentence)):
                if sentence[i] == old_word:
                    sentence[i] = new_word

        for word in words_to_delete:
            sentence = sentence - word

        with open("result1.txt", "w", encoding="utf-8") as file:
            file.write(" ".join(sentence.words))

        print("Number of words in edited text:", len(sentence))

    except FileNotFoundError as error:
        print("File was not found:", error)

    print("\nChecking exception handling:")

    try:
        Sentence(123)
    except SentenceError as error:
        print("Constructor:", error)

    try:
        test_sentence = Sentence("one two three")
        test_sentence[0] = 123
    except SentenceError as error:
        print("Word replacement:", error)

    try:
        test_sentence + 123
    except SentenceError as error:
        print(error)

    try:
        test_sentence - 123
    except SentenceError as error:
        print(error)


if __name__ == "__main__":
    main()