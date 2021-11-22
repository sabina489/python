# Strings, Bytes and Character Encodings
import sys
script, input_encoding, error = sys.argv
def main(language_file, encoding, errors):
    line = language_file.readline() #readline function simply tests for this empty string when it reaches the end of the file.

    if line:   #if line simply tests for this empty string.
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()  #python strip functions remove characters or white spaces from the beginning or end of a string.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages =open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

#Here, the language.txt file simply contains a list of human language names that are encoded in UTF-8.

#TO run this program, we need to type, python3 exercise23.py utf-8 strict
