class PetrolCar:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def refuel(self):
        print(f"{self.model}: Заправка {self.fuel_type}")

    def drive(self):
        print(f"{self.model}: Движется с характерным звуком ДВС")

    def check_petrol(self):
        print(f"{self.model}: Проверка наличия бензина")



class ElectricCar:
    def __init__(self,battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.model}: Заряжается электроэнергией, емкость {self.battery_capacity} кВт*ч")

    def drive(self):
        print(f"{self.model}:  Движется на электротяге")

    def check_battery(self):
        print(f"{self.model}: Проверка уровня заряда батареи")


class HybridCar(PetrolCar,ElectricCar):

    def __init__(self, battery_capacity, fuel_type):
        ElectricCar.__init__(self.battery_capacity)
        PetrolCar.__init__(self.fuel_type)

    def charge(self):
        super().charge()

    def check_battery(self):
        super().check_battery()

    def check_petrol(self):
        super().check_petrol()

    def refuel(self):
        super().refuel()

    def drive(self):
        super().drive()

    @staticmethod
    def engine_start():
        print('Машина двжется')

    @staticmethod
    def engine_stop():
        print('Машина не движется')
