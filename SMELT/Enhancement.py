from abc import ABC, abstractmethod
from io import BytesIO
from SMELT.Helpers import auto_buffer


class Enhancement(ABC):
    buffer = None

    def __init__(self, obj, show=False):
        if isinstance(obj, Enhancement):
            self.buffer = self.enhance(obj.buffer, show)
        elif isinstance(obj, BytesIO):
            self.buffer = self.enhance(obj, show)
        else:
            self.buffer = self.enhance(auto_buffer(obj), show)

    @abstractmethod
    def enhance(self, buffer, show) -> buffer:
        """Will run some sort of enhancements on BufferIO such as contrast or sharpness. When the show flag is True,
        a preview should be displayed"""
        pass
