import re


def organize_sentences(data):
    explosive_pattern = re.compile(r'\bexplos(?:ive|ion|ions|ives|e|ing)\b', re.IGNORECASE)
    hostage_pattern = re.compile(r'\bhostage\b', re.IGNORECASE)

    sentences = data.get("sentences", [])

    suspicious_sentences = [s for s in sentences if explosive_pattern.search(s) or hostage_pattern.search(s)]
    non_suspicious_sentences = [s for s in sentences if s not in suspicious_sentences]

    data["sentences"] = suspicious_sentences + non_suspicious_sentences

    return data
