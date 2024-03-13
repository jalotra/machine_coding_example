from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Operation:
    name : "operation"

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
