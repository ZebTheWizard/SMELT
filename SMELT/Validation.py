from abc import ABC, abstractmethod
from SMELT.Recognition import Recognition


class Validation(ABC):
    def __init__(self, detection, min_confidence=0.9):
        if isinstance(detection, Recognition):
            if detection.confidence > min_confidence:
                self.run(detection)
            else:
                self.failed = True
        else:
            raise TypeError("Image must run through Detection before Validation")

    @abstractmethod
    def confidence(self):
        pass

    def passing(self, threshold=0.8):
        return self.confidence() > threshold and not self.failed

    @abstractmethod
    def run(self, detection):
        pass


