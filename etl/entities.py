import spacy
nlp = spacy.load("en_core_web_sm")

def extract(text):
    doc = nlp(text)
    return [(e.text, e.label_) for e in doc.ents]
