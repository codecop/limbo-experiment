"""
Testing Tkinter Application

Testing a Tkinter application is not immediately possible, as the
event loop (`mainloop` in Tkinter) blocks the execution of other code,
in particular test code.

Running the event loop and the tests in separate threads does not appear
trivial.

However, instead of running the application through the event loop,
one can manually trigger updates (pump events) throughout the test case and thereby
run both the app as well as the test in the same thread.

Below example is based on this discussion on SO:
https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app

Not sure the details of `pump_events`.
"""
import os
import tkinter as tk
import _tkinter
import sys
import unittest

import pytest


# https://docs.github.com/en/actions/learn-github-actions/environment-variables#default-environment-variables
# If GITHUB_ACTION is set, we assume we run in a container and can not service user events
skipifcontainer_because_event_handling_not_working = pytest.mark.skipif(
    bool(os.environ.get("GITHUB_ACTION")), reason="Test executed within GitHub action."
)


class TkinterTestCase(unittest.TestCase):
    """Utility class to facilitate setup, teardown as well as manual GUI updates."""

    def setUp(self):
        if sys.platform.startswith('linux') and not os.environ.get("DISPLAY", False):
            self.skipTest(
                "No $DISPLAY environment variable. Cannot run Tk without (virtual) display."
            )

        self.root = tk.Tk()
        self.pump_events()

    def update_gui(self):
        """Utility method to update application"""
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.pump_events()
            self.root.destroy()

    def pump_events(self):
        while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass
