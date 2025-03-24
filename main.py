'''
    プログラさぼり君
            version: 1.2
    
        Made by nekogakure.

    このプログラムは、ランダムなログメッセージを生成し、
    ログレベルに応じて色付けして表示します。
    つまり、プログラムをコンパイルしているように見せかけ
    たりしてプログラミングをさぼれます。

    使い方:
        - プログラムを実行すると、ランダムなログメッセージが表示されます。
        - ログメッセージは、同じディレクトリに設置された
          gcc.txt, clang.txt, msvc.txt などのファイルから
          ランダムに選択されます。

    必要なライブラリ:
        - colorama

    著作権は放棄しませんが商用利用、改変、再配布など自由に
    していただいて構いません。クレジットも不要です。
'''

import time
import random
import datetime
import os
from colorama import init, Fore

# 色を有効にする
init(autoreset=True)

# ログの種類と色
LOG_LEVELS = {
    "INFO": Fore.GREEN,
    "info": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "warning": Fore.YELLOW,
    "ERROR": Fore.RED,
    "error": Fore.RED,
    "DEBUG": Fore.CYAN,
    "debug": Fore.CYAN,
    "CRITICAL": Fore.MAGENTA,
    "critical": Fore.MAGENTA,
    "FATAL": Fore.LIGHTRED_EX,
    "fatal": Fore.LIGHTRED_EX
}

current_dir = os.path.dirname(os.path.abspath(__file__))

# コンパイラ選択
def select_compiler():
    compilers = ["gcc", "clang", "cargo", "python", "java"]
    print("使用するコンパイラを選択してください:")
    for i, compiler in enumerate(compilers, start=1):
        print(f"{i}. {compiler}")
    while True:
        try:
            choice = int(input("番号を入力: "))
            if 1 <= choice <= len(compilers):
                return compilers[choice - 1]
            else:
                print("無効な番号です。もう一度入力してください。")
        except ValueError:
            print("数字を入力してください。")

# ログメッセージをファイルから読み込む
def load_log_messages(compiler):
    log_file = os.path.join(current_dir, f"src/{compiler}.txt")
    if not os.path.exists(log_file):
        print(Fore.RED + f"[ERROR] ログファイルが見つかりません: {log_file}")
        return []
    with open(log_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# コンパイラを選択
selected_compiler = select_compiler()
LOG_MESSAGES = load_log_messages(selected_compiler)

if not LOG_MESSAGES:
    print(Fore.RED + "[ERROR] ログメッセージが読み込めませんでした。プログラムを終了します。")
    exit(1)

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
    return random.choice(["root", "python", "guest", "pip", "admin"])

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

# メインループ
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
    log_level = message.split(":")[0][1:]
    color = LOG_LEVELS.get(log_level, Fore.WHITE)

    progress = 0
    while progress < 1:
        progress += random.uniform(0.1, 0.5)
        progress = min(progress, 1)
        show_progress_bar(f"{selected_compiler}", progress)
        time.sleep(random.uniform(0.1, 0.5))

    print(f"\n{color}{log_level} [{timestamp}] (PID: {pid}) {message}")

    delay = random.choice([
        random.uniform(0.01, 0.1),
        random.uniform(0.1, 0.5),
        random.uniform(0.5, 1.5),
        random.uniform(1.5, 3.0)
    ])
    time.sleep(delay)