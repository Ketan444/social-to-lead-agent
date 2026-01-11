# Social-to-Lead Agentic Workflow


This project was built as part of a technical assignment for the Machine Learning Intern role at ServiceHive.

The goal of this project is to build a simple, real-world conversational AI agent for a fictional SaaS product called **AutoStream**. The agent answers product-related questions, identifies high-intent users, and captures leads in a structured way.

I intentionally kept the design simple and easy to explain, focusing on clarity, reliability, and real-world usability rather than over-engineering.

---

## Product Overview – AutoStream

AutoStream is a SaaS platform for automated video editing for content creators.

### Plans
**Basic Plan**
- $29/month
- 10 videos per month
- 720p resolution

**Pro Plan**
- $79/month
- Unlimited videos
- 4K resolution
- AI captions
- 24/7 priority support

### Policies
- No refunds after 7 days
- 24/7 support available only for Pro users

All product information is stored locally and used by the agent while responding to user queries.

---

## How the Agent Works

The agent follows a simple conversational flow:

1. Detects the user’s intent (greeting, product query, or high intent).
2. Answers pricing and feature-related questions using a local knowledge base.
3. Identifies high-intent users who want to sign up.
4. Collects lead details step by step (name, email, platform).
5. Calls a mock lead capture function only after all details are collected.

Conversation state is maintained across multiple turns to ensure a smooth lead capture experience.

---

## Project Structure

