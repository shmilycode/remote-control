import stat
import pexpect
import argparse

import config
import file_transport_info
import peer_info

class CopyOption:
    '''
    copy file to remote user
    '''
    def scp_to(file_path, remote_path, remote_ip, usr, passwd):
        cmd = "scp %s %s@%s:%s" % {file_path, usr, remote_ip, remote_path}
        print ("Doing: "+scp)

        child = pexpect.spawn(cmd)
        child.expect("Password:")
        child.sendline(passwd)
        child.interact()
class CopyImplement:
    def __init__(self, delegate):
        self.copy_delegate_ = delegate

    def CopyFilesTo(self, file_info_list, peer_info):
        for file_info in file_info_list:
            self.copy_delegate.scp_to(file_info.GetSourceFilePath(), file_info.GetDestFilePath(), 
                            peer_info.GetAddress(), peer_info.GetUserName(), peer_info.GetPassword())

def main(config_path):
    try:
        config = ScriptConfig(config_path) 
        '''
        Get peers infomations
        '''
        peer_info_data = config.GetPeerInfoData()
        peer_manager = PeerInfoManager(peer_list_data)

        '''
        Get file list
        '''
        file_transport_manager = FileTransportManager(config.GetFileTransportData())

        copy_delegate = CopyOption()
        copy_implement = CopyImplement(copy_delegate)
        for peer_info in peer_manager.GetPeerInfoList():
            copy_implement.CopyFilesTo(file_transport_manger.GetFileTransportList(), peer_info)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    ip_list = get_ip_list() 
    parse = argparse.ArgumentParser(description = 'manual to this script')
    parse.add_argument('--config', type=str, default=None)
    argv = parse.parse_args()
    main(argv.config)


