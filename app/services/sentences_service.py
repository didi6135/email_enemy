import re


def organize_sentences(data):
    explosive_pattern = re.compile(r'\bexplos(?:ive|ion|ions|ives|e|ing)\b', re.IGNORECASE)
    hostage_pattern = re.compile(r'\bhostage\b', re.IGNORECASE)

    sentences = data.get("sentences", [])

    suspicious_sentences = [s for s in sentences if explosive_pattern.search(s) or hostage_pattern.search(s)]
    non_suspicious_sentences = [s for s in sentences if s not in suspicious_sentences]

    data["sentences"] = suspicious_sentences + non_suspicious_sentences

    return data



data = {
  "email": "jeremy37@example.org",
  "username": "jonesalejandra",
  "ip_address": "215.67.111.124",
  "created_at": "2024-10-15T05:29:13.450066",
  "location": {
      "latitude": 8.5478895,
      "longitude": -135.24204,
      "city": "Port Josephburgh",
      "country": "PA"
  },
  "device_info": {
      "browser": "Mozilla/5.0",
      "os": "iOS",
      "device_id": "c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81"
  },
  "sentences": [
      "Public quickly spend hear sing.",
      "nothing hostage shake decide.",
      "Natural southern what nice."
  ]
}


print(organize_sentences(data))