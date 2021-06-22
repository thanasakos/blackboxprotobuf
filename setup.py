import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')
req = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()
req = [x.strip() for x in req if x.strip()]

setuptools.setup(
    name="blackboxprotobuf",
    version="1.0.0",
    author="Athanasios Andreou, Forked from Yogesh Khatri",
    author_email="athan.andreou@gmail.com",
    description="Library for reading protobuf buffers without .proto definitions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thanasakos/blackboxprotobuf",
    packages=setuptools.find_packages(),
    install_requires=req,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT License",
)