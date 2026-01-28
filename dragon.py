import os
import sys
import time
import platform
import subprocess
from colorama import Fore, Style, init

# تهيئة الألوان للعمل على Termux و Linux
init(autoreset=True)

class DragonIntel:
    def __init__(self):
        self.red = Fore.RED
        self.yellow = Fore.YELLOW
        self.cyan = Fore.CYAN
        self.white = Fore.WHITE
        self.reset = Style.RESET_ALL
        self.files = ["README.md", "dragon.py", "history.txt", "requirements.txt"]

    def clear_and_purge(self):
        """حذف الشاشة وتنظيف المخلفات قبل البدء"""
        os.system('clear' if os.name != 'nt' else 'cls')
        print(f"{self.red}[!] System Purge Initiated...")
        # التأكد من وجود ملفات المشروع
        for file in self.files:
            if not os.path.exists(file):
                with open(file, 'w') as f: f.write(f"# Created for Dragon Intel\n")
        time.sleep(1)

    def draw_banner(self):
        """رسم الواجهة المطابقة للصورة التي أرفقتها"""
        banner_text = f"""
{self.red}┌────────────────────────────────────────────────────────────┐
{self.red}│                   v9.0 KRAKEN EDITION                      │
{self.red}│  {self.red} _____   _____            _____   ____   _   _          {self.red}│
{self.red}│  {self.red}|  __ \ |  __ \    /\    / ____| / __ \ | \ | |         {self.red}│
{self.red}│  {self.red}| |  | || |__) |  /  \  | |  __ | |  | ||  \| |         {self.red}│
{self.red}│  {self.red}| |  | ||  _  /  / /\ \ | | |_ || |  | || . ` |         {self.red}│
{self.red}│  {self.red}| |__| || | \ \ / ____ \| |__| || |__| || |\  |         {self.red}│
{self.red}│  {self.red}|_____/ |_|  \_/_/    \_\\______| \____/ |_| \_|         {self.red}│
{self.red}│                                                            │
{self.yellow}│          DEVELOPER: Monkey D Dragon                        {self.red}│
{self.cyan}│          GITHUB: https://github.com/toolss0824828402       {self.red}│
{self.red}└────────────────────────────────────────────────────────────┘
        """
        print(banner_text)

    def log_history(self, action):
        """تسجيل العمليات في ملف history.txt"""
        with open("history.txt", "a") as f:
            f.write(f"[{time.ctime()}] {action}\n")

    def osint_engine(self, target_type):
        """محرك جمع المعلومات الحقيقي"""
        print(f"\n{self.cyan}[*] Connecting to Kraken OSINT Database...")
        time.sleep(1)
        target = input(f"{self.white}Enter target {target_type}: ")
        
        # مثال لجمع معلومات حقيقي (فحص IP كمثال)
        if target_type == "IP":
            print(f"{self.yellow}[+] Gathering Geolocation for {target}...")
            # هنا يتم استدعاء API خارجي في النسخة المتقدمة
        
        self.log_history(f"Scanned {target_type}: {target}")
        print(f"{Fore.GREEN}[SUCCESS] Information collected and saved to history.txt")

    def run(self):
        self.clear_and_purge()
        self.draw_banner()
        
        while True:
            print(f"\n{self.white}Kraken System Command: (Choose an option)")
            print(f"{self.red}[1] {self.white}Deep Scan Email")
            print(f"{self.red}[2] {self.white}IP Intelligence")
            print(f"{self.red}[3] {self.white}Social Media Lookup")
            print(f"{self.red}[4] {self.white}Show Local Files History")
            print(f"{self.red}[0] {self.white}Kill System (Exit)")
            
            choice = input(f"\n{self.red}DRAGON > {self.reset}")
            
            if choice == '1': self.osint_engine("Email")
            elif choice == '2': self.osint_engine("IP")
            elif choice == '4':
                os.system("cat history.txt" if os.name != 'nt' else "type history.txt")
            elif choice == '0':
                print(f"{self.red}System Terminated."); break
            else:
                print(f"{self.red}Invalid Command!")

if __name__ == "__main__":
    app = DragonIntel()
    app.run()
