from abc import ABC, abstractmethod
from .parts.battery.battery import Battery, SpindlerBattery, NubbinBattery
from .parts.engine.engine import Engine, CapuletEngine, WilloughbyEngine, SternmanEngine

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
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        calliope_battery = SpindlerBattery(last_service_date, current_date)
        calliope_engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(calliope_engine, calliope_battery)
    
    @staticmethod 
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        glissade_battery = SpindlerBattery(last_service_date, current_date)
        glissade_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(glissade_engine, glissade_battery)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        palindrome_battery = SpindlerBattery(last_service_date, current_date)
        palindrome_engine = SternmanEngine(last_service_mileage, current_mileage)
        return Car(palindrome_engine, palindrome_battery)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        rorschach_battery = NubbinBattery(last_service_date, current_date)
        rorschach_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(rorschach_engine, rorschach_battery)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        thovex_battery = NubbinBattery(last_service_date, current_date)
        thovex_engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(thovex_engine, thovex_battery)