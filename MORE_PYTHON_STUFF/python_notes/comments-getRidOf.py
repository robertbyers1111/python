import re

lines = """

###
{dut:4500 dut1}
mode=standalone                # Mode {standalone | HA}

# Define the parameters for the desired active unit of the HA pair
name=wabbit                    # Name of the DUT
        wancom0_ip=10.196.145.49           # this is it!
accessmode=telnet              # Method to use to connect to the DUTs CLI
                               # Can be: telnet | ssh | console
accessport=wancom0             # Port name to connect to the DUT's CLI when
                               # using telnet or ssh as the accessmode.  For the
                               # "console" accessmode the terminal server will
                               # be used instead.
tsip=10.196.144.55              # Terminal server IP address.  Currently only
                               # Lantronix Terminal Servers are supported.
tsport=2006                    # Terminal server port (TCP port, not physical
                               # port)




"""


print
print '============== COMMENTS..'
for line in re.split('\r|\n', lines):
  line = line.strip()
  if line.startswith('#'):
    print line

print
print '============== DATA..'
for line in re.split('\r|\n', lines):
  line = line.strip()
  if not line.startswith('#'):
    postline = re.sub('\s*#.*', '', line)
    if postline == line:
      print line
    else:
      print
      print line
      print postline, '(comments removed)'
      print
