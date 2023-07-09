from googletrans import Translator

def TranslateIt(sText, lang):
    translator = Translator()

    out = translator.translate(sText, dest=lang)

    return out.text