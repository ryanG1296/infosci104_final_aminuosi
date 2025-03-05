import subprocess
import os
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewFileHandler(FileSystemEventHandler):
    def __init__(self, extension, callback):
        self.extension = extension
        self.callback = callback

    def on_created(self, event):
        if event.src_path.endswith(self.extension):
            print(f"New file created: {event.src_path}")
            self.callback(event.src_path)

def run_script(script_path, args=None):
    if args is None:
        args = []
    print(f"Running script: {script_path} with args: {args}")
    subprocess.run(['python', script_path] + args)

def wait_for_new_file(directory, extension):
    event_handler = NewFileHandler(extension, lambda path: observer.stop())
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f"Waiting for new file in directory: {directory} with extension: {extension}")
    observer.join()
    return event_handler.callback

def wait_for_file_update(file_path):
    last_modified_time = os.path.getmtime(file_path)
    while True:
        time.sleep(1)
        current_modified_time = os.path.getmtime(file_path)
        if current_modified_time != last_modified_time:
            print(f"File updated: {file_path}")
            return

def check_for_stop():
    while True:
        user_input = input()
        if user_input.lower() == 'n':
            print("Stop signal received")
            return True

# 定义文件路径
base_dir = r'C:\Users\18660\Desktop\00dkuclass\info104\000final'
test_scanner_path = os.path.join(base_dir, 'testScannerTemp.py')  # 修改为 testScannerTemp.py
text2speech_path = os.path.join(base_dir, 'text2speech.py')
manbo1_path = os.path.join(base_dir, 'manbo1.txt')
testapi102_path = os.path.join(base_dir, 'testapi102.py')
audio2text_path = os.path.join(base_dir, 'audio2text.py')

# 启动 testScannerTemp.py
scanner_process = subprocess.Popen(['python', test_scanner_path])
print("Started testScannerTemp.py")

# 检查键盘输入
stop_thread = threading.Thread(target=check_for_stop)
stop_thread.start()
print("Started check_for_stop thread")

# 等待新的 .wav 文件生成
new_wav_file = wait_for_new_file('.', '.wav')
print(f"New .wav file detected: {new_wav_file}")

# 如果收到停止信号，终止 testScannerTemp.py 并运行 audio2text.py
if stop_thread.is_alive():
    scanner_process.terminate()
    print("Terminated testScannerTemp.py")
    run_script(audio2text_path)
else:
    # 启动 text2speech.py 并传入新生成的 .wav 文件名
    run_script(text2speech_path, [new_wav_file])

    # 等待 manbo1.txt 文件内容更新
    wait_for_file_update(manbo1_path)

    # 读取 manbo1.txt 文件内容
    with open(manbo1_path, 'r') as file:
        manbo1_content = file.read().strip()
    print(f"Read manbo1.txt content: {manbo1_content}")

    # 启动 testapi102.py 并传入 manbo1.txt 文件内容
    run_script(testapi102_path, [manbo1_content])

    # 读取 testapi102.py 返回的字符串（假设它输出到标准输出）
    result = subprocess.check_output(['python', testapi102_path, manbo1_content]).decode().strip()
    print(f"testapi102.py result: {result}")

    # 启动 text2speech.py 并传入 testapi102.py 返回的字符串
    run_script(text2speech_path, [result])