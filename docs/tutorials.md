# Tutorials

Below you can find several tutorials illustrating various features of the CoastDef package. Each tutorial also discusses why the code works, and what it means. The tutorials are intended for people with little programing experience, so experience programmers might want to scroll through some of the explanations. The models and tutorials explored below use examples focused on Connecticut and the Long Island Sound, but the lessons they contain are transferable to other places in the US and around the world.

They are hosted in [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb), an online, hosted Jupyter notebook which allows you to collaborate with colleagues or partners. Jupyter notebooks allow you to mix text, mathematics, [Python](https://www.pythonforbeginners.com/learn-python/what-is-python/) code, and outputs in a single, self-contained document. Each Colab tutorial notebook will open in a new virtual machine, and you will have to install the dependencies on it before running the more interesting code. This should take less than a minute.

The tutorials are read-only files, but you can download a copy to your Google Drive and edit them to your heart's content. (If you are interested in contributing to the documentation, email [{{site.email}}](mailto:{{site.email}}) to get access.) All of this can be done in your browser, making it the easiest and quickest way to explore CoastDef's functionality. We would encourage you to use Colab for your own small to medium-sized projects, as a local install is often more of a hassle.

## [Using the Google Colab Environment](https://colab.research.google.com/drive/1_0oFoE9svyGNdtWJNRWvAowjIsnhreFx)

This tutorial offers an introduction to the Google Colab's notebook setup. We install the CoastDef package and its dependencies, and we show the user how to get files in and out of the Colab workspace. We briefly introduce some of the capacities of Python, as well as running Bash commands in a !bang format. Experienced programmers can probably skip this.

## Preprocessing Your Data

Here we import some sample project data from Bridgeport Connecticut. (For advice on acquiring data, see [Finding Data Sources](finding_data_sources.md). We combine parcel appraisals for and structure outlines to isolate building values, and use those building outlines to produce a "building free DEM." We to add wall data to the model, and use "water points" to calculate flooding extents for a certain elevation height. We use this to make a short video, showing how increasing storm surges will affect flooding in Bridgeport, with or without a coastal wall.

## Making a Model

Coming soon.

## Using Empirical Data in Your Models

When the library is sufficiently fleshed out, we will give several examples of several modeling methodologies. We will also supply toy data and an introductory discussion of [MCMC](https://twiecki.github.io/blog/2015/11/10/mcmc-sampling/).

