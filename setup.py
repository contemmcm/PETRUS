from setuptools import setup

setup(name='petrus',
      version='0.1',
      description='Online automatic phonetic transcription system for Brazilian Portuguese',
      url='https://github.com/contemmcm/PETRUS',
      author='Alessandro Bokan',
      author_email='abokan@gmail.com',
      packages=['petrus', 'petrus.g2p', 'petrus.stress', 'petrus.syllables'],
      zip_safe=False)
