# Batik Air Automation - Selenium Python

This project automates the ticket booking process on the [Batik Air website](https://www.batikair.com) using Selenium WebDriver and Python.

## 📂 Project Structure

batikair_automation/
├── pages/
│ └── landing_page.py # Page Object Model for the Batik Air site
├── tests/
│ └── test_book_ticket.py # Main test script
├── screenshots/ # Folder for failure screenshots (auto-created)
├── requirements.txt
└── README.md

## 🚀 Features

- Auto-dismiss cookie and popup modals
- Select departure & return cities
- Select departure & return dates
- Choose flights (economy)
- Input passenger name and phone number
- Select nationality (Indonesia)
- Proceed to payment page

## 🧩 Prerequisites

- Python 3.8 or newer
- Google Chrome installed

## 🛠️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/masteng0205/batikair_automation.git
   cd batikair_automation

2. Install dependencies
    ```bash
   pip install -r requirements.txt

## ▶️ How to Run the Test

``pytest -s tests/test_book_ticket.p
``

## 🛠️ Tech Stack
- Python
- Selenium WebDriver
- WebDriver Manager
- Page Object Model (POM) pattern

## 📌 Author
- Tengku Taufik
- GitHub: @masteng0205

---

Let me know if you'd like a version in Bahasa Indonesia or want to add badges (e.g. Python version, test status, etc).
