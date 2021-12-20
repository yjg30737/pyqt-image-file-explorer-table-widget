from setuptools import setup, find_packages

setup(
    name='pyqt-image-file-explorer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt image file explorer',
    url='https://github.com/yjg30737/pyqt-image-file-explorer.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)