import stat
import pexpect

from config import ScriptConfig
from file_transport_info import FileTransportManager
from peer_info import PeerInfoManager

class CopyOption:
    '''
    copy file to remote user
    '''
    def FormatCommand(self, file_path, remote_path, remote_ip, usr):
       return  "scp %s %s@%s:%s" % (file_path, usr, remote_ip, remote_path)

    def Spawn(self, command):
        return pexpect.spawn(command)

    def ScpToExpect(self, child, passwd):
        ret = child.expect(["[Pp]assword","yes/no"], timeout = 5)
        if(ret is 1):
            child.sendline("yes")
            child.expect("[Pp]assword:")
            child.sendline(passwd)
        elif (ret is 0):
            child.sendline(passwd)

        child.interact()

    def ScpTo(self, file_path, remote_path, remote_ip, usr, passwd):
        cmd = self.FormatCommand(file_path, remote_path, remote_ip, usr)
        print ("Doing: "+cmd)
        child = self.Spawn(cmd)
        self.ScpToExpect(child, passwd)

class CopyImplement:
    def __init__(self, delegate):
        self.copy_delegate_ = delegate

    def CopyFilesTo(self, file_info_list, peer_info):
        for file_info in file_info_list:
            self.copy_delegate_.ScpTo(file_info.GetSourceFilePath(), file_info.GetDestFilePath(), 
                            peer_info.GetAddress(), peer_info.GetUserName(), peer_info.GetPassword())