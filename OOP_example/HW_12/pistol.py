from OOP_example.HW_12.igun import IGun


class Pistol(IGun):

    def __init__(
            self,
            name: str,
            mag_capacity: int,
            current_number_of_rounds: int,
            is_loaded: bool
    ):
        self.__name = name
        self.__mag_capacity = mag_capacity
        self._current_number_of_rounds = current_number_of_rounds
        self.__is_loaded = is_loaded

    @property
    def loading(self):
        """Returns pistol status - loaded or unloaded"""
        if self._current_number_of_rounds <= 0:
            self.__is_loaded = False
            return f"The {self.__name} is unloaded"
        else:
            self.__is_loaded = True
            return f'The {self.__name} is loaded with ' \
                   f'{self._current_number_of_rounds} round(s)!'

    @loading.setter
    def loading(self, rounds: int) -> None:
        """Sets current number of rounds in pistol"""
        if rounds > self.__mag_capacity or rounds < 0:
            raise ValueError(f'Number of rounds should be '
                             f'between 1 and {self.__mag_capacity}')
        self._current_number_of_rounds = rounds

    def shooting(self):
        """Describes shooting the pistol"""
        if self._current_number_of_rounds > 0:
            self._current_number_of_rounds -= 1
            return f'{self.__name} shot one round'
        else:
            return f'Run out of ammo! Load the {self.__name}!'