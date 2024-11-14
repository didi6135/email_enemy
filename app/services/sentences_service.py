

def organize_sentences(sentences):
    suspicious_sentences = [s for s in sentences if "explosive" in s.lower() or "hostage" in s.lower()]
    non_suspicious_sentences = [s for s in sentences if s not in suspicious_sentences]

    return suspicious_sentences + non_suspicious_sentences