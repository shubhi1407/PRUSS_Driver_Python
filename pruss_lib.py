# Python library to communicate with PRUSS Kernel Driver
# This piece of code gives a brief demostration of how the python
# wrapper will be implemented. This code is only meant for demostration
# and neither it is complete nor will it compile.
# Similar libraries can be easily written for Javascript, C, C++.
PAGE_SIZE =	4096
HOME =	"/sys/class/remoteproc/pru/"
DATA_FILE_W            =	HOME + "pru_data_w"
MEMTYPE_FILE		   =	HOME + "pru_memtype"
DATA_FILE_R            =	HOME + "pru_data_r"
EXEC_FILE 	           =	HOME + "pru_load_firmware"
INIT_FILE 	           =	HOME + "pru_initialize"
STATUS_FILE            =	HOME + "pru_status"
RESET_FILE     		   =	HOME + "pru_reset"
EVENT_SEND_FILE        =	HOME + "pru_send_event"
EVENT_RECEIVE_FILE     =	HOME + "pru_recv_event"

def pruss_init():
	'''
	Write 1 to INIT_FILE to initialise pru
	'''
	with open(INIT_FILE, "w") as f:
	f.write('1')


def pruss_load(pru_num, filename):
	'''
	pass path to firmware as argument
	'''
	with open(filename, "r") as f:
		lines = f.readlines()
	    f.close
	
	with open(EXEC_FILE, "w") as f:
		f.write(pru_num)
		f.writelines(lines)	


def pruss_status(num):
	'''
	Write 1 to STATUS_FILE to resume pru and 0 to halt pru
	'''
	with open(STATUS_FILE, "w") as f:
	f.write(num)


def pruss_reset():
	'''
	Call this function to reset pru
	'''
	with open(RESET_FILE, "w") as f:
	f.write('0')


def pruss_event_send(event_num):
	'''
	Write event num to file
	'''
	with open(EVENT_SEND_FILE, "w") as f:
	f.write(event_num)


def pruss_event_receive():
	'''
	Read event num from file
	'''
	with open(EVENT_RECIEVE_FILE, "r") as f:
		print f.read()
		return f.read()

def pruss_data_write(mem_type,data,address):
	'''
	Write data to specified memory. address is optional
	'''
	with open(MEMTYPE_FILE, "w") as f:
		f.write(mem_type)
	    f.close()
	with open(DATA_FILE_W, "w") as f:
		f.write(data)
	    f.close()

def pruss_data_read(data,address):
	'''
	Read data from pru. address is optional
	'''
	with open(DATA_FILE_R, "r") as f:
		return f.read()
	    f.close()