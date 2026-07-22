# LittleSoul

> A tiny Chinese Transformer chatbot built completely from scratch using PyTorch.

LittleSoul is a lightweight Chinese Transformer project implemented from scratch without relying on Hugging Face or any pre-trained language models.

The project was originally created as a learning project for understanding how language models work internally, and is gradually evolving into a lightweight framework for training small domain-specific language models.

---

# Features

- ✅ Character-level Tokenizer
- ✅ Transformer implemented from scratch
- ✅ Pure PyTorch implementation
- ✅ Autoregressive text generation
- ✅ Personality Memory Retrieval
- ✅ Input normalization
- ✅ Stable dialogue framework
- ✅ 100/100 Memory Test Passed

---

# Project Structure

```
LittleSoul
│
├── dataset/
│   └── emotion.jsonl
│
├── tokenizer/
│   └── vocab_char.json
│
├── src/
│   ├── chat.py
│   ├── train.py
│   ├── model.py
│   ├── transformer.py
│   ├── tokenizer.py
│   ├── dataset.py
│   ├── memory.py
│   ├── test_all_memory.py
│   └── ...
│
├── little_soul_final.pt
│
├── requirements.txt
│
└── README.md
```

---

# Quick Start

## Install

```bash
pip install -r requirements.txt
```

---

## Train

```bash
python src/train.py
```

---

## Chat

```bash
python src/chat.py
```

---

# Example

```
You:
今天工作很累。

LittleSoul:
嗯...想把脑袋靠过来吗？我在这。
```

```
You:
晚安。

LittleSoul:
晚安，好梦。
```

---

# Architecture

```
               User Input
                    │
                    ▼
           Input Normalization
                    │
                    ▼
             Memory Retrieval
             │              │
             │              │
        Memory Hit     Memory Miss
             │              │
             ▼              ▼
      Fixed Response   Transformer
                    │
                    ▼
              Final Response
```

---

# Why Memory Retrieval?

Small language models trained with limited datasets often produce unstable responses.

LittleSoul introduces a lightweight Memory Retrieval layer before generation.

This allows the model to:

- Keep personality consistent
- Produce deterministic replies for known conversations
- Use Transformer generation only when memory is unavailable

This architecture significantly improves dialogue stability while keeping the model lightweight.

---

# Current Version

Version:

```
v0.1 Stable
```

Current capabilities:

- Character Tokenizer
- Transformer
- Stable Memory Retrieval
- Chinese Dialogue
- Small Dataset Training

---

# Roadmap

## v0.2

- Temperature Sampling
- Top-K Sampling
- Repeat Penalty

## v0.3

- Semantic Memory Retrieval
- Similarity Search

## v0.4

- Larger Dataset
- Better Generalization

## v1.0

LittleSoul Framework

A lightweight framework for training domain-specific language models.

---

# Future Vision

LittleSoul is not intended to become another large language model.

Instead, the long-term goal is to build a lightweight framework capable of training specialized AI models for different domains, such as:

- Medical Assistant
- Legal Assistant
- NPC Dialogue
- Customer Service
- Emotional Companion

using the same underlying architecture.

---

# License

MIT License