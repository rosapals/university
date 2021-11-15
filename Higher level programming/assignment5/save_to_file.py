def save_to_file(filename, texts):
    """Writes given items to filename.txt.
    Input
        filename (str): Name of file to be created. Already-existing files are overwritten
        texts (list of str): Text to be put in .txt-file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(texts+"\n")
    return