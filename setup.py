from setuptools import setup, find_packages

setup(
    name='pyqt-image-file-explorer-table-widget',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QTableWidget for image file explorer',
    url='https://github.com/yjg30737/pyqt-image-file-explorer-table-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)