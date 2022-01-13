import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="photolapse",  # Replace with your own username
    version="1.0.0",
    author="Matthieu Totet",
    author_email="matthieu.totet@gmail.com",
    description="Generate a composition pictures from a set of timelapse pictures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["itg = intervallographie.__main__:run"]},
    install_requires=["Pillow==9.0.0", "numpy==1.18.1"],
)
