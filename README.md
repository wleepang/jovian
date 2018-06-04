# Jovian

A simple python/Qt wrapper to launch JupterLab in a stand-alone window


## Requirements

* pyqt 5.9+
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

Closing the window does not automatically shut down the jupyter kernel server.
You will need to do this manually in the terminal with keyboard interrupts (i.e. <kbd>ctrl+c</kbd>).

This functionality is pending upcoming REST API changes to jupyter.

