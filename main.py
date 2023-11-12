text_file = open("text.txt", encoding="utf-8")
text = text_file.read()

if text.__len__() == 0:
    print("Файл порожній!")
else:
    signs = ['.', ',', ';', ':', '!', '?']
    paragraphs = text.split("\n\n")

    print("Абзаци зі словами-тегами:" + "\n")
    for paragraph in paragraphs:
        words_in_paragraph = paragraph.split()
        for word in words_in_paragraph:
            if word.startswith('#') and not any(word.endswith(sign) for sign in signs):
                print(paragraph + "\n")
                break
