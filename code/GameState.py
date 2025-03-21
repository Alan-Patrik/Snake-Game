from abc import ABC, abstractmethod


class GameState(ABC):
    @abstractmethod
    def handle_input(self, game):
        pass

    @abstractmethod
    def update(self, game):
        pass

    @abstractmethod
    def draw(self, game):
        pass
