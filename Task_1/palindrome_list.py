"""
Palindrome class realization.
"""

from arraystack import ArrayStack
from math import ceil

class Palindrome:
    """
    Class Palindrome
    """

    def read_file(self, path_from):
        """
        Reads a file and returns words from it
        """
        all_list = []

        with open(path_from, 'r', encoding = 'utf-8') as file:
            for line in file:
                all_list.append(line.strip().split()[0])

        return all_list

    def write_to_file(self, path_to, words):
        """
        Writes words to a file
        """
        with open(path_to, 'w', encoding = 'utf-8') as file:
            try:
                file.write(words[0])
            except IndexError:
                pass
            for line in words[1:]:
                file.write("\n")
                file.write(line)

    def find_palindromes(self, path_from, path_to):
        """
        Main function that finds palindroms and writes them to a file
        """
        fin_list = []

        words = self.read_file(path_from)

        for word in words:
            just_word = ArrayStack()
            reversed_word = ArrayStack()
            enough_len = ceil(len(word) / 2)

            for i in range(enough_len):
                just_word.add(word[i])
                reversed_word.add(word[-(i + 1)])

            for i in range(enough_len):
                if just_word.pop() != reversed_word.pop():
                    break
            else:
                fin_list.append(word)

        self.write_to_file(path_to, fin_list)
        return fin_list
