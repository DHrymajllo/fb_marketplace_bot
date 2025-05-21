# Facebook Marketplace Bot

<p align="center">
  <img src="https://i.postimg.cc/rsFn1BbS/Adobe-Express-file.png" />
</p>

This bot searches for listings (e.g. bikes) in the Łódź area and sends a message to sellers on Facebook Marketplace.

## 🔧 Requirements

- Python 3.9+
- Chrome + ChromeDriver installed
- `selenium` package

## 🧠 Features

- Sends up to 20 messages per day
- Avoids duplicates using SQLite
- Simple config file for customization

## 🚀 Usage

1. Install dependencies:
   ```bash
   pip install selenium
   ```
1. Change path to chromedriver.exe (selenium) in code:
   ```bash
   service = Service("C:/PathToSeleniumDriver/chromedriver.exe")
   ```
   
3. Run the bot:
   ```bash
   python bot.py
   ```

3. Log in manually to Facebook when prompted.



https://github.com/user-attachments/assets/7940d3f1-99e3-4b29-bd2b-589fc8641368



