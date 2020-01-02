"""The primary graphical user interface used to 
control and run experiments.

Example:
    From command line::

        $ python reach_master.py

Todo:
    * Create executable

"""

if __name__ == '__main__':
	import reachmaster.application as app
	rm = app.ReachMaster()
	rm.run()