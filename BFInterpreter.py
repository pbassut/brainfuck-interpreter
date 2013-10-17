import sys
import re


class Interpreter():
    def __init__(self, program_str, output=False):
        self.program_str = re.compile(r'\s+').sub('', program_str)
        self.cell_table = []
        self.cell_pointer = 0
        self.eip = 0
        self.stack_pointer = []
        self.interpret()

        if output:
            self.output()

    def alloc(self):
        # create room for the next cell
        if len(self.cell_table) > 30000:
            raise MemoryError('Out of memory!')

        self.cell_table.append(0)

    def cell(self):
        if len(self.cell_table) <= self.cell_pointer:
            self.alloc()

        return self.cell_table[self.cell_pointer]

    def set_cell(self, value):
        self.cell()
        self.cell_table[self.cell_pointer] = value

    def inc(self):
        self.set_cell(self.cell() + 1)

    def dec(self):
        self.set_cell(self.cell() - 1)

    def next_row(self):
        self.cell_pointer += 1

    def prev_row(self):
        self.cell_pointer -= 1

    def navigate_to(self, x):
        self.eip = x

    def command_issuer(self):
        while 1:
            if self.eip < len(self.program_str):
                yield self.program_str[self.eip]
            else:
                break

    def loop_end(self):
        return self.program_str.find(']', self.eip)

    def loop_begin(self):
        return self.program_str.find('[', 0, self.eip)

    def interpret(self):
        for command in self.command_issuer():
            if command == '+':
                self.inc()

            elif command == '-':
                self.dec()

            elif command == '>':
                self.next_row()

            elif command == '<':
                self.prev_row()

            elif command == '.':
                try:
                    print chr(self.cell())
                except ValueError:
                    print 'Value %d not found in ASCCI table' % self.cell()

            elif command == ',':
                self.set_cell(int(sys.stdin.read(3)))

            elif command == '[':
                if self.cell() == 0:
                    self.navigate_to(self.loop_end())
                else:
                    self.stack_pointer.append(self.eip)

            elif command == ']':
                if self.cell() == 0:
                    self.stack_pointer.pop()
                else:
                    self.navigate_to(self.stack_pointer[len(self.stack_pointer) - 1])

            self.eip += 1

    def output(self):
        print '\nOutput: '
        for index, each in enumerate(self.cell_table, 1):
            print 'Cell #%d: %s ' % (index, each)


interpreter = Interpreter('++++++ [ > ++++++++++ < - ] > +++++ .', True)