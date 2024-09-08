import subprocess
import time

# 打开一个终端并运行第一个命令
def run_command_in_terminal(command):
    # 在 Windows 上，你可以使用 'cmd' 或 'powershell'
    process = subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', command])
    return process

def main():
    # 第一个终端命令
    command1 = '.\koboldcpp.exe .\models\Hermes-3-Llama-3.1-8B.Q4_K_M.gguf'
    #process1 = run_command_in_terminal(command1)
    
    #time.sleep(20) 

    # 第二个终端命令
    command2 = 'python Agent.py'
    process2 = run_command_in_terminal(command2)

    # 等待两个进程结束
    #process1.wait()
    process2.wait()

if __name__ == '__main__':
    main()
