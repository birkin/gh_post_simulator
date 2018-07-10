Purpose
=======

For a couple of projects, we have a 'listener' web-app set up to be hit by a github message when a (data) repository is updated.

It's nice to be able to test these without actually having to change real data, or resubmit real data.

This code does that.

Run like this:

        cd /path/to/project/; source ../env/bin/activate; ../env/bin/python3 ./post_simulator.py

---
