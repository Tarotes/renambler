import os

def rename_files():
    file_count = 1
    for filename in os.listdir("."):
        if filename.endswith(".pdf") or filename.endswith(".docx"):
            new_filename = str(file_count) + ".pdf" if filename.endswith(".pdf") else str(file_count) + ".docx"
            os.rename(filename, new_filename)
            file_count += 1

rename_files()
