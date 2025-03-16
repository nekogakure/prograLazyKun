'''
    プログラさぼり君
            version: 1
    
        Made by nekogakure.

    このプログラムは、ランダムなログメッセージを生成し、
    ログレベルに応じて色付けして表示します。
    つまり、プログラムをコンパイルしているように見せかけ
    たりしてプログラミングをさぼれます。

    使い方:
        - プログラムを実行すると、ランダムなログメッセージが表示されます。
        - ログメッセージは、同じディレクトリに設置されたlog.txtファイルに
          記述されたものからランダムに選択されます。

    必要なライブラリ:
        - colorama

    著作権は放棄しませんが商用利用、改変、再配布など自由に
    していただいて構いません。クレジットも不要です。
'''




import time
import random
import datetime
import os
os.system('pip install colorama')

from colorama import init, Fore

# 色を有効にする
init(autoreset=True)

# ログの種類と色
LOG_LEVELS = {
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "DEBUG": Fore.CYAN,
    "CRITICAL": Fore.MAGENTA,
    "FATAL": Fore.LIGHTRED_EX
}

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(current_dir+'\log.txt', 'r') as f:
    kw_list = f.read().split("\n")

LOG_MESSAGES = kw_list

'''
LOG_MESSAGES = [
    "[INFO] System initialization completed.",
    "[INFO] Kernel loaded successfully.",
    "[INFO] User login from {}.",
    "[INFO] Fetching latest software updates...",
    "[INFO] File '{}' successfully processed.",
    "[INFO] Process {} started.",
    "[INFO] CPU Temperature: {}°C",
    "[INFO] Memory usage: {}%",
    "[INFO] Disk space available: {}GB",
    "[INFO] Network latency: {}ms",
    "[INFO] Backup completed successfully.",
    "[INFO] Connection established to {}:{}",
    "[INFO] Database connection established.",
    "[INFO] Web service running on port {}.",
    "[INFO] User '{}' successfully authenticated.",
    "[INFO] API request received from {}.",
    "[INFO] Session expired for user '{}'.",
    "[INFO] Virtual machine '{}' started.",
    "[INFO] Log file rotated: '{}'.",
    "[INFO] System uptime: {} hours.",
    
    "[WARNING] High memory usage detected ({}%).",
    "[WARNING] Disk usage {}% on /dev/sda1. Cleanup recommended.",
    "[WARNING] Unauthorized access attempt detected from {}.",
    "[WARNING] Network congestion detected. Packet loss: {}%",
    "[WARNING] SSL certificate expires in {} days.",
    "[WARNING] Process '{}' consuming high CPU ({}%).",
    "[WARNING] Running low on disk space: {}GB remaining.",
    "[WARNING] Background job '{}' taking longer than expected.",
    "[WARNING] User '{}' attempted invalid login.",
    "[WARNING] DNS resolution delay: {}ms.",
    
    "[ERROR] Connection to {}:{} failed. Retrying...",
    "[ERROR] Service '{}' failed to start.",
    "[ERROR] Database query failed: '{}'.",
    "[ERROR] File '{}' not found.",
    "[ERROR] Process {} crashed due to segmentation fault.",
    "[ERROR] Kernel module '{}' failed to load.",
    "[ERROR] Out of memory. Process {} killed.",
    "[ERROR] System clock out of sync by {} seconds.",
    "[ERROR] Could not write to log file '{}'.",
    "[ERROR] API request to '{}' timed out.",
    "[ERROR] SMTP server unreachable at {}.",
    "[ERROR] No response from gateway at {}.",
    "[ERROR] Authentication error for user '{}'.",
    "[ERROR] Unable to resolve hostname '{}'.",
    "[ERROR] Failed to mount filesystem '{}'.",
    "[ERROR] Timeout waiting for process {}.",
    "[ERROR] Corrupted file detected: '{}'.",
    
    "[DEBUG] Background job '{}' completed successfully.",
    "[DEBUG] Cache cleared successfully.",
    "[DEBUG] Packet received from {}:{}",
    "[DEBUG] User session '{}' extended.",
    "[DEBUG] API request '{}' processed in {}ms.",
    "[DEBUG] Thread '{}' executed in {}ms.",
    "[DEBUG] Temporary file '{}' deleted.",
    "[DEBUG] Process '{}' memory allocation: {}MB.",
    "[DEBUG] System time adjusted by {}ms.",
    "[DEBUG] Debugging mode enabled for '{}'.",
    
    "[CRITICAL] Kernel panic! System stability at risk.",
    "[CRITICAL] Power supply unstable! Switching to backup...",
    "[CRITICAL] RAID array failure detected on {}.",
    "[CRITICAL] Unauthorized root access detected.",
    "[CRITICAL] Network outage detected at {}.",
    "[CRITICAL] Disk failure on drive '{}'.",
    "[CRITICAL] Emergency shutdown in progress...",
    "[CRITICAL] Core dump created at '{}'.",
    
    "[FATAL] Unexpected shutdown initiated!",
    "[FATAL] System failure detected. Reboot required.",
    "[FATAL] Security breach detected in process '{}'.",
    "[FATAL] Data corruption detected on volume '{}'.",
    "[FATAL] Hardware failure: '{}' component damaged.",
    "[FATAL] Emergency mode activated.",
    "[FATAL] BIOS corruption detected!",
    "[FATAL] Motherboard voltage irregularity detected.",
    "[FATAL] Backup system failure!",
    "[FATAL] CPU overheating! Immediate shutdown required.",
]
'''
# ランダムなデータ生成関数
def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def random_port():
    return random.randint(1024, 65535)

