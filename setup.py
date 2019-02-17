from setuptools import setup

setup(name='pypairwisemap',
      version='0.8',
      description='Python utility for pairwise mapping of atomic spacing to represent protein structures in 2D',
      url='https://github.com/kanxx030/pdb-pairwise-mapping',
      author='Chi Nok Enoch Kan',
      author_email='kanxx030@gmail.com',
      license='MIT',
      packages=['pypairwisemap'],
      install_requires=[
          'biopython','numpy','matplotlib'
      ],
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      zip_safe=False)