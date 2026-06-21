"""
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.
"""

from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Create an array of 26 to counts the letter (bucket count)
        letter_count = [0 for _ in range(26)]

        for c in licensePlate:
            if c.isalpha():
                char = c.lower()

                index = ord(char) - 97

                letter_count[index] += 1

        result: str = ""

        # Iteration over all words
        for word in words:
            # Slice to create a new copy and not only the pointer
            letter_count_copy = letter_count[:]
            for char in word:
                index = ord(char.lower()) - 97
                letter_count_copy[index] -= 1

            if all(x <= 0 for x in letter_count_copy):
                if result == "" or len(word) < len(result):
                    result = word

        return result
