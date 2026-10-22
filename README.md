# Log Analyzer

A small Python tool that reads a log file, counts failed logins per IP address, and alerts on suspicious activity.

## Features
- Reads any log file you name
- Counts failed logins per IP
- Alerts when an IP reaches a limit you choose
- Handles missing files and bad input

## How to run
python analyzer.py

Then enter the log file name (for example auth.log) and the alert limit.
