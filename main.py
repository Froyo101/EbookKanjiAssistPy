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
        print(line, type(line))
        scrapeKanji(line)

    f.close()
elif fileType == "epub":
    # You may need to be careful about relative paths here - ebooklib may require absolute pathing
    epubPath = os.path.abspath("text/{0}.epub".format(fileName))
    book = epub.read_epub(epubPath)

    documents = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    # TODO - Prompt user to input their document's number or start with the first and loop through all
    # Need to also display the index of each document before giving the preview of its contents
    for doc in documents:
        name = doc.get_name() # Should also consider using bs to extract the title of each document for a more user-friendly name
        print(name)

        # Parse the XHTML body from here
        soup = BeautifulSoup(doc.get_body_content(), "html.parser")
        content = [p.get_text() for p in soup.find_all('p')]

        # Prints a sample of the first 3 paragraphs found in the document
        realParagraphCount = 0
        paragraphIndex = 0
        # TODO - Should prob change this block to not default to failure when < 3 pars exist. Check the length of content before the other logic
        try:
            while realParagraphCount < 3:
                if content[paragraphIndex] and (not content[paragraphIndex].isspace()):
                    # TODO - Add a filter that only displays the first ~30-50 chars of each section
                    # Ex. - if len(par) > 30, print(par[:30]), else, print(par)
                    print("Section {0}:".format(realParagraphCount + 1), content[paragraphIndex])
                    realParagraphCount += 1
                    paragraphIndex += 1
                else:
                    paragraphIndex += 1
        except IndexError:
            print("Sample exhausted") # Full sample not available? Less than 3 pars?
else:
    print("ERROR: Invalid filetype detected")

# Consider having a main loop that requests input to retrieve the next batch of kanji data for each document that is being parsed (user can enter "exit" or "stop" to break)
# When you've exhausted a document, it will then prompt if you would like to continue on to the next document

for kanji in kanjiList:
    print(kanji)
    webbrowser.open("https://jisho.org/search/{0} %23kanji".format(kanji))
    input("Continue? ")
