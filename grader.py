import difflib

def calculate_similarity(string1, string2):
    matcher = difflib.SequenceMatcher(None, string1, string2)
    similarity = matcher.ratio()
    return similarity

def grade(a, b):
    a = a.lower()
    b = b.lower()

    if a == b:
        return 1
    if calculate_similarity(a, b) > .85:
        return 1
    else:
        return 0