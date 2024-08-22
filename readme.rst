==========
LiteScript
==========
.. image:: https://github.com/someshfengde/litescript/blob/main/docs/logo.png

.. image:: https://img.shields.io/pypi/v/litescript.svg
        :target: https://pypi.python.org/pypi/litescript


.. image:: https://app.travis-ci.com/someshfengde/litescript.svg
    :target: https://app.travis-ci.com/someshfengde/litescript


.. image:: https://readthedocs.org/projects/litescript/badge/?version=latest
        :target: https://litescript.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://img.shields.io/pypi/dm/litescript
     :target: https://litescript.readthedocs.io/
     :alt: Updates



Utility package for streamlined Python scripts with logging, common imports, and essential utilities


* Free software: MIT license
* Documentation: https://litescript.readthedocs.io.

.. image:: https://github.com/someshfengde/litescript/blob/main/docs/litescript_demo.gif


Quickstart
----------

To use LiteScript in a project::

    # imports all the essentials for scripting (setup_logger, tqdm, os, glob, sys etc.)
    from litescript import *  

    # sets up a logger with a default format and level
    logger = setup_logger()  

    logger.debug("This is a debug message")

    # listing out directories 
    for dir in glob("*"):
        logger.info(f"-- Found directory: {dir}")

    # using tqdm for progress bars
    for i in tqdm(range(10)):
        logger.info("hii")
        time.sleep(0.1)

    # preety print with emojis with help of rich 
    rprint("Hello, World! :earth_asia:")
    # Hello, World! 🌏


Get data science related imports::

    # imports all the essentials for data science (pandas, numpy, setup logger, tqdm, much more.)
    from litescript.data_science import * 


Get vis related imports ::

    from litescript.vis_utils import * # imports all the essentials for visualization (matplotlib, plotly etc.)
    
    # directly start plotting 
    fig = px.line(x=[1, 2, 3], y=[1, 3, 2])
    fig.show()

    # another matplotlib figure 
    fig = plt.figure()
    plt.plot([1, 2, 3], [1, 3, 2])
    plt.show()



Features
--------

* can more workflows for simplification can be added here? if someone uses lmk will add those too. 😊
