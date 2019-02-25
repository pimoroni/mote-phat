|Mote| https://shop.pimoroni.com/products/mote-phat

Drive four channels of APA102 pixels from your Raspberry Pi or Pi Zero
with Mote pHAT

Installing
----------

Full install (recommended):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've created an easy installation script that will install all
pre-requisites and get your Mote pHAT up and running with minimal
efforts. To run it, fire up Terminal which you'll find in Menu ->
Accessories -> Terminal on your Raspberry Pi desktop, as illustrated
below:

.. figure:: http://get.pimoroni.com/resources/github-repo-terminal.png
   :alt: Finding the terminal

In the new terminal window type the command exactly as it appears below
(check for typos) and follow the on-screen instructions:

.. code:: bash

    curl https://get.pimoroni.com/motephat | bash

Alternatively, on Raspbian, you can download the ``pimoroni-dashboard``
and install your product by browsing to the relevant entry:

.. code:: bash

    sudo apt-get install pimoroni

(you will find the Dashboard under 'Accessories' too, in the Pi menu -
or just run ``pimoroni-dashboard`` at the command line)

If you choose to download examples you'll find them in
``/home/pi/Pimoroni/motephat/``.

Manual install:
~~~~~~~~~~~~~~~

Library install for Python 3:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

    sudo apt-get install python3-motephat

other environments:

.. code:: bash

    sudo pip3 install motephat

Library install for Python 2:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

    sudo apt-get install python-motephat

other environments:

.. code:: bash

    sudo pip2 install motephat

Development:
~~~~~~~~~~~~

If you want to contribute, or like living on the edge of your seat by
having the latest code, you should clone this repository, ``cd`` to the
library directory, and run:

.. code:: bash

    sudo python3 setup.py install

(or ``sudo python setup.py install`` whichever your primary Python
environment may be)

In all cases you will have to enable the i2c bus.

Documentation & Support
-----------------------

-  Guides and tutorials - https://learn.pimoroni.com/mote-phat
-  Function reference - http://docs.pimoroni.com/motephat/
-  GPIO Pinout - https://pinout.xyz/pinout/mote\_phat
-  Get help - http://forums.pimoroni.com/c/support

.. |Mote| image:: mote-logo.png

