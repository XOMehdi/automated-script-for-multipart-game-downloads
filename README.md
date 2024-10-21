# Automated Download Script for Multipart Game Downloads

## Overview
This repository contains a Python script that automates the downloading of games from websites that host multi-part downloads. Using Selenium, the script navigates the website, interacts with necessary elements, and downloads each part sequentially.

## Features
- Automates the download process for games divided into multiple parts.
- Configurable parameters for wait times and number of parallel downloads.
- Supports easy adaptation for similar game download sites.

## Requirements
- Python 3.x
- Selenium library
- Chrome WebDriver
- Any download manager with the browser extension

## Setup
1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Install Selenium**: Install the Selenium library by running:
   ```bash
   pip install selenium
3. **Download Chrome WebDriver**: Make sure to have the Chrome WebDriver that matches your Chrome version.

### Optional
4. **Set up your downloader manager**: Install a Download Manager and enable the IDM extension for Chrome.
5. **Update the Script**: Modify the EXTENSION_PATH constant in the script to point to the location of the extension on your machine.


## Important Notes
- Be sure to respect the website's terms of service when using automated scripts.
- The script may require adjustments based on changes to the website's layout or functionality.
- Ensure that the CSS selectors and element IDs in the script match those of the target site.
