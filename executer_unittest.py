from peer_info import PeerInfo
from commands_manager import CommandLine, CommandManager
from executer import CommandExecuter, ExecuterManager
from mock_pexpect import Mockpexpect
import unittest

class CommandExecuterTest(unittest.TestCase):

  def test_FormatCommand(self):
    cmd_execter = CommandExecuter()

    result_1 = cmd_execter.FormatCommand("ls", "192.168.0.1", "walle")
    self.assertEqual(result_1, "ssh walle@192.168.0.1 \"ls\"")

    result_2 = cmd_execter.FormatCommand("/tmp/udp_test.sh", "192.168.1.1", "walle")
    self.assertEqual(result_2, "ssh walle@192.168.1.1 \"/tmp/udp_test.sh\"")
  
  def test_DoRun(self):

    passwd = "12345"

    child = Mockpexpect(["yes/no", "[Pp]assword"])
    ce = CommandExecuter()
    ce.DoRun(child, passwd)

    right_result = ["yes", passwd]
    right_result.sort()
    right_result = ",".join(right_result)
    self.assertEqual(right_result, child.GetAllLine())

    child = Mockpexpect(["[Pp]assword"])
    ce = CommandExecuter()
    ce.DoRun(child, passwd)

    right_result = [passwd]
    right_result.sort()
    right_result = ",".join(right_result)
    self.assertEqual(right_result, child.GetAllLine())


class MockExecuter:
  def __init__(self):
    self.command_list_ = []
  def Run(self, command_line, remote_ip, user, password, expect_result):
    cmd = "ssh %s@%s \"%s\"" % (user, remote_ip, command_line)
    self.command_list_.append(cmd)

  def GetResult(self):
    self.command_list_.sort()
    our_result = ','.join(self.command_list_)
    return our_result


class ExecuterMangerTest(unittest.TestCase):
  def test_RunAll(self):
    command1 = CommandLine("ls", False)
    command2 = CommandLine("/tmp/udp_test args", False)
    command_list = [command1, command2]
    peer_info = PeerInfo("192.168.0.1", "walle", "123456")
    executer = MockExecuter()
    executer_manager = ExecuterManager(executer)
    executer_manager.RunAll(command_list, peer_info)

    right_result = ["ssh walle@192.168.0.1 \"ls\"",
                    "ssh walle@192.168.0.1 \"/tmp/udp_test args\""]
    right_result.sort()
    right_result = ','.join(right_result)

    result = executer.GetResult()
    self.assertEqual(right_result, result)

if __name__ == "__main__":
    unittest.main()

