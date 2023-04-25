from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.name = name
        self.locator = locator


class Button(Component):
    def __init__(self):
        super().__init__()
