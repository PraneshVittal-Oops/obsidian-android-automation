# Obsidian Mobile QA Automation (Android)

## Overview
This project demonstrates a lightweight multi-agent mobile QA automation system
using Android Emulator + ADB. The system validates real application behavior
using Obsidian Android as a target app.

## Architecture
- **Planner Agent**: Converts natural language test goals into executable steps
- **Executor Agent**: Executes steps using ADB commands on a running emulator

## Test Flow
1. Launch Obsidian via ADB
2. Create a note (UI placeholder)
3. Enter text into the note
4. Verify persistence via device storage

## Tools & Tech
- Android Emulator (Pixel 6, Android 14)
- ADB
- Python 3
- Obsidian Android app

## How to Run
```bash
cd obsidian_automation
python run_obsidian_test.py