def random_percentage():
    return random.randint(1, 100)

def random_gb():
    return round(random.uniform(0.1, 500), 1)

def random_ms():
    return round(random.uniform(1, 5000), 1)

def random_filename():
    return f"file_{random.randint(1000, 9999)}.log"

def random_process_id():
    return random.randint(1000, 99999)

def random_temperature():
    return round(random.uniform(30, 95), 1)

def random_seconds():
    return random.randint(1, 10000)

def random_user():
    return random.choice(["root", "python", "guest", "pip"])

def random_database_error():
    return random.choice([
        "Syntax error near 'SELECT * FROM'",
        "Connection timeout",
        "Primary key constraint violation",
        "Deadlock detected"
    ])

def show_progress_bar(task_name, progress):
    bar_length = 50
    block = int(round(bar_length * progress))
    progress_str = "█" * block + " " * (bar_length - block)
    print(f"\r{task_name}: [ {progress_str} ] {int(progress * 100)}%", end="")

while True:
    timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    pid = random_process_id()

    message = random.choice(LOG_MESSAGES)

    placeholders = message.count("{}") + message.count("'{}'")
    random_data = [
        random.choice([
            random_percentage(), random_ip(), random_port(),
            random_filename(), random_database_error(),
            random_process_id(), random_temperature(),
            random_gb(), random_ms(), random_seconds(),
            random_user()
        ])
        for _ in range(placeholders)
    ]

    try:
        message = message.format(*random_data)
    except IndexError as e:
        print(Fore.RED + f"[ERROR] [SYSTEM] Log formatting error: {e}")
        continue

    log_level = message.split("]")[0][1:]
    color = LOG_LEVELS.get(log_level, Fore.WHITE)

    progress = 0
    while progress < 1:
        progress += random.uniform(0.1, 0.5)
        progress = min(progress, 1)
        show_progress_bar(f":", progress)
        time.sleep(random.uniform(0.1, 0.5))

    print(f"\n{color}[{log_level}] [{timestamp}] (PID: {pid}) {message}")

    delay = random.choice([
        random.uniform(0.01, 0.1),
        random.uniform(0.1, 0.5),
        random.uniform(0.5, 1.5),
        random.uniform(1.5, 3.0)
    ])
    time.sleep(delay)
