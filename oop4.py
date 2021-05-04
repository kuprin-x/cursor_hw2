from abc import abstractmethod, ABC

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, name, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.name = name
        self.screen_ = screen
        self.keyboard_ = keyboard
        self.touchpad_ = touchpad
        self.webcam_ = webcam
        self.ports_ = ports
        self.dynamics_ = dynamics

    def screen(self):
        print(f'{self.name} has a {self.screen_} screen')


    def keyboard(self):
        print(f'{self.name} has {self.keyboard_} keyboard ')


    def touchpad(self):
        print(f'{self.name} has {self.touchpad_} touchpad')


    def webcam(self):
        print(f'{self.name} has a webcam with {self.webcam_}')


    def ports(self):
        print(f'{self.name} has ports - {self.ports_}')


    def dynamics(self):
        print(f'{self.name} has {self.dynamics_} dynamics')


hp_lap = HPLaptop('Fujitsu', '14"','Membrane','sensitive','hd','3USB','2')
hp_lap.screen()
hp_lap.keyboard()
hp_lap.touchpad()
hp_lap.webcam()
hp_lap.ports()
hp_lap.dynamics()