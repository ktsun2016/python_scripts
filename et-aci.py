#!/router/bin/python

import sys, os, string, getopt, telnetlib, time

devices = {

        'RL1'           : ['172.31.128.8', '2015', None],
        'RL2'           : ['172.31.128.8', '2013', None],
        'RS1'           : ['172.31.128.8', '2014', None],
        'L3OUT1'        : ['172.31.128.4', '2029', None],
	'L3OUT3'	: ['172.31.128.7', '2025', None],
	'L1'		: ['172.31.128.4', '2030', None],
	'L2'		: ['172.31.128.4', '2031', None],
	'L3OUT2'	: ['172.31.128.4', '2032', None],
	'L3'		: ['172.31.128.4', '2033', None],
	'L4'		: ['172.31.128.4', '2034', None],
	'L5'		: ['172.31.164.5', '2033', None],
        'S1'            : ['172.31.164.5', '2037', None],
	'L6'		: ['172.31.164.5', '2030', None],
	'L7'		: ['172.31.128.4', '2019', None],
        'T2S1'          : ['172.31.164.5', '2034', None],
        'T2L1'          : ['172.31.164.5', '2012', None],
        'T2L2'          : ['172.31.164.5', '2018', None],
        'T2L3OUT'       : ['172.31.164.5', '2021', None],
	'IPN'		: ['172.31.128.8', '2020', None],
	'S2S1'		: ['172.31.164.5', '2049', None],
	'S2'		: ['172.31.164.5', '2013', None],
        'S2L1'          : ['172.31.164.5', '2016', None],
        'S2L3'          : ['172.31.164.5', '2046', None],
	'S2L4'		: ['172.31.164.5', '2047', None],
	'PASA2'		: ['172.31.164.5', '2044', None],
	'PASA1'		: ['172.31.164.5', '2045', None],
        'PASA3'         : ['172.31.164.5', '2043', None],
        'PASA4'         : ['172.31.164.5', '2050', None],
        'PASA5'         : ['172.31.164.5', '2019', None],
        'PASA6'         : ['172.31.164.5', '2025', None],
        'S2SW'           : ['172.31.128.8', '2025', None],
        'S1SW'           : ['172.31.128.8', '2026', None],
        'S8'            : ['172.31.128.7', '2030', None],
        'P2L1'          : ['172.31.128.8', '2024', None],
        'P2L2'          : ['172.31.128.7', '2034', None],
        'P2L3'          : ['172.31.128.8', '2009', None],
        'IPN1'          : ['172.31.128.8', '2032', None],
        'IPN2'          : ['172.31.128.8', '2033', None],

        
        }





def usage():
	print "Syntax:", str(sys.argv[0]), "[opt] [<device_name> | <alias>]"
	print "\t-h, --help : prints this page"
	print "\t-l : lists all registered devices"
	print "\t-s : connect to device using terminal server"
	print "\t-t : connect to device using dirtnet connection"
	print "\t-c : clears line to device on terminal server"
	#print 
	#sys.exit(0)
def is_alias(device, verbose=1):
#def is_alias(device,):
	device = string.upper(device)
	print device
	print verbose
	if devices.has_key(device):
		# Direct match on key
		if verbose: print str(args[0]), 'found in device list ...'
		return device
	else:
		# Try to match an alias
		device_names = devices.keys()
		device_alias = []
		for name in device_names:
			device_alias.append(string.split(name, '-')[0])
		if device in device_alias:
			# Alias match found
			index = device_alias.index(device)
			if verbose: print str(device), 'is an alias for', str(device_names[index])
			return device_names[index]
		else:
			# No match, force exit
			print str(device), 'does not exist in device list ...'
			sys.exit(1)

def list():
	print "%15s%7s%15s%6s%15s" % ("device_name", "alias", "console_ip", "port", "dirtnet_ip")
	devs = devices.keys()
	devs.sort()
	for dev in devs:
		print "%15s%7s%15s%6s%15s" % (dev, string.split(dev, '-')[0], devices[dev][0], devices[dev][1], devices[dev][2])
	sys.exit(0)

def clearline(device):
	try:
		device = is_alias(device)
		print 'Clearing console line to', device
		telnetObj = telnetlib.Telnet(devices[device][0])
		#telnetObj.set_debuglevel(1)
		telnetObj.expect(["sername:"])
		telnetObj.write('admin\n')
		telnetObj.expect(["assword:"])
		telnetObj.write('insieme\n')
		telnetObj.expect(["#"])

		telnetObj.write('clear line ' + devices[device][1][2:] + '\n')
		telnetObj.expect(["[confirm]"])
		telnetObj.write('\n')
		telnetObj.expect(["#"])
		telnetObj.write('exit\n')
		del telnetObj
		time.sleep(2)
		connect(device, 'serial')
	except KeyError:
		print 'Device could not be found ...'
		sys.exit(1)

def connect(device, mode=None):
	device = is_alias(device)
	# Connect to device
	print 'Trying to connect to', str(device), '...'
	if mode == 'serial':
		print 'Opening console connection to', str(device), '...'
		#s = ' xterm -sb -sl 10000 -bg black -e telnet  ' + str(devices[device][0]) + ' ' + str(devices[device][1]) + ' & '
		#print s
		#os.system(s)
		os.system('  xterm -title ' + device + ' -fg green -bg black -sb -sl 10000 -e telnet ' + str(devices[device][0]) + ' ' + str(devices[device][1]) + '&')
		#sys.exit(0)
	elif mode == "telnet":
		if devices[device][2] == None:
			print 'Dirtnet connection not provisioned, exiting ...'
			sys.exit(1)
		else:
			print 'Opening telnet connection to', str(device), '...'
			os.system('xterm -title str(device) telnet ' + str(devices[device][2]))
			sys.exit(0)		
	else:
		print 'Unspecified connection method, exiting ...'
		sys.exit(1)

if __name__ == '__main__':
        shortopt = 'sthcl'
        longopt = ['help']
        try:
                optlist, args = getopt.getopt(sys.argv[1:], shortopt, longopt)
		print optlist
		print len(args)
		if len(optlist) == 0 and len(args) == 0:
			print 'empty option list ...'
			usage()
		if len(optlist) == 0 and len(args) == 1:
			connect(args[0], 'serial')
                for option in optlist:
                        if option[0] == '-h' or option[0] == '--help': 
				usage()
			elif option[0] == '-l':
				list()
			elif option[0] == '-c':
				print 'number of device is %s' % len(args)
				for i in range(len(args)): 
					print 'connecting the %s: %s' % (i, args[i] )
					clearline(args[i])
                        elif option[0] == '-t':
				connect(args[0], 'telnet')
                        elif option[0] == '-s': 
				connect(args[0], 'serial') 
        except getopt.error as err:
                print 'Invalid option, exiting ...'
		usage()
		sys.exit(1)

	#usage()
	sys.exit(0)
