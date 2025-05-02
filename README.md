# Bing Search Automation

This project automates Bing searches using Selenium, providing a script for both desktop and mobile search simulations.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

The project utilizes the Selenium library to automate Bing searches for a list of randomly selected words. The script includes two search scenarios: desktop and mobile mode. It can be used for testing and experimenting with web automation techniques.

## Features

- **Automated Bing searches** with Selenium for both desktop and mobile browsers.
- **Command-line customization**: Specify the number of searches to perform (e.g., `python search_pc.py 15` or `python search_mobile.py 5`).
- **Human-like interaction patterns**:
  - Variable typing speed with random delays between keystrokes
  - Natural pauses before submitting searches
  - Occasional "thinking" pauses during search sessions
  - Random scrolling behavior on search results
- **Mobile emulation** with realistic device properties and responsive behavior.
- **Randomized behavior** to create more natural search patterns:
  - Variable wait times between searches
  - Random selection of search terms
  - Different scrolling depths on results pages
- **Robust error handling** with detailed logging for troubleshooting.
- **Cross-platform compatibility** supporting Windows, macOS, and Linux environments.
- **Enhanced browser automation stealth**:
  - Disables automation flags and indicators
  - Modifies browser fingerprinting to avoid detection
  - Implements custom JavaScript to mask WebDriver presence
  - Simulates genuine user behavior patterns to evade bot detection systems

## Getting Started

### Prerequisites

- Python installed on your machine.
- Required Python packages: `selenium` for web automation, `requests` for HTTP requests.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ethan4thewin/BingSearchAutomation.git
   ```

2. Download Edge WebDriver and Firefox WebDriver:

   Download Edge web driver from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver. Most of the time, the stable channel is the right choice.

   We may also want Firefox web driver Geckodriver for mobile browsing emulating (currently it is Edge for this). Link for downloading Mozilla Firefox geckodriver is https://github.com/mozilla/geckodriver/releases; choose the appropriate one for your computer architecture.

   In any case, find the one that works best for you and put the file into the repository location.

3. Install dependencies:

   ```bash
   pip install selenium
   pip install requests
   ```

### Usage

Execute the desktop search script:

```bash
python search_pc.py
```

Execute the mobile search script:

```bash
python search_mobile.py
```

Perform a certain number of searches:

```bash
python search_pc.py 4
python search_mobile.py 2
```

### Contributing & Troubleshooting

Contributions are welcome! Feel free to open issues or pull requests.

### License

This project is licensed under the MIT License.
