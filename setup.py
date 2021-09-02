import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='OSRS-Hiscores',  
    version='0.6',
    author="Matthew Thornton",
    author_email="osrsbotdetector@gmail.com",
    description="An Old School Runescape (OSRS) Hiscores Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThorntonMatthewD/osrs-hiscores",
    packages=setuptools.find_packages(include=['OSRS_Hiscores']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)