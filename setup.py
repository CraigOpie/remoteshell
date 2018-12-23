import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="remoteShell",
    version="1.0.0",
    author="Craig Opie",
    author_email="craigopie@gmail.com",
    description="A reverse shell used to connect the client to a server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CraigOpie/remoteShell",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
