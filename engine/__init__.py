from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine

class EngineFactory:
    def create_willoughby_engine(self, last_service_date, current_mileage, last_service_mileage):
        return WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)

    def create_sternman_engine(self, last_service_date, warning_light_is_on):
        return SternmanEngine(last_service_date, warning_light_is_on)

    def create_capulet_engine(self, last_service_date, current_mileage, last_service_mileage):
        return CapuletEngine(last_service_date, current_mileage, last_service_mileage)
