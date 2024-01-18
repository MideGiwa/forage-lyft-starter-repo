from calliope import Calliope
from glissade import Glissade
from palindrome import Palindrome
from rorschach import Rorschach
from thovex import Thovex


class CarFactory:
    def create_calliope(self, last_service_date, current_mileage, last_service_mileage):
        return Calliope(last_service_date, current_mileage, last_service_mileage)

    def create_glissade(self, last_service_date, current_mileage, last_service_mileage):
        return Glissade(last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(self, last_service_date, warning_light_is_on):
        return Palindrome(last_service_date, warning_light_is_on)

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage):
        return Rorschach(last_service_date, current_mileage, last_service_mileage)

    def create_thovex(self, last_service_date, current_mileage, last_service_mileage):
        return Thovex(last_service_date, current_mileage, last_service_mileage)
