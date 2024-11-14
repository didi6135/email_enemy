import re

def check_sentences_for_explosive_or_hostage(sentences):

    explosive_pattern = re.compile(r'\bexplos(?:ive|ion|ions|ives|e|ing)\b', re.IGNORECASE)
    hostage_pattern = re.compile(r'\bhostage\b', re.IGNORECASE)

    for sentence in sentences:
        if explosive_pattern.search(sentence):
            return "explosive"
        elif hostage_pattern.search(sentence):
            return "hostage"
    return None





