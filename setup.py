import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

    __version__ = "0.0.0"

    REPO_NAME = "Text-Summarizer-Project"
    AUTHOR_USER_NAME = "Jonathan"
    SRC_REPO = "textSummarizer"
    AUTHOR_EMAIL = "ivvi4coolpad@gmail.com"

    setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="A text summarization tool using the Transformers library. A small python package for NLP app",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        packages=setuptools.find_packages(where="src"),
        package_dir={"": "src"},
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        # python_requires=">=3.6",
        # install_requires=[
        #     "transformers==4.18.0",
        #     "torch==1.10.0",
        #     "torchvision==0.11.1",
        # ]
    )