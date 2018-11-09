import stat
import pexpect
import argparse

from config import ScriptConfig
from file_transport_info import FileTransportManager
from peer_info import PeerInfoManager

class CopyOption:
    '''
    copy file to remote user
    '''
    def format_command(self, file_path, remote_path, remote_ip, usr, passwd):
       return  "scp %s %s@%s:%s" % (file_path, usr, remote_ip, remote_path)

    def scp_to(self, file_path, remote_path, remote_ip, usr, passwd):
        cmd = self.format_command(file_path, remote_path, remote_ip, usr, passwd)
        print ("Doing: "+cmd)

        child = pexpect.spawn(cmd)
        child.expect("Password:")
        child.sendline(passwd)
        child.interact()

class CopyImplement:
    def __init__(self, delegate):
        self.copy_delegate_ = delegate

    def CopyFilesTo(self, file_info_list, peer_info):
        for file_info in file_info_list:
            self.copy_delegate_.scp_to(file_info.GetSourceFilePath(), file_info.GetDestFilePath(), 
                            peer_info.GetAddress(), peer_info.GetUserName(), peer_info.GetPassword())

def main(config_path):
    try:
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

        copy_delegate = CopyOption()
        copy_implement = CopyImplement(copy_delegate)
        for peer_info in peer_manager.GetPeerInfoList():
            copy_implement.CopyFilesTo(file_transport_manager.GetFileTransportList(), peer_info)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description = 'manual to this script')
    parse.add_argument('--config', type=str, default=None)
    argv = parse.parse_args()
    main(argv.config)


