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
import tkinter as tk
import _tkinter
import unittest


class TkinterTestCase(unittest.TestCase):
    """Utility class to facilitate setup, teardown as well as manual GUI updates."""

    def setUp(self):
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
