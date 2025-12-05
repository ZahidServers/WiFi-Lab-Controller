from setuptools import setup, find_packages

setup(
    name="wifilab",
    version="1.0.0",
    py_modules=["app"],
    author="Mohammed Zahid Wadiwale",
    author_email="support@webaon.com",
    description="Wi-Fi Lab Controller: Safe WiFi testing toolkit with scanning, fake AP, DNS redirection.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZahidServers/WiFi-Lab-Controller",
    license="GPL-3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    install_requires=[],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "wifilab=WiFi-Lab-Controller.app:main"
        ]
    },
)
