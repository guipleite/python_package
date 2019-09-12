from setuptools import setup

setup(name='my_hello_guilhermepl3',
      version='0.1',
      packages=['my_hello'],
      author='Guilherme Leite',
      python_requires='>=3.6',
      platforms=['posix', 'nt'],
      install_requires=[
          'numpy'
      ],
      scripts=['scripts/hello.py']
     )