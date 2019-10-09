from setuptools import setup
from setuptools import find_packages


setup(
    name='parallel_data_cleaning',
    version='1.0.0',
    description='Parallel data cleaning package',
    url='',
    author='Marina Fomicheva',
    author_email='',
    license='',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            'apply-classifier=parallel_data_cleaning.bin.apply_classifier:main',
            'extract-features=parallel_data_cleaning.bin.extract_features:main',
            'train-classifier=parallel_data_cleaning.bin.train_classifier:main',
            'generate-synthetic=parallel_data_cleaning.bin.generate_synthetic_data:main',
            'build-testset=parallel_data_cleaning.bin.build_testset:main',
        ]
    }
)
