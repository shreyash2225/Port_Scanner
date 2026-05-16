# 🔍 Smart Port Scanner

A beginner-friendly cybersecurity project built using Python, Flask, HTML, and Socket Programming.

This web-based application scans open TCP ports on a target system and provides:
- Open port detection
- Service identification
- Risk level analysis
- Security suggestions

---

# 🚀 Features

✅ Scan custom IP addresses  
✅ Scan custom port ranges  
✅ Detect open TCP ports  
✅ Identify common services  
✅ Show risk levels  
✅ Display security recommendations  
✅ Clean cybersecurity-themed UI  
✅ Flask web interface  

---

# 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Socket Programming

---

# 📂 Project Structure

```text
Port-Scanner/
│
├── app.py
├── scanner.py
├── README.md
│
└── templates/
    └── index.html
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Port_Scanner.git
```

---

## 2️⃣ Navigate Into Project

```bash
cd Port_Scanner
```

---

## 3️⃣ Install Flask

```bash
pip install flask
```

For Kali Linux / WSL:

```bash
pip install --break-system-packages flask
```

---

# ▶️ Run Project

```bash
python3 app.py
```

---

# 🌐 Open In Browser

```text
http://127.0.0.1:5000
```

---

# 🧪 Example Test

Open another terminal:

```bash
nc -lvp 4444
```

Then scan:

| Field | Value |
|---|---|
| Target IP | 127.0.0.1 |
| Start Port | 1 |
| End Port | 5000 |

The scanner should detect:

```text
Port 4444 OPEN
```

---

# 📸 Features Preview

- Open Port Detection
- Risk Level Analysis
- Service Information
- Security Suggestions

---

# ⚠️ Ethical Use Disclaimer

This project is intended for:
- Educational purposes
- Personal lab environments
- Authorized systems only

Do NOT scan systems without permission.

---

# 📈 Future Improvements

- Multithreading for faster scanning
- Banner grabbing
- OS detection
- Export scan reports
- Login system
- Scan history
- Nmap-style scanning
- Dark hacker dashboard UI

---

# 👨‍💻 Author

Shreyash Deore  
Computer Engineering Student | Cybersecurity Enthusiast

---

# ⭐ If you like this project

Give it a ⭐ on GitHub
