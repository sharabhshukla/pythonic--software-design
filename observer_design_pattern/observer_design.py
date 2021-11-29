class Subject(object):

    def __init__(self):
        '''create an empty observer list'''
        self._observers = []

    def notify(self, modifier = None):
        '''Alert the observers'''

        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)


