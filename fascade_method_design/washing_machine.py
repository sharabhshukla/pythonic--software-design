from washing_machine_functions import Washing, Rinsing, Spinning

class WashingMachine(object):

    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def start_wash_cycle(self):
        self.washing.wash()
        self.spinning.spin()
        self.rinsing.rinse()

if __name__ == '__main__':
    washing_machine = WashingMachine()
    washing_machine.start_wash_cycle()
