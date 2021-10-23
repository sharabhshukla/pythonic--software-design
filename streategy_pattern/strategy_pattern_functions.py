import uuid


def electric_discount(car):
    if car.model_name == 'TESLA MODEL S':
        return car.price * (1- 0.20)
    else:
        return car.price * (1- 0.15)


class Car(object):

    def __init__(self, model_name, type, price, discount_strategy):
        self.model_name = model_name
        self.type = type
        self.price = price
        self.discount_strategy = discount_strategy
        self.registration_id = None

    @staticmethod
    def generate_registration_id():
        return str(uuid.uuid4())

    def calculate_final_price(self):
        return self.discount_strategy(self)

    def register(self):
        self.registration_id = self.generate_registration_id()
        print('Car with model name {} and type registered'.format(self.model_name, self.type))
        print('The registration id of the car is {}'.format(self.registration_id))
        print('The final price is {}'.format(self.calculate_final_price()))


if __name__ == '__main__':
    tesla_model_s = Car('TESLA MODEL S', 'Electric', 60000, electric_discount )
    tesla_model_s.register()
