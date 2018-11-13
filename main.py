import string
from config import ScriptConfig
from file_transport_info import FileTransportManager
from peer_info import PeerInfoManager
from deploy import CopyImplement, CopyOption
from commands_manager import CommandLine, CommandManager
from executer import CommandExecuter, ExecuterManager
import argparse

def Finish(name):
  print name+" Finish."
  choice = raw_input("Do next step ? yes/no: ")
  return HandleInput(choice)


def HandleInput(input_data):
  if(input_data == "yes"):
    return True
  else:
    return False

def Deploy(peer_manager, file_transport_manager):
  copy_delegate = CopyOption()
  copy_implement = CopyImplement(copy_delegate)
  for peer_info in peer_manager.GetPeerInfoList():
      copy_implement.CopyFilesTo(file_transport_manager.GetFileTransportList(), peer_info)

  return Finish("Deploy")

def RunScript(peer_manager, command_manager):
  command_executer = CommandExecuter()
  executer_manager = ExecuterManager(command_executer)
  for peer_info in peer_manager.GetPeerInfoList():
    executer_manager.RunAll(command_manager.GetCommandList(), peer_info)

  return Finish("RunScript")

def LoadConfig(config_path):
  config = ScriptConfig()
  config.ParseConfig(config_path)
  return config

def GetPeers(config):
  '''
  Get peers infomations
  '''
  peer_info_data = config.GetPeerInfoData()
  peer_manager = PeerInfoManager(peer_info_data)
  return peer_manager


def main(config_path, need_deploy):

  config = LoadConfig(config_path)
  peer_manager = GetPeers(config)

  '''
  Get file list
  '''
  print need_deploy
  if(need_deploy == True):
    file_transport_manager = FileTransportManager(config.GetFileTransportData())
    '''
    Deploy
    '''
    ret = Deploy(peer_manager, file_transport_manager)

    if(ret is False):
      print "Finish Deploy, and exit now!"
      return;

  '''
  Run script
  '''
  commands_data = config.GetCommandsData()
  command_manager = CommandManager(commands_data)
  RunScript(peer_manager, command_manager)

def run_command(config_path, cmd, run_in_background):
  config = LoadConfig(config_path)
  peer_manager = GetPeers(config)
  '''
  Run command
  '''
  commands_data = [{"command":cmd, "background":run_in_background}]
  command_manager = CommandManager(commands_data)
  return RunScript(peer_manager, command_manager)

def upload_log(config_path, suffix):
  upload_cmd = "/tmp/upload_log.sh http://172.18.91.173/Code/upload/upload_file.php userfile mlan0 %s" % (suffix)
  kill_cmd = "/tmp/kill_script.sh iperf"
  ret = run_command(config_path, kill_cmd, "")
  if(ret is True):
    run_command(config_path, upload_cmd, "")

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description = 'manual to this script')
    parse.add_argument('--config', type=str, default=None, help="config file path")
    parse.add_argument('--run', type=str, default=None, help="run commands")
    parse.add_argument('-background', action="store_true", help="is need to run in background")
    parse.add_argument('-upload_udp', action="store_true", help="upload the udp log")
    parse.add_argument('-upload_multicast', action="store_true", help="upload the multicast log")
    parse.add_argument('-deploy', action="store_true", help="is need to deploy the script")
    argv = parse.parse_args()
    if(argv.config is None):
      parse.print_help()
    elif(argv.run):
      run_command(argv.config, argv.run, argv.background)
    elif(argv.upload_udp == True):
      upload_log(argv.config, "_udp_server.log")
    elif(argv.upload_multicast == True):
      upload_log(argv.config, "_multicast_server.log")
    else:
      main(argv.config, argv.deploy)
