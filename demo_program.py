# Demo program which writes to PRU, waits for event from PRU
# Print result written back PRU.
# This program is only meant to show how the userspace program
# may look like after the project is complete. This program
# will not compile.
import pruss_lib as pru

print "Initializing PRU"
pru.init()

print "Loading PRU and begin execution"
pru.load(0,/path/to/firmware)

print "Write 1234 to memory"
pru.data_write('DDR','1234')

print "Wait for event from PRU"
while(pru.event_receive())

print "Print received data"
print pru.data_read()