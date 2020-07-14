<div align="center">
<h1>Social Media Engagement Legitimacy Tester(SMELT)</h1>
<!-- <a href="https://bit.ly/3224Lkp"><img src="https://img.shields.io/badge/Donate-PayPal-green.svg?logo=paypal&style=flat-square" alt="PayPal Donation"/></a> -->
</div>

SMELT is a framework and library for validating the legitimacy of social media content. The framework is design to be modular and highly compatible with existing libraries. The door is open for data analysis, machine learning, and image recognition.

## Reasoning
It is widely known that automated journalism and social media manipulation is a problem. There are tools to "fact check" content, but those tools are not enough. Posts that are supposed to be light-hearted contain fake media to increase viewership and retention. However, many people cannot tell fake from reality. Even if the fake media is obvious, there needs be a notice for manipulation. This project is my attempt to fix a global issue without changing too much.

## Disclaimer
I am not responsible for how this library is used. Nor am I responsible for modules created by the community.

## Goals
I hope to provide a robust modular Python framework while keeping the end-user in mind. I want to make it as easy as possible for developers of all skill levels to spot fake media. I hope to build a strong, stable community around the framework to increase the awareness of this global issue.
## Donations
I do not want to sell this product. I believe every one should have the right to determine truth from reality. That being said, I work a full time job and have other projects that I maintain. Donating to this project will inspire me to improve this project and our online world.

## Installation
```buildoutcfg
pip install smelt
```

## Classes
All classes are independent. Users should inherit base classes to expand functionality.

#### Store
Stores cache data used inside validation. Files, memory, and databases are all types of stores. Stores should work the same no matter where data is kept.

#### Validation
Validations parse and validate Detection data. They may use external sources such as databases or web APIs to validate data.

#### Recognition
Recognitions take an image buffer and spit out a string and the confidence of the black box operation. This class may be used to abstract pattern recognition, character recognition, or something else.

#### Enhancement
Enhancements take an image buffer, perform manipulations, and spit out a new image buffer. The goal is to increase the confidence of recognition strategies. They may be as simple as increasing the contrast, or they may block out useless pieces of media.

#### Buffer (BytesIO)
Enhancements, Recognitions, and Validations all modify an image buffer. The buffer is a BytesIO instance. However, a custom Buffer can be created by inheriting from BytesIO. This is useful for exporting data to BytesIO. Common buffer types will be auto-converted to BytesIO when passed to SMELT classes.