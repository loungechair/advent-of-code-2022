import abc
import copy
import re
from dataclasses import dataclass
from itertools import islice
from typing import Dict, List, Tuple

FILE = "input.txt"

State = Dict[int, List[str]]

@dataclass
class MoveInstruction:
    source: int
    target: int
    count: int

    @staticmethod
    def from_string(command: str) -> "MoveInstruction":
        rematch = re.match(r'move (\d+) from (\d+) to (\d)+\n', command)
        c, s, t = [int(x) for x in rematch.groups()]
        return MoveInstruction(s, t, c)


def load_input(filename: str) -> Tuple[State, List[MoveInstruction]]:
    initial_state = {i: [] for i in range(1, 10)}

    with open(filename) as f:
        head = list(islice(f, 8))
        for row in reversed(head):
            for i in range(0, 9):
                crate = row[1 + 4 * i]
                if crate != ' ':
                    initial_state[i+1].append(crate)
        # skip two lines
        next(f)
        next(f)
        instructions = [MoveInstruction.from_string(s) for s in f]

    return initial_state, instructions

class Simulation(abc.ABC):
    def __init__(self, initial_state: State) -> None:
        self.state: State = copy.deepcopy(initial_state)

    @abc.abstractmethod
    def _process_instruction(self, inst: MoveInstruction) -> None:
        pass

    def run(self, instructions: List[MoveInstruction]) -> None:
        for inst in instructions:
            self._process_instruction(inst)

    def get_state(self) -> str:
        return ''.join([crates[-1] for _, crates in self.state.items()])


class FirstSimulation(Simulation):
    def __init__(self, initial_state: State) -> None:
        super().__init__(initial_state)

    def _process_instruction(self, inst: MoveInstruction) -> None:
        for i in range(inst.count):
            self.state[inst.target].append(self.state[inst.source].pop())


class SecondSimulation(Simulation):
    def __init__(self, initial_state: State) -> None:
        super().__init__(initial_state)

    def _process_instruction(self, inst: MoveInstruction):
        self.state[inst.target].extend(self.state[inst.source][-inst.count:])
        self.state[inst.source] = self.state[inst.source][:-inst.count]


if __name__ == '__main__':
    state, instructions = load_input(FILE)

    sim1 = FirstSimulation(state)
    sim1.run(instructions)
    print(sim1.get_state())

    sim2 = SecondSimulation(state)
    sim2.run(instructions)
    print(sim2.get_state())
