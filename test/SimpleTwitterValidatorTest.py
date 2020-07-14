import unittest
from PIL import Image
from SMELT.enhancements import SimpleInvertAndIncreaseContrast
from SMELT.recognitions import TesseractRecognition


class SimpleTwitterValidatorTest(unittest.TestCase):
    cmd = r'/usr/bin/tesseract'

    def test_real_tweet(self):
        image = Image.open("images/tweet_real.jpeg")
        enhance = SimpleInvertAndIncreaseContrast(image, show=False)
        detection = TesseractRecognition(enhance, cmd="/usr/bin/tesseract")
        print(detection)


if __name__ == '__main__':
    unittest.main()
