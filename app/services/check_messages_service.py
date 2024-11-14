


def check_sentences_for_explosive_or_hostage(sentences):
    if any("explosive" in sentence.lower() for sentence in sentences):
        return "explosive"
    elif any("hostage" in sentence.lower() for sentence in sentences):
        return "hostage"
    return None





