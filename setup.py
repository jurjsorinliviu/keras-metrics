import keras_metrics
import os
import setuptools


long_desctipion = """\
This package provides metrics for evaluation of Keras classification models. The
metrics are safe to use for batch-based model evaluation.
"""

setuptools.setup(
    name="keras-metrics",
    version=keras_metrics.__version__,

    long_desctipion=long_description,
    long_description_content_type="text/markdown",
    description="Metrics for Keras model evaluation",

    url="https://github.com/netrack/keras-metrics",
    author="Yasha Bubnov",
    author_email="girokompass@gmail.com",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords="keras metrics evaluation",

    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=["Keras>=2.1.5"],
)
