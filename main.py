###　漢字読み 本を読んで漢字を学ぶ！
import webbrowser

kanjiList = []

def scrapeKanji(line):
    for char in line:
        unicodeValue = None
        unicodeValue = ord(char)
        print(unicodeValue)
        if unicodeValue >= 0x4e00 and unicodeValue <= 0x9faf:
            kanjiList.append(char)

textFileName = input("Please enter the name of your text file, minus the extension: ")
print(textFileName)

f = open("text/{0}.txt".format(textFileName), "r")

for line in f:
    print("A line detected")
    print(line)
    scrapeKanji(line)

f.close()

for kanji in kanjiList:
    print(kanji)
    webbrowser.open("https://jisho.org/search/{0} %23kanji".format(kanji))
    input("Continue? ")
