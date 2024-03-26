
# Import necessary module
import setuptools

# Read the long description from the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define project details
__version__ = "0.0.0"
REPO_NAME = "EasyScan-LungDetect-AIOps-Sentinel--ML-FLow-DVC"
AUTHOR_USER_NAME = "FasilHameed"
SRC_REPO = "EasyScan"
AUTHOR_EMAIL = "faisalhameed763@gmail.com"

# Set up the project using setuptools
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for cancer detection using CNN",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
