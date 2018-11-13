import string
from config import ScriptConfig
from file_transport_info import FileTransportManager
from peer_info import PeerInfoManager
from deploy import CopyImplement, CopyOption
from commands_manager import CommandLine, CommandManager
from executer import CommandExecuter, ExecuterManager
import os
import argparse


if __name__ == "__main__":
  parse = argparse.ArgumentParser(description = 'run client')
  parse.add_argument('--config', type=str, default=None, help="config file path")
  parse.add_argument('--port', type=int, default=None, help="port for client")
  argv = parse.parse_args()

  config = ScriptConfig()
  config.ParseConfig(argv.config)
  peer_info_data = config.GetPeerInfoData()
  peer_manager = PeerInfoManager(peer_info_data)

  for peer_info in peer_manager.GetPeerInfoList():
#    cmd = "iperf -c %s -u -b 100m -t 120 -t 120 -i 1 -p %d 1>/dev/null &" % (peer_info.GetAddress(), argv.port)
    cmd = "iperf -c %s -u -b 5m -t 60 -i 1 -p %d &" % (peer_info.GetAddress(), argv.port)
    print "Running "+cmd
    os.system(cmd)

 
 