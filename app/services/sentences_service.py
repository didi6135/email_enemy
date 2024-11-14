
def organize_sentences(data):
    sentences = data.get("sentences", [])

    suspicious_sentences = [s for s in sentences if "explosive" in s.lower() or "hostage" in s.lower()]
    non_suspicious_sentences = [s for s in sentences if s not in suspicious_sentences]

    data["sentences"] = suspicious_sentences + non_suspicious_sentences

    return data