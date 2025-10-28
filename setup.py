from setuptools import setup
import os


def readme():
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(parent_dir, "README.md")) as f:
        return f.read()


setup(
    name="chart-studio",
    version="2.0.0",
    author="Chris P",
    author_email="chris@plot.ly",
    maintainer="Plotly Libraries Team",
    maintainer_email="community@plot.ly",
    url="https://plot.ly/",
    project_urls={
        "Deprecated": "https://github.com/plotly/chart-studio/blob/main/README.md",
        "Github": "https://github.com/plotly/chart-studio"
    },
    description="DEPRECATED: utilities for interfacing with Plotly's Chart Studio",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    license="MIT",
    packages=[
        "chart_studio",
        "chart_studio.api",
        "chart_studio.api.v2",
        "chart_studio.dashboard_objs",
        "chart_studio.grid_objs",
        "chart_studio.plotly",
        "chart_studio.plotly.chunked_requests",
        "chart_studio.presentation_objs",
    ],
    install_requires=["plotly", "requests", "retrying>=1.3.3"],
    zip_safe=False,
)
