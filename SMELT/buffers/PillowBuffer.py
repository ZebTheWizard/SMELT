from io import BytesIO


class PillowBuffer(BytesIO):
    def __init__(self, image, **kwargs):
        super().__init__()
        if kwargs:
            image.save(self, **kwargs)
        else:
            image.save(self, format=image.format)
