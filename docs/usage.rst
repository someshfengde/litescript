=====
Usage
=====

To use LiteScript in a project:
--------------------------------

.. code-block:: python

    # imports all the essentials for scripting (setup_logger, tqdm, os, glob, sys, etc.)
    from litescript import *

    # sets up a logger with a default format and level
    logger = setup_logger()

    logger.debug("This is a debug message")

    # listing out directories
    for dir in glob.glob("*"):
        logger.info(f"Found directory: {dir}")

    # using tqdm for progress bars
    for i in tqdm(range(10)):
        time.sleep(0.1)

    # pretty print with emojis with help of rich
    rprint("Hello, World! :world: :")



Get data science related imports:
----------------------------------

.. code-block:: python
    
    # imports all the essentials for data science (pandas, numpy, setup logger, tqdm, much more.)
    from litescript.data_science import * 


Get vis related imports :
--------------------------

.. code-block:: python
    
    from litescript.vis_utils import * # imports all the essentials for visualization (matplotlib, plotly etc.)
    
    # directly start plotting 
    fig = px.line(x=[1, 2, 3], y=[1, 3, 2])
    fig.show()

    # another matplotlib figure 
    fig = plt.figure()
    plt.plot([1, 2, 3], [1, 3, 2])
    plt.show()


Detailed imports available
--------------------------

::

   from litescript import * 

- setup_logger (colored logger with file handler at app.log)
- os 
- time
- sys
- json
- Path
- datetime
- tqdm
- glob
- yaml
- Console (rich console) 
- Table (rich table)
- rprint (rich print) 
- vis_utils
- data_science

::

   from litescript.data_science import *

- np
- pd
- setup_logger (colored logger with file handler at app.log)
- os
- sys
- json
- Path
- datetime
- tqdm
- glob
- yaml
- Console (rich console)
- Table (rich table)
- rprint (rich print)

::

   from litescript.vis_utils import *

- plt (matplotlib pyplot)
- px  (plotly express)