from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['angus'] = 'java'
favorite_languages['jen'] = 'c'
favorite_languages['phil'] = 'php'
favorite_languages['guangsir'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
