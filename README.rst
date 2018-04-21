--- For original README and other user guides, please refer to https://github.com/Jetsetter/pybktree ---


This is a simpler implementation, which uses Levenshtein distance to compare actual strings. You just need to have "distance" library installed, and instantiate the BKTree class.
Simple example:
words = {"hat":1, "chat":1, "something totally different":1}
tree = BKTree(words)
print(tree.find("cat",1))

For better understanding, please read the original repository.


This is my modification of Jetsetter's original implementation of a BKTree in Python. I changed a couple of functions and inputs so it could work better with another project of mine.

CREDITS:
pybktree was written by Ben Hoyt for Jetsetter and is licensed with a
permissive MIT license
