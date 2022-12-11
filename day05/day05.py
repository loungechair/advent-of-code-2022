import copy
import re

from dataclasses import dataclass
from itertools import islice

FILE = "input.txt"


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


def load_input(filename):
    initial_state = {i: [] for i in range(1, 10)}
    instructions = []

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


class FirstSimulation:
    def __init__(self, initial_state):
        self.state = copy.deepcopy(initial_state)

    def _process_instruction(self, instruction):
        for i in range(instruction.count):
            self.state[instruction.target].append(self.state[instruction.source].pop())

    def run(self, instructions):
        for inst in instructions:
            self._process_instruction(inst)

    def get_state(self):
        return ''.join([crates[-1] for _, crates in self.state.items()])


class SecondSimulation:
    def __init__(self, initial_state):
        self.state = copy.deepcopy(initial_state)

    def _process_instruction(self, inst):
        self.state[inst.target].extend(self.state[inst.source][-inst.count:])
        self.state[inst.source] = self.state[inst.source][:-inst.count]

    def run(self, instructions):
        for inst in instructions:
            self._process_instruction(inst)

    def get_state(self):
        return ''.join([crates[-1] for _, crates in self.state.items()])

if __name__ == '__main__':
    state, instructions = load_input(FILE)

    sim1 = FirstSimulation(state)
    sim1.run(instructions)
    print(sim1.get_state())

    sim2 = SecondSimulation(state)
    sim2.run(instructions)
    print(sim2.get_state())
