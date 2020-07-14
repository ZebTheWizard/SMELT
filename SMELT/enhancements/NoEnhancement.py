from SMELT.Enhancement import Enhancement, save_location


class NoEnhancement(Enhancement):
    buffer = bytes()

    def enhance(self, buffer):
        self.buffer = buffer
