
# 🐺 GateHound - A Lightweight, Clean Port Scanner by blody

**GateHound** is a minimalistic yet powerful TCP port scanner built using Python's socket programming capabilities. Designed primarily for learners, security enthusiasts, and penetration testers in training, GateHound offers a clean, easy-to-understand interface and practical functionality to explore the basics of network port scanning.

This tool helps you identify which ports are open or closed on a target host by attempting TCP connections, allowing you to gain insight into running services and potential vulnerabilities.

---

## 🔧 Features

- **Predefined Common Ports:** Scans a carefully selected list of commonly used TCP ports including HTTP, FTP, SSH, DNS, SMTP, and database ports to provide a quick overview of typical service exposure.
- **User-Friendly Output:** Color-coded results using `colorama` library for easy differentiation between open and closed ports.
- **Input Validation:** Validates the target IP address to reduce errors and improve user experience.
- **Clear Banner and Informative Logs:** Displays a professional ASCII art banner and timestamps the scanning process for transparency.
- **Graceful Interruption Handling:** Allows users to safely stop scanning with keyboard interrupts (`Ctrl+C`), ensuring the program exits cleanly.
- **Lightweight and Fast:** Uses a short socket timeout to scan ports efficiently without hanging on unresponsive targets.

---

## 🚀 Installation & Usage

### Requirements:
- Python 3.x installed on your system
- `colorama` package (for colored terminal output)

To install `colorama`, run:
```bash
pip install colorama
```

### Running GateHound:

Open your terminal or command prompt and run:

```bash
python gatehound.py <target_ip>
```

Replace `<target_ip>` with the IP address of the machine or server you want to scan.

**Example:**

```bash
python gatehound.py 192.168.1.1
```

This will start scanning the predefined ports on the specified host and print the results in real-time.

---

## ⚠️ Important Notes and Disclaimer

- **Educational Use Only:** This tool is intended solely for learning and authorized testing purposes.
- **Legal Compliance:** Do **not** scan networks or systems without explicit permission from the owner. Unauthorized scanning can be illegal and is punishable under various laws worldwide.
- **Network Impact:** Although lightweight, running port scans may trigger alerts on firewalls and intrusion detection systems. Use responsibly.
- **No Warranty:** This tool is provided "as-is" with no guarantees regarding accuracy or completeness.

---

## 🛠️ How It Works (Brief Technical Overview)

- The scanner attempts TCP connections to each port in the predefined list using Python’s `socket` module.
- If the connection is successful (`connect_ex()` returns 0), the port is considered **open**.
- If the connection fails or times out, the port is marked as **closed**.
- The scan uses a short timeout to avoid delays on ports that do not respond.
- The output is color-coded: **green** for open ports, **red** for closed ports.

---

## 📚 Who Should Use GateHound?

- **Beginners** interested in learning network programming and cybersecurity fundamentals.
- **Penetration testers in training** who want a simple tool to practice scanning.
- **Developers** and **system administrators** who want a quick way to check their systems.
- **Anyone curious** about how port scanning works!

---

## 👨‍💻 About the Author

Created and maintained by [blody](https://github.com/iamblody)  
Follow me on Instagram: [@blody.sh](https://instagram.com/blody.sh)  

---

## 📢 Contributions & Feedback

I welcome pull requests, suggestions, and feedback to improve GateHound. Feel free to open issues or contribute on GitHub.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
