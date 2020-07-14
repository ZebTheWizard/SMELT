from SMELT.Enhancement import Enhancement
from PIL import Image, ImageOps, ImageEnhance, ImageStat
from SMELT.buffers import PillowBuffer

class SimpleInvertAndIncreaseContrast(Enhancement):
    def enhance(self, buffer, show):
        image = Image.open(buffer)

        fmt = image.format
        image = image.convert('L')
        stat = ImageStat.Stat(image)
        if stat.mean[0] < 127.5:
            image = ImageOps.invert(image)

        image = ImageEnhance.Contrast(image).enhance(5)
        image = ImageEnhance.Sharpness(image).enhance(0.9)
        image = ImageEnhance.Contrast(image).enhance(5)
        image = ImageEnhance.Sharpness(image).enhance(0.9)


        if show:
            image.show()

        # image.save(output, format=fmt)

        return PillowBuffer(image, format=fmt)
