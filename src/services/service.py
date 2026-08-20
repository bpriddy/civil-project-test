"""service: describe what this step does.

The canvas reads this file, not a config. The handler's signature is the
node's contract -- rename anything, and the ports follow the code.
"""
from typing import TypedDict


class Input(TypedDict):
    value: str


class Output(TypedDict):
    value: str


def handler(data: Input) -> Output:
    return {"value": data["value"]}
