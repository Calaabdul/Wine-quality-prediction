from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Wine-quality-prediction"
AUTHOR_USER_NAME = "Calaabdul"
AUTHOR_EMAIL = "ajidagba19@gmail.com"
SRC_REPO = "mlProject"

setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = 'python package for mlops',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    packages = find_packages(where = "src"),
    package_dir = {"": "src"}
    )