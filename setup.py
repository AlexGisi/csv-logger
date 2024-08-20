from setuptools import setup, find_packages

setup(
    name='csv_logger',                   # Name of your package
    version='0.1',                       # Version number
    description='A simple CSV logger',   # Short description of your package
    author='Your Name',                  # Your name
    author_email='your.email@example.com', # Your email
    packages=find_packages(),            # Automatically find packages in the directory
    include_package_data=True,           # Include additional files specified in MANIFEST.in
    install_requires=[                   # List of dependencies
        # 'numpy',  # Example dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',             # Minimum Python version requirement
)
