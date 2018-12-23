import sys


def solve(io):
	A = io.read_int()
	B = io.read_int()

	io.println(A + B)


# +---------------------+
# | TEMPLATE CODE BELOW |
# |    DO NOT MODIFY    |
# +---------------------+


class IO:
	in_stream = None
	out_stream = None
	raw = ""
	buf = []
	pos = 0

	def __init__(self, input_stream, output_stream):
		self.in_stream = input_stream
		self.out_stream = output_stream

	def read_to_buffer(self):
		self.raw = self.in_stream.readline().rstrip('\n')
		self.buf = self.raw.split()
		self.pos = 0

	def read_string(self):
		while self.pos == len(self.buf):
			self.read_to_buffer()
		ans = self.buf[self.pos]
		self.pos += 1
		return ans

	def read_int(self):
		return int(self.read_string())

	def read_float(self):
		return float(self.read_string())

	def read_string_array(self, N, offset=0):
		arr = [None] * offset
		for _ in range(0, N):
			arr.append(self.read_string())
		return arr

	def read_int_array(self, N, offset=0):
		arr = [None] * offset
		for _ in range(0, N):
			arr.append(self.read_int())
		return arr

	def read_float_array(self, N, offset=0):
		arr = [None] * offset
		for _ in range(0, N):
			arr.append(self.read_float())
		return arr

	def read_line(self):
		while self.pos == len(self.buf):
			self.read_to_buffer()
		if self.pos > 0:
			raise ValueError("Cannot call read_line in the middle of a line.")
		self.pos = len(self.buf)
		return self.raw

	def print(self, *args):
		self.out_stream.write(' '.join([str(x) for x in args]))

	def println(self, *args):
		self.print(*args)
		self.print('\n')

	def println_array(self, arr, sep=' '):
		self.println(sep.join(str(x) for x in arr))

	def flush_output(self):
		self.out_stream.flush()


pythonIO = IO(sys.stdin, sys.stdout)
solve(pythonIO)
pythonIO.flush_output()
