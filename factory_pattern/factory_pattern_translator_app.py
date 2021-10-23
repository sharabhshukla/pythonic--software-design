
class FrenchLocalizer(object):

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, message):
        return self.translations.get(message, message)


class SpanishLocalizer(object):

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}


    def localize(self, message):
        return self.translations.get(message, message)


class EnglishLocalizer(object):

    def localize(self, message):
        return message


def factory(language='english'):
    localizers = {
        'french': FrenchLocalizer,
        'spanish': SpanishLocalizer,
        'english': EnglishLocalizer
    }
    return localizers.get(language)()


def main():
    while True:
        language = input('Enter the language you wish to translate to:- ')
        localizer = factory(language)
        message = input('Enter the message:- ')
        print('{} -> {}'.format(message, localizer.localize(message=message)))


if __name__ == '__main__':
    main()