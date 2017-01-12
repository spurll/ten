Ten
===

A lazy terminal implementation of 2048.

Usage
=====

Installation
------------

**TODO**

Requirements
------------

* `curses` (included with Python 3.5 on \*nix systems)

Because `curses` is not included on Windows distributions of Python, Windows
users may want to run `ten` in Cygwin (or maybe [bash for Windows](http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)
would work). Alternatively, you can make a go of it with one of the
several `curses` implementations available for Windows.

Basic Usage
-----------

**TODO**: The following assumes it's installed with setuptools/pip:

Once installed, run `ten`.

Bugs and Feature Requests
=========================

Feature Requests
----------------

* Ability to actually resize the grid from the command line
* Ability to restart a completed game with `ENTER`
* For win and loss messages, replace the logo with `WIN` or `LOSS`
* Simultaneous head-to-head race modes!
    1. Race: Both have the same seed for their random tiles. Who can finish first?
    2. Battle: You only get a new tile when you have no available moves or when the
       other player combines two tiles.

Known Bugs
----------

* Doesn't check for losses

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).
