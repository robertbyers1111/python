from subprocess import Popen, PIPE, STDOUT

emailexe = '/bin/mail'
emailfrom = '-rlabmonitor@acmepacket.com'
emailsubj = '-sABC-07'
emailrecipients = 'bob.byers@oracle.com'
emailmsg = b'one\ntwo\nthree\nfour\nfive\nsix\n'

p = Popen([emailexe, \
     emailfrom, \
     emailsubj, \
     emailrecipients], \
    stdout=PIPE, \
    stdin=PIPE, \
    stderr=STDOUT)    

grep_stdout = p.communicate(input=emailmsg)[0]
print(grep_stdout.decode())

