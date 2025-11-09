# 💤 LazyLogs


Hi! I made **LazyLogs**, a simple tool for people who are too *lazy 🧢* to clean logs manually (like me :3).  
Just run it once and *Kaboom* — logs are archived, old logs are deleted, and old archives are cleaned up.  
Keep your system clean without the hassle.

---

## ✨ Features

- 📦 Archive logs into **tar.gz** format  
- 🗑️ Automatically delete old logs  
- 🗂️ Clean up old archives to save space  
- 📝 Record all activity in `archive.log`  
- ⚡ Interactive & non-interactive modes  
- 🔍 **Dry Run mode** for testing without making changes 

---

## 📂 Project Structure

```
lazylogs/
├── log_archive.py     # Main script
├── README.md          # Documentation
├── LICENSE            # License
├── .gitignore         # # Git ignore rules
├── archives/          # Archives folder (auto-created)
└── archive.log        # Activity log (auto-created)
```

---

## ⚙️ Installation
Follow the steps below to get started:

### 1. Check if Python is installed
Run the command:

- Linux/macOS:
  ```bash
  python3 --version
  ```
- Windows:
  ```powershell
  python --version
  ```

If you see something like Python 3.10.12, you’re good to go. ✅ 

### 2. If Python is not installed
- **Windows** → Download from [python.org/downloads](https://www.python.org/downloads/) and install (check Add to PATH during setup).  
- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt update
  sudo apt install python3 -y
  ```
- **Linux (Arch/Manjaro):**
  ```bash
  sudo pacman -S python
  ```
- **macOS** (use [Homebrew](https://brew.sh/)):
  ```bash
  brew install python
  ```

### 3. Clone or download this project
```bash
git clone https://github.com/Chikochiii/lazylogs.git
cd lazylogs
```

---

## 🚀 Usage

### Mode 1: Non-Interactive
Run directly with arguments:
```bash
python log_archive.py <log_dir> <keep_logs_days> <keep_archives_days> [--dry-run]
```

Example:
```bash
python log_archive.py /var/log 7 30
```

Explanation:
- `/var/log` → the log directory to archive    
- `7` → logs older than 7 days will be deleted
- `30` →  archives older than 30 days will be deleted 
- `--dry-run` → optional, simulate only without deleting/archiving 

### Mode 2: Interactive
Too **lazy** to type arguments? Just run:
```bash
python log_archive.py
```
It shows a menu:
```
=== LazyLogs Menu ===
1. Set log directory
2. Set log retention days
3. Set archive retention days
4. Run archiving
5. Exit
```
Choose what you need and let it work for you.

---

## 📝 Example Output

- Archives are stored in`archives/`:
  ```
  logs_archive_20240915_103012.tar.gz
  ```
- Activity is logged in `archive.log`.

---

## 🤔 Why LazyLogs?

Because:
- You’re too lazy to delete logs manually
- You’re too lazy to think about archive names
- You’re too lazy to check files one by one
👉 Let **LazyLogs** do it for you.

---

## 📜 Lisensi

This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Future Ideas

- Upload archives to Google Drive / Dropbox / S3
- Send notifications via Email / Telegram
- Add a mini GUI for non-CLI users 

---

## Message✉️
Please click the ⭐ (`star`) button if you like this project — it motivates me to create more projects 👉👈

<a href="https://cdn.donmai.us/original/7b/95/__10251858__7b95b725704153e65b399c48a82aca0d.webp?download=1" alt="pwissss" border="0" width="200"></a>
