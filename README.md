# Jovian

A simple python/Qt wrapper to launch JupterLab in a stand-alone window


## Requirements

* pyqt 5.9+
* jupyter 1.0.0+
* notebook 5.5.0+
* jupyterlab 0.32+


## Installation

This code was tested using the Anaconda distribution which ships with many of the
underlying dependencies for jupyterlab.

```bash
git clone https://github.com/wleepang/jovian
pip install ./jovian
```


## Usage

Simply type the following:

```bash
$ jovian
```

and a webview window with Jupyter Lab will launch.

This window is independent of your default installed web browser.


### Caveats

The jupyter server started at launch is automatically terminated when the webview window is closed.
This assumes only one jupyter application server is running at any given time.

