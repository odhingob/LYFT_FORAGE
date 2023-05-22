from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):
    def __init__(self) -> None:
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self) -> bool:
        threshold = self._last_service_date.replace(year=self._last_service_date.year + 2)
        return threshold < current_date 

class NubbinBattery(Battery):
    def __init__(self) -> None:
        self._last_service_date = last_service_date
        self._current_date = current_date

    def needs_service(self) -> bool:
        threshold = self._last_service_date.replace(year=self._last_service_date.year + 4)
        return threshold < current_date 

