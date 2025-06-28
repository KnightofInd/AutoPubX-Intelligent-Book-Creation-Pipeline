# Automated-Book-Publication-Workflow

# 📘 Automated Book Publication Workflow

An intelligent and automated pipeline to extract book chapters from the web, rewrite ("spin") them using AI, enable iterative human input, and store final outputs with version control and intelligent retrieval.

---

## 🧭 Table of Contents

- [🔍 Introduction](#-introduction)  
- [✨ Features](#-features)  
- [🧰 Tech Stack](#-tech-stack)  
- [🏗️ Architecture](#-architecture)  
- [⚙️ Installation](#-installation)  
- [🛠️ Configuration](#-configuration)  
- [🚀 Usage](#-usage)  
- [📚 Workflow Example](#-workflow-example)  
- [📦 Dependencies](#-dependencies)  
- [👥 Contributors](#-contributors)  
- [🪪 License](#-license)  
- [🐞 Troubleshooting](#-troubleshooting)

---

## 🔍 Introduction

This project enables the automated transformation of public domain literature into AI-enhanced rewritten versions. Starting with chapter scraping and screenshots, it flows through AI-assisted writing and reviewing, facilitates human feedback loops, and stores version-controlled outputs using ChromaDB with intelligent search.

---

## ✨ Features

- **Web Scraping**: Extract chapter content and take full-page screenshots from a URL using Playwright.
- **AI Spinning & Reviewing**: Rewrite chapters with a large language model (LLM) and conduct AI-based peer reviews.
- **Human-in-the-Loop Workflow**: Supports multi-stage human editing before content is finalized.
- **Agent-Orchestrated Pipeline**: Inter-agent communication and decision flows managed via a custom agentic API.
- **Version Control & Retrieval**: Store and retrieve different versions using ChromaDB and reinforcement-learning (RL) based semantic search.

---

## 🧰 Tech Stack

| Tool/Library | Description | Logo |
|--------------|-------------|------|
| **[Gemini API](https://ai.google.dev/)** | Used for AI-driven chapter rewriting and reviewing | ![Gemini](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Google_Gemini_logo.svg/120px-Google_Gemini_logo.svg.png) |
| **[Playwright](https://playwright.dev/)** | Automates web scraping and screenshots | ![Playwright](https://playwright.dev/img/playwright-logo.svg) |
| **[Hugging Face Transformers](https://huggingface.co/transformers/)** | Optional models for additional NLP tasks | ![Transformers](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) |
| **[Python](https://www.python.org/)** | Core development language | ![Python](https://www.python.org/static/community_logos/python-logo.png) |
| **[ChromaDB](https://www.trychroma.com/)** | Vector database for storing and retrieving AI-enhanced content | ![ChromaDB](https://avatars.githubusercontent.com/u/111155219?s=200&v=4) |

---

## 🏗️ Architecture

```text
[ Scraper + Screenshot ]
           ↓
      [ AI Writer ]
           ↓
   [ Human Writer Pass ]
           ↓
     [ AI Reviewer ]
           ↓
   [ Human Reviewer Pass ]
           ↓
     [ Editor Finalizes ]
           ↓
[ ChromaDB + RL Search Integration ]

