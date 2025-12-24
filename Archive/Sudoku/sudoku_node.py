from typing import Optional
from random import randrange

class SudokuNode:

    def __init__(self, idx: int, value: Optional[int] = 0):
        self._idx = idx
        self._value = value
        self._display = False
        self._connectedTo = set()

    def getIndex(self) -> int:
        return self._idx

    def getValue(self) -> int:
        return self._value

    def setValue(self, newValue: int) -> bool:
        assert (
            newValue > 0 and newValue <= 9
        ), f"SudokuNode {self._idx}'s value cannot be set to a value other than 1-9"

        for node in self._connectedTo:
            if node.getValue() == newValue:
                return False

        self._value = newValue
        return True

    def resetValue(self) -> None:
        self._value = 0
        
    def getDisplay(self) -> bool:
        return self._display
    
    def setDisplay(self, newDisplay) -> None:
        self._display = newDisplay

    def getEdges(self) -> set["SudokuNode"]:
        return self._connectedTo.copy()

    def addEdge(self, node: "SudokuNode") -> None:
        self._connectedTo.add(node)

    def removeEdge(self, node: "SudokuNode") -> None:
        self._connectedTo.remove(node)

    def hasEdge(self, node: "SudokuNode") -> bool:
        return node in self._connectedTo
    
    def isValid(self) -> bool:
        if self._value == 0:
            return True
        
        for node in self._connectedTo:
            if node.getValue() == self._value:
                return False
        return True
    
    def reset(self) -> None:
        self._value = 0
        self._display = False

    def __str__(self):
        allConnections = list(self._connectedTo)
        allConnections.sort()
        return (
            "Node "
            + str(self._idx)
            + f" [{self.value}] -"
            + " Connected to: "
            + str(allConnections)
        )
