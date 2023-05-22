#engine.py

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage) -> None:
        self._last_service_mileage = last_service_mileage
        self._current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        return self._current_mileage - self._last_service_mileage > 30,000
    
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage) -> None:
        self._last_service_mileage = last_service_mileage
        self._current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        return self._current_mileage - self._last_service_mileage > 60,000

class SternmanEngine(Engine):
    def __init__(self, warning_light_on) -> None:
        self._warning_light_on = warning_light_on
    
    def needs_service(self) -> bool:
        return self._warning_light_on