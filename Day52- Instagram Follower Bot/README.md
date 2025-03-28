# 🚀 Instagram Follower Bot  

This Python bot automates the process of finding and following Instagram users from a specific account's followers list. It uses **Selenium** to interact with the Instagram web interface.

---

## 📜 Features  
✅ **Automated Login** – Logs into your Instagram account securely.  
✅ **Find Followers** – Fetches followers of a specific account.  
✅ **Auto-Follow** – Clicks the "Follow" button for each user.  
✅ **Avoids Bot Detection** – Uses randomized delays and exception handling.  
✅ **Handles Pop-ups** – Dismisses Instagram's save login and notification prompts.  
✅ **Closes Browser After Execution**  

---

## 📦 Installation  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/lipivirmani/Day52_Instagram_Follower_Bot.git
cd Day52_Instagram_Follower_Bot
```

### 2️⃣ **Install Dependencies**  
Ensure you have Python installed, then install the required libraries:  
```bash
pip install selenium
```

### 3️⃣ **Download WebDriver**  
- Install [ChromeDriver](https://chromedriver.chromium.org/downloads) that matches your Chrome version.  
- Place it in the project directory or set it in the system PATH.

---

## 🛠️ Usage  

### **1️⃣ Update Credentials**
Edit the `USERNAME` and `PASSWORD` fields in `bot.py`:
```python
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"
```

### **2️⃣ Choose a Target Account**
Update the `SIMILAR_ACCOUNT` variable with the account whose followers you want to follow:
```python
SIMILAR_ACCOUNT = "Businessbrite"
```

### **3️⃣ Run the Bot**
```bash
python bot.py
```

---

## 🛡️ Disclaimer  
This bot **violates Instagram's terms of service** if misused. Use responsibly, and avoid aggressive automation to prevent account bans.  

🚨 **Use at your own risk!** 🚨

---

## 👨‍💻 Author  
**Lipi Virmani**  
📧 Lipivirmani182@gmail.com  
🔗 [GitHub Profile](https://github.com/lipivirmani)

---

## 📜 License  
This project is licensed under the MIT License.
```
