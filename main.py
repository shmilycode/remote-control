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

def main(config_path):
  config = ScriptConfig()
  config.ParseConfig(config_path)
  '''
  Get peers infomations
  '''
  peer_info_data = config.GetPeerInfoData()
  peer_manager = PeerInfoManager(peer_info_data)

  '''
  Get file list
  '''
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


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description = 'manual to this script')
    parse.add_argument('--config', type=str, default=None)
    argv = parse.parse_args()
    main(argv.config)


