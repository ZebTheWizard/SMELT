from abc import ABC, abstractmethod
from io import BytesIO
from SMELT.Helpers import auto_buffer, dumpstr
from SMELT.Enhancement import Enhancement


class Recognition(ABC):
    """
    Detection should be inherited for custom image detection. **kwargs are available so users can tweak the underlying image
    detection algorithms. When the run method is finished it should return a string of the detected content and the
    confidence level of the image detection.
    """
    string = str
    confidence = 0

    def __init__(self, obj, **kwargs):
        if isinstance(obj, Enhancement):
            self.string, self.confidence = self.run(obj.buffer, **kwargs)
        elif isinstance(obj, BytesIO):
            self.string, self.confidence = self.run(obj, **kwargs)
        else:
            self.string, self.confidence = self.run(auto_buffer(obj), **kwargs)

    @abstractmethod
    def run(self, buffer, **kwargs) -> (str, float):
        pass

    def __str__(self):
        return dumpstr(self)