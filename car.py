from abc import ABC, abstractmethod
from .parts.battery.battery import Battery
from .parts.engine.engine import Engine

class Servicable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Servicable):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() 

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        calliope_battery = Battery(last_service_date, current_date)
        calliope_engine = Engine(last_service_mileage, current_mileage)
        return Car(calliope_engine, calliope_battery)
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        glissade_battery = Battery(last_service_date, current_date)
        glissade_engine = Engine(last_service_mileage, current_mileage)
        return Car(glissade_engine, glissade_battery)
    
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        palindrome_battery = Battery(last_service_date, current_date)
        palindrome_engine = Engine(last_service_mileage, current_mileage)
        return Car(palindrome_engine, palindrome_battery)
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        rorschach_battery = Battery(last_service_date, current_date)
        rorschach_engine = Engine(last_service_mileage, current_mileage)
        return Car(rorschach_engine, rorschach_battery)
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        thovex_battery = Battery(last_service_date, current_date)
        thovex_engine = Engine(last_service_mileage, current_mileage)
        return Car(thovex_engine, thovex_battery)