def is_unique_sorting(word: str) -> bool:
    """checks whether the string has all unqiue characters

    this is an O(n log n) algorithm that doesn't use additional
    data structure

    Args:
        word (str): word to be checked
    """
    word = ''.join(sorted(word))
    if len(word) < 2:
        return True
    i = 1
    while i < len(word):
        if word[i] == word[i - 1]:
            return False
        else:
            i += 1
    return True
    

if __name__ == '__main__':
    print(f'word is: {"word"} - {is_unique_sorting("word")}')
    print(f'word is: {"qa"} - {is_unique_sorting("qa")}')
    print(f'word is: {"abdullah"} - {is_unique_sorting("abdullah")}')
    