
book = "books/frankenstein.txt"

with open(book) as f:
    file_contents = f.read()

print(f"-- Begin report of {book} --")

words = file_contents.split()
print(f"{len(words)} words found in document")

characters = {}
for character in file_contents.lower():
    characters.setdefault(character, 0)
    characters[character] += 1

for k in sorted(characters, key=characters.get, reverse=True):
    if k.isalpha():
        print(f"The letter '{k}' was found {characters[k]} times")

print("-- End report --")
