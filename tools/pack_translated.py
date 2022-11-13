import os

TEXT_DIR = os.listdir("../target")

OUT_TEXT = os.path.join("..","export","US_Strings.txt")
MID_TEXT = ["BINTEXT",""]

for TEXT in TEXT_DIR:
    with open(os.path.join("..","target",TEXT), 'r', encoding="utf-8") as txt:
        print(TEXT)
        BLOCK = txt.read().splitlines()
        BLOCK = [i for i in BLOCK if i[0] != "#" and len(i) != 0]
        MID_TEXT.extend(BLOCK)
MID_TEXT.extend(["          7356"])

PROC_TEXT = [T.encode('cp1251').decode('cp1252') for T in MID_TEXT]
with open(OUT_TEXT, 'w', encoding='utf-16-le') as txt:
    txt.seek(0)
    txt.write('\ufeff') # Сигнатура Unicode
    for T in PROC_TEXT:
        txt.write(T+'\n')