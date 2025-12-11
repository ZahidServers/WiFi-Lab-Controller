from setuptools import setup, find_packages

setup(
    name="wifilab",
    version="1.1.2",
    packages=find_packages(),
    author="Mohammed Zahid Wadiwale",
    author_email="info@webaon.com",
    description="Wi-Fi Lab Controller: Safe WiFi testing toolkit with scanning, fake AP, DNS redirection.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZahidServers/WiFi-Lab-Controller",
    license="BSD-3-Clause",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    install_requires=[],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "wifilab=wifilab.app:main"
        ]
    },
)
