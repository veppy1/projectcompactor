# setup.py

import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="projectcompactor",
    version="0.2.0",  # Incremented version due to enhancements
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to generate a project tree and extract file contents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/projectcompactor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "tqdm>=4.0.0",
    ],
    entry_points={
        'console_scripts': [
            'projectcompactor=projectcompactor.generator:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
