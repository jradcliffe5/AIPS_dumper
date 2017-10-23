import os, sys
import getopt
import math, re
from AIPS import AIPS, AIPSDisk
from AIPSTask import AIPSTask, AIPSList
from AIPSData import AIPSUVData, AIPSImage, AIPSCat, _AIPSCatEntry
from Wizardry.AIPSData import AIPSUVData as WizAIPSUVData
import numpy as np
ifile=''
ofile=''

###############################
# o == option
# a == argument passed to the o
###############################
# Cache an error with try..except
# Note: options is the string of option letters that the script wants to recognize, with
# options that require an argument followed by a colon (':') i.e. -i fileName
#
prefix='PWD'

try:
    myopts, args = getopt.getopt(sys.argv[1:],"p:n:h")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -i input -o output" % sys.argv[0])
    sys.exit(2)

for o, a in myopts:
    if o == '-p':
        prefix=a
    elif o == '-n':
        AIPS.userno=int(a)
    elif o == '-h':
        print 'Help is on its way\n'
        print '-p defines a prefix output directory\n'
        print '-n defines an AIPS userno'
    else:
        print 'Put in some inputs'
print AIPS.userno
disk=0
if disk == 0:
    disks = range(1, len(AIPS.disks))
    pass

cat = {}
for disk in disks:
    proxy = AIPS.disks[disk].proxy()
    catalog = proxy.AIPSCat.cat(AIPS.disks[disk].disk, AIPS.userno)
    cat[disk] = [_AIPSCatEntry(entry) for entry in catalog]
    continue

for disk in disks:
    for i in cat[disk]:
        uvdata = AIPSUVData(i['name'],i['klass'],disk,i['seq'])
        fittp = AIPSTask('FITTP')
        fittp.indata = uvdata
        fittp.dataout = '%s:%s_%s_%s_%s.fits' % (prefix,i['name'],i['klass'],disk,i['seq'])
        fittp.go()
