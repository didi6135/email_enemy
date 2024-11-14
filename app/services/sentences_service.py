import re


def organize_sentences(data):

    suspicious_pattern = re.compile(r'\b(?:explos(?:ive|ion|ions|ives|e|ing)|hostage)\b', re.IGNORECASE)
    data['sentences'] = sorted(data.get('sentences', []), key=lambda sentence: not bool(suspicious_pattern.search(sentence)))
    return data


