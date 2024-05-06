import os

import PyPDF2


def pdf_to_string(path):
    if not os.path.isdir(path):
        return "The provided path is not a directory"

    pdf_contents = []

    # Iterate over each file in the directory
    for filename in os.listdir(path):
        # Open the PDF file to read & bytes
        with open(os.path.join(path, filename), 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            content = ""

            # Iterate over each page in the PDF
            for page_num in range(pdf_reader.getNumPages()):
                content += pdf_reader.getPage(page_num).extractText()

            pdf_contents.append(content)

    return pdf_contents


def split_into_words(list_of_strings):
    # List to hold the list of words for each string
    list_of_word_lists = []

    # Iterate over each string in the list
    for string in list_of_strings:
        # Split the string into words and add the list of words to the list
        list_of_word_lists.append(string.split(" "))

    return list_of_word_lists


def create(path):
    pdf_string_list = pdf_to_string(path)
    words_pdf_list = split_into_words(pdf_string_list)

    for pdf_string in words_pdf_list:
        for word in pdf_string:
            print(word)
