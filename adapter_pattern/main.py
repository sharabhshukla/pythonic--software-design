# Dog - Cycle
# human - Truck
# car - Car

class MotorCycle:

	"""Class for MotorCycle"""

	def __init__(self):
		self.name = "MotorCycle"

	def TwoWheeler(self):
		return "TwoWheeler"


class Truck:

	"""Class for Truck"""

	def __init__(self):
		self.name = "Truck"

	def EightWheeler(self):
		return "EightWheeler"


class Car:

	"""Class for Car"""

	def __init__(self):
		self.name = "Car"

	def FourWheeler(self):
		return "FourWheeler"

class Adapter:
	"""
	Adapts an object by replacing methods.
	Usage:
	motorCycle = MotorCycle()
	motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
	"""

	def __init__(self, obj, **adapted_methods):
		"""We set the adapted methods in the object's dict"""
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __getattr__(self, attr):
		"""All non-adapted calls are passed to the object"""
		return getattr(self.obj, attr, 'Not Found')

	def original_dict(self):
		"""Print original object dict"""
		return self.obj.__dict__


""" main method """
if __name__ == "__main__":

	"""list to store objects"""
	motor_cycle = MotorCycle()
	truck = Truck()
	car = Car()
	objects = [Adapter(motor_cycle, output_data = motor_cycle.TwoWheeler),
			   Adapter(truck, output_data = truck.EightWheeler),
			   Adapter(car, output_data = car.FourWheeler)]

	for obj in objects:
		print("A {0} is a {1} vehicle".format(obj.name, obj.output_data()))
