# MentorAI Architecture Documentation

**Project Name:** MentorAI

**Version:** 1.0 (Development)

**Document Type:** Software Architecture

**Authors:** Team MentorAI

---

# Vision

MentorAI is not an AI chatbot.

MentorAI is an AI Mentor that guides students throughout their complete learning journey.

Instead of simply answering questions, MentorAI acts as a:

- Teacher
- Mentor
- Planner
- Friend
- Motivation Coach
- Progress Tracker

The objective is to help students achieve long-term goals such as:

- GATE
- Placements
- UPSC
- GRE
- DSA
- AI/ML
- Web Development
- Competitive Programming

---

# Problem Statement

Most students fail because they:

- Don't know where to start.
- Don't have a mentor.
- Lose consistency.
- Forget previously learned topics.
- Don't track progress.
- Have no accountability.

Existing AI systems answer questions but do not mentor students over weeks or months.

MentorAI solves this problem by becoming a persistent AI mentor.

---

# High-Level Architecture

Student

↓

Discord

↓

Discord Bot

↓

Orchestrator

↓

Intent Classifier

↓

Decision Engine

↓

Task Router

↓

Agent

↓

Ollama (Qwen)

↓

Response

↓

Discord

---

# Core Components

## Discord Layer

Responsibilities:

- Receive messages
- Send responses
- Handle events
- User onboarding

---

## Orchestrator

Responsibilities:

- Coordinate the entire system
- Receive every user request
- Call the correct internal modules
- Return the final response

The Orchestrator never teaches or generates answers.

It only decides what should happen.

---

## Intent Classifier

Responsibilities:

Determine what the student wants.

Examples:

Input:

Explain Binary Search

↓

Intent:

STUDY

Input:

Give me a quiz

↓

Intent:

QUIZ

Input:

Good morning

↓

Intent:

GENERAL_CHAT

MentorAI uses a Hybrid Intent Classification approach.

Rule-Based detection is used first.

If confidence is low, Qwen determines the intent.

---

## Decision Engine

Responsibilities:

Determine the best action.

Example:

Student:

Explain Dynamic Programming

Decision Engine:

Check Memory

↓

Student never learned Recursion

↓

Recommend revising Recursion first

Instead of immediately teaching Dynamic Programming.

---

## Task Router

Responsibilities:

Select the correct AI Agent.

Example

STUDY

↓

Teacher Agent

QUIZ

↓

Quiz Agent

PROGRESS

↓

Analytics Agent

MOTIVATION

↓

Motivation Agent

---

## AI Agents

Teacher Agent

- Explain concepts
- Examples
- Practice Questions

Planner Agent

- Study Roadmaps
- Daily Goals
- Weekly Plans

Quiz Agent

- Generate quizzes
- Evaluate answers
- Update scores

Memory Agent

- Store Learning DNA
- Store progress
- Retrieve history

Reminder Agent

- Daily reminders
- Missed study reminders

Motivation Agent

- Encourage students
- Improve consistency

Analytics Agent

- Weekly reports
- Readiness Score
- Performance Graphs

---

# Learning DNA

Each student has a personalized profile called Learning DNA.

It stores:

- Goal
- Current Level
- Strong Topics
- Weak Topics
- Study Hours
- Learning Style
- Preferred Study Time
- Quiz Accuracy
- Consistency
- Revision History

Learning DNA is continuously updated.

---

# Memory System

MentorAI contains four types of memory.

Temporary Memory

Stores greetings and short conversations.

Session Memory

Stores today's study session.

Long-Term Memory

Stores progress and learning history.

Knowledge Memory

Stores resources and learning material.

---

# Technology Stack

Language

Python

Platform

Discord

AI Framework

LangGraph (Future)

Local LLM

Ollama

Model

Qwen 3

Database

PostgreSQL

Vector Database

ChromaDB

Backend

FastAPI

Version Control

Git + GitHub

---

# Architecture Decisions

## AD-001

Platform: Discord

Reason:

- Free
- Open Platform
- Community Support
- Rich API

---

## AD-002

Deployment: Local

Reason:

- Zero API Cost
- Privacy
- Offline Capability

---

## AD-003

LLM: Qwen 3 via Ollama

Reason:

- Open Source
- Good Coding Ability
- Good Reasoning
- Free

---

## AD-004

Intent Classification: Hybrid

Reason:

- Fast
- Scalable
- Low AI Usage

Rule-Based

↓

If uncertain

↓

Qwen

---

## AD-005

MentorAI thinks before responding.

Flow:

Understand

↓

Remember

↓

Decide

↓

Teach

Instead of:

Question

↓

Answer

---

# Development Status

Sprint 1

✅ Discord Bot

Sprint 2

✅ Modular Architecture

Sprint 3

✅ Local AI Integration

Sprint 4

🚧 Mentor Brain (In Progress)

---

# Future Work

- Multi-Agent System
- Learning DNA
- Dashboard
- Progress Tracking
- Reminder System
- Group Study
- Voice Mentor
- Mobile Companion App