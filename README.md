# Vera Message Engine (magicpin AI Challenge)

A FastAPI-based intelligent messaging engine that generates contextual, high-conversion merchant engagement messages based on triggers, category insights, and merchant data.

---

## Live Demo

https://magicpin-bot-ceg3.onrender.com

API Docs:
https://magicpin-bot-ceg3.onrender.com/docs

---

## Problem Statement

Build a system that:
- Detects business triggers (e.g., search spikes)
- Generates personalized messages for merchants
- Handles merchant replies intelligently
- Avoids spam & auto-replies
- Converts intent into action

---

## Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Rule-based logic
- Render (Deployment)
- GitHub (Version Control)

---

## API Endpoints

### Health Check
GET /v1/healthz

### Metadata
GET /v1/metadata

### Context Store
POST /v1/context

### Trigger Processing
POST /v1/tick

### Merchant Reply Handling
POST /v1/reply

---

## Core Features

### Context-Aware Messaging
Generates campaign messages based on:
- Category
- Merchant performance
- Trigger signals

---

### Auto-Reply Detection
Detects patterns like:
"Thank you for contacting..."
Automatically ends conversation

---

### Intent Detection
Recognizes signals like:
- yes
- ok
- sure
- do it

Converts into campaign execution

---

### Hostile Handling
Detects messages like:
- stop
- spam
- do not

Immediately stops messaging

---

### Smart Waiting Logic
Avoids spamming by:
- Waiting 30 seconds between attempts
- Ending conversation when needed

---

## Evaluation Results

All judge scenarios passed successfully:

- Warmup
- Auto-reply detection
- Intent transition
- Hostile handling

---

## Deployment

https://magicpin-bot-ceg3.onrender.com

---

## Setup Instructions

### Clone Repository
git clone https://github.com/hariomkushwaha-1217/magicpin-bot.git
cd magicpin-bot

### Install Dependencies
pip install -r requirements.txt

### Run Server
uvicorn main:app --reload

---

## Author

Hari Om Kushwaha  
B.Tech CSE (2021–2025)  
Java Full Stack Developer  

---

## Final Status

Project Completed  
Successfully Deployed  
All Tests Passed  
Ready for Submission
