class Device:
    def __init__(self, color, power, volume=None):
        self.__color = color
        self.__power = power
        self.__volume = volume

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def __str__(self):
        retSTR = (f'Color - {self.__color}\n'
                  f'Power - {self.__power} W\n')
        if self.__volume:
            retSTR += f'Volume - {self.__volume} L\n'
        return retSTR


class CoffeeMachine(Device):
    def __init__(self, pressure, color, power, volume):
        super().__init__(color, power, volume)
        self.__pressure = pressure
        self.__volume = volume

    @property
    def pressure(self):
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure):
        self.__pressure = pressure

    def __str__(self):
        return (f'{super().__str__()}'
                f'Pressure - {self.__pressure} bar\n')


class Blender(Device):
    def __init__(self, color, power, volume):
        super().__init__(color, power, volume)


class MeatGrinder(Device):
    def __init__(self, color, power):
        super().__init__(color, power)


class DustSucker(Device):
    def __init__(self, weight, color, power, volume):
        super().__init__(color, power, volume)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def __str__(self):
        return (f'{super().__str__()}'
                f'Weight - {self.__weight} KG\n')


Philips_EP2230 = CoffeeMachine(15, 'black', 1500, 1.8)
Cecotec_Power_Titanium_2000_Pro = Blender('black', 2000, 2)
SeaBreeze_SB004 = MeatGrinder('black', 2600)
Deerma_Vacuum_Cleaner_Wet_and_Dry_TJ200 = DustSucker(5, 'white', 400, 6)

# print(Philips_EP2230)
# print(Cecotec_Power_Titanium_2000_Pro)
# print(SeaBreeze_SB004)
# print(Deerma_Vacuum_Cleaner_Wet_and_Dry_TJ200)

device_list = [0, Philips_EP2230, Cecotec_Power_Titanium_2000_Pro,
               SeaBreeze_SB004, Deerma_Vacuum_Cleaner_Wet_and_Dry_TJ200]

choice = input('Choose a device to get info about:\n'
               '1 - Coffe machine Philips EP2230\n'
               '2 - Blender Cecotec Power Titanium 2000 Pro\n'
               '3 - Meat grinder SeaBreeze SB004\n'
               '4 - Hoover Deerma Vacuum Cleaner Wet and Dry TJ200\n')
print(device_list[int(choice)])
