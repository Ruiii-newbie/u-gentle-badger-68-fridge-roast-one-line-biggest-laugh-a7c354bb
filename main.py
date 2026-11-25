#!/usr/bin/env python3
"""Fridge Roast entry: one line (<=200 chars) roasting a smart fridge.

The joke targets the fridge's firmware update bricking the ice maker:
the punchline is the deadpan "error 404: ice not found" while the
drink warms up — specific to smart fridges, no grocery-ordering or
surveillance crack.
"""
import os

LINE = (
    "My smart fridge's firmware update bricked the ice maker — now it "
    "blinks 'error 404: ice not found' while my drink slowly gives up "
    "on being cold."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
