# First I put this in the TERMINAL in pycharm: pip install translate
# this installed the package to translate

from translate import Translator
translator = Translator(to_lang="zh")
translation = translator.translate("This is a pen.")
print(translation)