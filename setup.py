from setuptools import setup

setup(name='hoerapi',
      version='1.3',
      description='hoerapi in python',
      author='luto',
      author_email='m@luto.at',
      license='MIT',
      url='https://github.com/hoersuppe/hoerapi.py',
      packages=['hoerapi'],
      install_requires=[
       'requests', 'pytz',
      ],
     )
