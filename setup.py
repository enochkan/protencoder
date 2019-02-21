from setuptools import setup

setup(name='protencoder',
      version='0.9',
      description='Python utility to implement various encoding methods for protein structures',
      url='https://github.com/kanxx030/protencoder',
      author='Chi Nok Enoch Kan',
      author_email='kanxx030@gmail.com',
      license='MIT',
      packages=['protencoder'],
      install_requires=[
          'biopython','numpy','matplotlib'
      ],
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      zip_safe=False)