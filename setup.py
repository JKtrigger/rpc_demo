import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="chat",
    version="0.0.1",
    author="Maxim",
    author_email="",
    description="Package to create chat",
    long_description="",
    long_description_content_type="text/markdown",
    packages=["chat/proto"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Maksim Nalimov Approved :: SELF License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.16',
)
