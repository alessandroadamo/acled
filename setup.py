import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alessandroadamo",
    version="0.1.0",
    author="Alessandro Adamo",
    author_email="alessandro.adamo@gmail.com",
    description="The Armed Conflict Location & Event Data Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alessandroadamo/acled",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
