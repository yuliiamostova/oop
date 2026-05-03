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

    def __len__(self):
        return len(self.words)

    def __getitem__(self, item):
        return self.words[item]

    def __setitem__(self, key, value):
        self.words[key] = value

    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence(self.words + other.words)

        elif isinstance(other, str):
            new_words = self.words.copy()
            new_words.append(other)
            return Sentence(new_words)

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

        return Sentence(new_words)

    def __contains__(self, item):
        return item in self.words

    def __str__(self):
        return (
            f"Text: {' '.join(self.words)}\n"
            f"Sentence words: {self.words}\n"
            f"Number of words: {len(self.words)}"
        )

    def __iter__(self):
        return SentenceIterator(self)

class SentenceIterator:
    def __init__(self, data):
        if isinstance(data, SentenceIterator):
            self.words = data.words.copy()
            self.index = data.index
        elif isinstance(data, Sentence):
            self.words = sorted(data.words, key=str.lower)
            self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word

def readfile(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

def main():
    text = readfile("text.txt")
    sentence = Sentence(text)
    for word in sentence:
        print(word)

if __name__ == "__main__":
    main()
