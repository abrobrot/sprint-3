class Car:
    def __init__(self,color,mileage, number: str = None):
        self.color = color
        self.mileage = mileage
        self._number: Optional[str] = None

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if self._number is None:
            self._number= value
        else:
            raise ValueError("номер нельзя менять")

    def increase_mileage(self, km):
        self.mileage += km
        print(f" Добавочный пробег {km} км. Измененный пробег: {self.mileage} км")


    def __str__(self):
        return f"машина ({self.color}), пробег: {self.mileage} km, номер: {self._number or 'нет значения'}"

cars = []
colors = ["blue", "green", "black"]
mileages = [2633, 1312, 1134]
step = 0


for i,color, in enumerate(colors, start = 1 ):

    car =  Car(color, mileages[step])
    step = step +1
    cars.append(car)


cars[0].number = "A222BC777"
cars[1].number = "B888DE123"
cars[2].number = "E666FG456"


try:
    cars[0].number= "новый номер"
except ValueError as error:
    print(f"Error: {error}")

for car in cars:
    print(car)
    car.increase_mileage(500)
    print()
