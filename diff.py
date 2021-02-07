#!/usr/bin/python
#
# This wrapper script is needed to get meld working with git.  The purpose is
# to get rid of the extra arguments.

import sys
import os

os.system('meld "%s" "%s"' % (sys.argv[2], sys.argv[5]))
