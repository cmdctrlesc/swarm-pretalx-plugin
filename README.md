Pretalx plugin for exporting the agenda to Swarm
==========================

This is a plugin for `pretalx`_. 

Installation
-----------------

pip install swarm-pretalx




Requirements
-----------------

This plugin uses the Github api to post data to Swarm. You will need write access to this repository https://github.com/datafund/web_devconagenda as well as your Github credentials.
Credentials need to be put in an .env file as follows:

GITHUB_TOKEN = mytokenstring
GITHUB_USERNAME = 'My Github Name'
GITHUB_EMAIL = 'mygithub@email.com'

The plugin will look for the .env file in the Swarm-plugin directory, which is the directory that also contains setup.py, Makefile etc. 


Development setup
-----------------

1. Make sure that you have a working `pretalx development setup`_.

2. Clone this repository, eg to ``local/swarm-plugin``.

3. Activate the virtual environment you use for pretalx development.

4. Execute ``pip install -e .`` within this directory to register this application with pretalx's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretalx server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

Copyright 2022 cmdctrlesc

Released under the terms of the Apache License 2.0


.. _pretalx: https://github.com/pretalx/pretalx
.. _pretalx development setup: https://docs.pretalx.org/en/latest/developer/setup.html
