###　漢字読み 本を読んで漢字を学ぶ！
# Main test relative path - text/この素晴らしい世界に祝福を！1.epub
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os
import webbrowser

kanjiList = []

def scrapeKanji(line):
    for char in line:
        unicodeValue = None
        unicodeValue = ord(char)
        print(unicodeValue)
        if unicodeValue >= 0x4e00 and unicodeValue <= 0x9faf:
            kanjiList.append(char)

fileType = input("Enter the file extension here - txt or epub: ")
fileName = input("Please enter the name of your file, minus the extension: ")
print(fileName)

if fileType == "txt":
    f = open("text/{0}.txt".format(fileName), "r")

    for line in f:
        print("A line detected")
        print(line)
        scrapeKanji(line)

    f.close()
elif fileType == "epub":
    # You may need to be careful about relative paths here - ebooklib may default to absolute pathing
    epubPath = os.path.abspath("text/{0}.epub".format(fileName))
    book = epub.read_epub(epubPath)

    documents = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    # Prompt user to input their document's number or start with the first and loop through all
    for doc in documents:
        body = doc.get_body_content() # BODY SECTION ONLY
    # Parse the XHTML body from here
else:
    print("ERROR: Invalid filetype detected")

# Consider having a main loop that requests input to retrieve the next batch of kanji data for each document that is being parsed (user can enter "exit" or "stop" to break)
# When you've exhausted a document, it will then prompt if you would like to continue on to the next document


for kanji in kanjiList:
    print(kanji)
    webbrowser.open("https://jisho.org/search/{0} %23kanji".format(kanji))
    input("Continue? ")
