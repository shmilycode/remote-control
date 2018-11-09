from config import ScriptConfig 
from file_transport_info import FileTransportInfo
from peer_info import PeerInfo
from copy_opt import CopyImplement, CopyOption
import unittest

class Mockpexpect:
    def __init__(self, pattern_list):
        self.pattern_list_ = pattern_list
        self.send_line_list_ = []

    def expect(self, pattern, timeout):
        target_pattern = "you can't match me, haha"
        if(len(self.pattern_list_) > 0):
            target_pattern = self.pattern_list_[0]
            self.pattern_list_ = self.pattern_list_[1:]
        print '\n'+target_pattern

        if(isinstance(pattern, list) is False):
            print "isinstance is false"
            if(pattern == target_pattern):
                return 0
            else:
                return -1
        print target_pattern + "".join(pattern) + str(pattern.count(target_pattern))
        if(pattern.count(target_pattern) == 0):
            return -1
        return pattern.index(target_patern)        
        
    def sendline(self, line):
        self.send_line_list_.append(line)
    
    def interact(self):
        return

    def GetAllLine(self):
        self.send_line_list_.sort()
        return "".join(self.send_line_list_)


class CopyOptionTest(unittest.TestCase):
    def test_CopyOption(self):
        co = CopyOption()
        result_1 = co.FormatCommand("./a", "./b", "192.168.0.1", "walle", "wer")
        self.assertEqual(result_1, "scp ./a walle@192.168.0.1:./b")

        result_2 = co.FormatCommand("/usr/bin/iperf", "/usr/local/bin/iperf", "192.168.1.1", "walle", "")
        self.assertEqual(result_2, "scp /usr/bin/iperf walle@192.168.1.1:/usr/local/bin/iperf")

    def test_ScpToExpect(self):
        cmd = "scp /usr/bin/iperf walle@192.168.1.1:/usr/local/bin/iperf"
        passwd = "12345"

        child = Mockpexpect(["yes/no", "password"])
        co = CopyOption()
        co.ScpToExpect(child, cmd, passwd)

        right_result = ["yes", passwd]
        right_result.sort()
        right_result = "".join(right_result)
        self.assertEqual(right_result, child.GetAllLine())

class MockCopyDelegate:
    def __init__(self):
        self.result_pool = []

    def ScpTo(self, file_path, remote_path, remote_ip, usr, passwd):
        cmd = "scp %s %s@%s:%s" % (file_path, usr, remote_ip, remote_path)
        self.result_pool.append(cmd) 

    def GetResult(self):
        self.result_pool.sort()
        our_result = ''.join(self.result_pool)
        return our_result

class CopyImplementTest(unittest.TestCase):
    def test_CopyFilesTo(self):
        file_transport_info1 = FileTransportInfo("./a", "./b")
        file_transport_info2 = FileTransportInfo("/usr/bin/iperf", "/usr/local/bin/iperf")
        file_transport_list = [file_transport_info1, file_transport_info2]
        peer_info = PeerInfo("192.168.0.1", "walle", "123456")
        copy_delegate = MockCopyDelegate()
        copy_implement = CopyImplement(copy_delegate)
        copy_implement.CopyFilesTo(file_transport_list, peer_info)

        right_result = ["scp ./a walle@192.168.0.1:./b",
                        "scp /usr/bin/iperf walle@192.168.0.1:/usr/local/bin/iperf"]
        right_result.sort()
        right_result = ''.join(right_result)

        result = copy_delegate.GetResult()
        self.assertEqual(right_result, result)

if __name__ == "__main__":
    unittest.main()



