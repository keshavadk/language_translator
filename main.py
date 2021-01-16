from googletrans import Translator

translator = Translator()

out = translator.translate("क्या हाल है", dest="kn")

print(out)