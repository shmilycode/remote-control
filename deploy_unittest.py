from file_transport_info import FileTransportInfo
from peer_info import PeerInfo
from deploy import CopyImplement, CopyOption
from mock_pexpect import Mockpexpect
import unittest

class CopyOptionTest(unittest.TestCase):
    def test_CopyOption(self):
        co = CopyOption()
        result_1 = co.FormatCommand("./a", "./b", "192.168.0.1", "walle")
        self.assertEqual(result_1, "scp ./a walle@192.168.0.1:./b")

        result_2 = co.FormatCommand("/usr/bin/iperf", "/usr/local/bin/iperf", "192.168.1.1", "walle")
        self.assertEqual(result_2, "scp /usr/bin/iperf walle@192.168.1.1:/usr/local/bin/iperf")

    def test_ScpToExpect1(self):
        passwd = "12345"

        child = Mockpexpect(["yes/no", "[Pp]assword"])
        co = CopyOption()
        co.ScpToExpect(child, passwd)

        right_result = ["yes", passwd]
        right_result.sort()
        right_result = ",".join(right_result)
        self.assertEqual(right_result, child.GetAllLine())

        child = Mockpexpect(["[Pp]assword"])
        co = CopyOption()
        co.ScpToExpect(child, passwd)

        right_result = [passwd]
        right_result.sort()
        right_result = ",".join(right_result)
        self.assertEqual(right_result, child.GetAllLine())

class MockCopyDelegate:
    def __init__(self):
        self.result_pool = []

    def ScpTo(self, file_path, remote_path, remote_ip, usr, passwd):
        cmd = "scp %s %s@%s:%s" % (file_path, usr, remote_ip, remote_path)
        self.result_pool.append(cmd) 

    def GetResult(self):
        self.result_pool.sort()
        our_result = ",".join(self.result_pool)
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
        right_result = ",".join(right_result)

        result = copy_delegate.GetResult()
        self.assertEqual(right_result, result)

if __name__ == "__main__":
    unittest.main()



