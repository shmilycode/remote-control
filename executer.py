import pexpect
import string

class CommandExecuter:

  def Run(self, command_line, remote_ip, user, password):
    cmd = self.FormatCommand(command_line, remote_ip, user)
    expect = self.Spawn(cmd)
    return self.DoRun(expect, password)

  def FormatCommand(self, command_line, remote_ip, usr):
    return  "ssh %s@%s \"%s\"" % (usr, remote_ip, command_line)

  def DoRun(self, child, password):
    ret = child.expect(["[Pp]assword","yes/no"], timeout = 5)
    if(ret is 1):
        child.sendline("yes")
        child.expect("[Pp]assword:")
        child.sendline(password)
    elif (ret is 0):
        child.sendline(password)

    child.interact()

  def Spawn(self, command):
      return pexpect.spawn(command)

class ExecuterManager:
  def __init__(self, executer):
    self.executer_ = executer

  def RunAll(self, command_list, peer_info):
    for cmd in command_list:
      self.executer_.Run(cmd.GetCommandLine(), peer_info.GetAddress(), 
                        peer_info.GetUserName(), peer_info.GetPassword())
