"""
grep -Po "^TOTAL.*\\s+(\\d+\\%)$" test_result.log
"""

from tkinter import Button, Tk
from sys import exit
import re


def popupError(s):
    with open("test_result.log", "r") as fh:
        lines = fh.readlines()

    test_report = "\n".join(lines)
    _ = re.match(r"^TOTAL.*\s+(\d+%)$", test_report, flags=re.MULTILINE)
    total_converage = "95%"
    # TODO/optional: color if coverage is less than 90%
    # if code is removed we have the feedback that it is not working
    # Q: is this fast enough if we create a new TK process all the time?
    # Optional: watch for changes; socket
    # Q: can we display coverage directly in VSCode?
    # Q: is it useful to display evolution of coverage over time?
    # Q: when do we revert? where is the threshold
    popupRoot = Tk()
    popupRoot.after(500, exit)
    popupButton = Button(
        popupRoot, text=total_converage, font=("Verdana", 12), bg="yellow", command=exit
    )
    popupButton.pack()
    popupRoot.geometry("400x50+700+500")
    popupRoot.mainloop()


if __name__ == "__main__":
    popupError("bla bla")
