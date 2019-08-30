#!/usr/bin/python
import random


class MarkovModel:

    def __init__(self):
        self.first_word = "START"

    @staticmethod
    def read_input(filepath):
        print("Reading input...")
        text_in = ""
        with open(filepath, 'r', encoding="utf8") as file_in:
            for line in file_in.readlines():
                text_in = text_in + line + " "
        return text_in

    @staticmethod
    # getting Starts and Ends
    def starts_ends(text_in):
        print("Finding starts and ends...")
        text_in = "START " + text_in
        paragraphs = [".\n \n", "!\n \n", "?\n \n"]
        for entry in paragraphs:
            while entry in text_in:
                text_in = text_in.replace(entry, " END ENDOFTEXT START ")
        punctuation = [".", "?", "!"]
        for entry in punctuation:
            while entry in text_in:
                text_in = text_in.replace(entry, " END START ")
        return text_in

    @staticmethod
    # does some text processing
    def process_text(text_in):
        print("Starting text processing...")
        remove_characters = [",", ";", ":", '\"', "_", "”", "“", ")", "(", "\n", "/", "- "]
        for i in remove_characters:
            text_in = text_in.replace(i, "")
        text_in = text_in.split(" ")
        while "" in text_in:
            text_in.remove("")
        text_in[-1] = "ENDOFTEXT"
        unique_keys = set(text_in)
        return text_in, unique_keys

    @staticmethod
    # defining how big the window of follow tokens are (inclusive)
    def make_window(text_in):
        print("Finding text windows...")
        window_dict = dict()
        for win_index, word in enumerate(text_in):
            words_after = text_in[win_index + 1: win_index + 2]
            if words_after:
                window_dict.setdefault(word, list())
                window_dict[word].extend(words_after)
        return window_dict

    @staticmethod
    # selecting the next token through random sampling
    def next_word(word, win_dict):
        possible = win_dict[word]
        new_word = random.choices(possible)
        return new_word[0]

    def create_text(self, text_in):
        text_in = self.starts_ends(text_in)
        text_in, keys = self.process_text(text_in)
        text_windows = self.make_window(text_in)
        new_word = self.first_word
        new_text = "\n" + new_word + " "
        print("Finding words...")
        while new_word != "ENDOFTEXT":
            new_word = self.next_word(new_word, text_windows)
            if new_word == "END":
                new_text = new_text + new_word + "\n"
            elif new_word != "ENDOFTEXT":
                new_text = new_text + new_word + " "
        return print(new_text)


# model = MarkovModel()
# input_text = model.read_input(r"stuff_2.txt")
# # input_text = model.starts_ends(input_text)
# # input_text, text_keys = model.process_text(input_text)
# # input_dict = model.make_window(input_text)
# model.create_text(input_text)


class MarkovModelLetter:

    @staticmethod
    def read_input(filepath):
        print("reading input...")
        text_in = ""
        with open(filepath, 'r', encoding="utf8") as file_in:
            for line in file_in.readlines():
                text_in = text_in + line.rstrip() + " "
        return text_in

    @staticmethod
    def process_letters(text_in):
        print("processing text...")
        list_out = []
        remove_characters = [",", ";", ":", '\"', "_", "”", "“", ")", "(", ".", "?", "!", "/", "- "]
        for i in remove_characters:
            text_in = text_in.replace(i, "")
        text_in = text_in.replace("-", ' ')
        text_in = text_in + ' '
        for letter in text_in:
            list_out.append(letter.lower())
        return list_out

    @staticmethod
    def make_window(text_in):
        print("making windows...")
        window_dict = dict()
        for win_index, word in enumerate(text_in):
            words_after = text_in[win_index + 1: win_index + 2]
            if words_after:
                window_dict.setdefault(word, list())
                window_dict[word].extend(words_after)
        return window_dict

    @staticmethod
    def next_letter(word, win_dict):
        possible = win_dict[word]
        next_letter = random.choices(possible)
        return next_letter[0]

    def create_word(self, text_in, first_letter):
        print("creating word...")
        text_in = self.process_letters(text_in)
        text_windows = self.make_window(text_in)
        new_letter = first_letter
        new_word = new_letter
        while new_letter != ' ':
            new_letter = self.next_letter(new_letter, text_windows)
            new_word = new_word + new_letter
        return print("\n" + new_word)


# model = MarkovModelLetter()
# input_text = model.read_input(r"60151-0.txt")
# # letter_list = model.process_letters(input_text)
# # letter_dict = model.make_window(letter_list)
# model.create_word(input_text, "t")
