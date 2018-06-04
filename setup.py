from setuptools import setup, find_packages

setup(
    name='jovian',
    version='0.0.0',
    description='a window on jupyter',
    author='W. Lee Pang',
    license='Apache-2',
    packages=find_packages(),
#    install_requires=[
#        'pyqt',
#        'jupyterlab'
#    ],
    scripts=[
        'bin/jovian',
        'jovian/jovian.py'
    ],
    zip_safe=False
)
