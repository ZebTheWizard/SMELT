import pytesseract as pt
from SMELT import Recognition
from PIL import Image


class TesseractRecognition(Recognition):
    def __init__(self, obj, cmd="/usr/bin/tesseract", **kwargs):
        super().__init__(obj, **kwargs)
        pt.pytesseract.tesseract_cmd = cmd

    def run(self, buffer, **kwargs) -> (str, float):
        image = Image.open(buffer)
        string = pt.image_to_string(image, **kwargs)
        data = pt.image_to_data(image, output_type=pt.Output.DICT, **kwargs)
        confs = list(filter(lambda x: x != '-1', data.get("conf")))
        conf = sum(confs) / len(confs)
        return string, conf
