import string
import os
import argparse


if __name__ == "__main__":
  parse = argparse.ArgumentParser(description = 'run client')
  parse.add_argument('--address', type=str, default=None, help="Address to multicast")
  parse.add_argument('--port', type=int, default=None, help="port for client")
  argv = parse.parse_args()

   # -b band-with -p port 
  cmd = "iperf -c %s -u -b 5m -t 10 -i 1 -p %d &" % (argv.address, argv.port)
  print "Running "+cmd
  os.system(cmd)

 
 