# Fake Identity Generator

This Python script creates **purely fictional** identities (names, emails,
addresses, credit-card numbers, etc.) for **testing and educational purposes only**.

---

## ⚠️ Disclaimer
All data produced by this program is randomly generated and **not real**.  
Do **not** use it to impersonate anyone or for any illegal activity.  
The author assumes **no responsibility for misuse**.

---

## Features
- Generates full profiles: personal info, contact data, fake government IDs,
  financial details, online presence, and more.
- Saves each generated identity as a JSON file with a timestamp.
- Command-line argument to create up to **10 identities** in one run.

Example:
```bash
python fake.py 5
````

Generates 5 completely fake identities and stores them as JSON files.

---

## Installation & Usage

### Requirements

* **Python 3.7+**
* The [`faker`](https://pypi.org/project/Faker/) library

### Windows

1. **Install Python 3**
   Download from [python.org](https://www.python.org/downloads/) and during setup
   tick the box **“Add Python to PATH”**.

2. **Download the project**
   Clone with git or download the ZIP and extract it.

3. **Install the required library**
   Open a Command Prompt in the project folder and run:

   ```bash
   pip install faker
   ```

4. **Run the generator**

   ```bash
   python fake.py
   ```

   or to generate multiple identities:

   ```bash
   python fake.py 5
   ```

---

### Linux

1. **Install Python 3 and pip**
   On Debian/Ubuntu:

   ```bash
   sudo apt install python3 python3-pip
   ```

2. **Download the project**
   Clone the repository or download the ZIP.

3. **Install the required library**
   In the project folder run:

   ```bash
   pip3 install faker
   ```

   *(If your distribution enforces PEP 668 and blocks system-wide installs,
   you can create a virtual environment instead:
   `python3 -m venv venv && source venv/bin/activate && pip install faker`)*

4. **Run the generator**

   ```bash
   python3 fake.py
   ```

   or to generate several identities:

   ```bash
   python3 fake.py 5
   ```

---

## License

MIT License (or any other OSI-approved license of your choice).
Include a `LICENSE` file if you want to specify usage rights clearly.

---

## Notes

* Credit-card numbers, SSNs, and other fields are **not valid** and intended
  only for **software demos, database testing, and UI mockups**.
* This project was created quickly as a simple utility; updates may follow.
