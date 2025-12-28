# Physical AI & Humanoid Robotics Textbook Constitution

## Core Principles

### I. Spec-Driven Development
All project components, from the textbook content to the chatbot, will be developed using a strict spec-driven methodology. We will use Spec-Kit Plus to define specifications and Claude Code to drive the implementation, ensuring every piece of work is traceable to a requirement.

### II. AI-Native Content and Tooling
The project must be "AI-native." The textbook will be augmented with an integrated RAG chatbot to create an interactive learning experience. Development itself will be AI-driven, utilizing Claude Code agents and skills.

### III. Docusaurus for Content, GitHub Pages for Deployment
The textbook will be built using Docusaurus for a modern, maintainable documentation site. All content will be hosted and deployed via GitHub Pages for continuous integration and public accessibility.

### IV. Integrated RAG Chatbot
A core deliverable is an embedded Retrieval-Augmented Generation (RAG) chatbot. It must be capable of answering user questions based on the book's content. The specified technical stack (OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres, Qdrant) is mandatory.

### V. Reusable Intelligence
We will prioritize the creation of reusable intelligence. This will be implemented by developing Claude Code Subagents and Agent Skills. This approach is not only for bonus points but also for building a foundation for future projects.

### VI. User-Centric Features
While optional, building user-centric features is highly encouraged. This includes user authentication (Signup/Signin), content personalization based on user background, and translation capabilities to broaden accessibility.

## Technical Stack Requirements

The following technologies are mandated for the project:
- **Book Framework:** Docusaurus
- **Deployment:** GitHub Pages
- **Development Tool:** Claude Code with Spec-Kit Plus
- **Chatbot Backend:** FastAPI
- **Chatbot SDKs:** OpenAI Agents/ChatKit
- **Database:** Neon Serverless Postgres
- **Vector Store:** Qdrant Cloud (Free Tier)
- **Authentication:** better-auth.com

## Governance

This Constitution serves as the guiding document for the project. All development work, pull requests, and reviews must align with these principles. Any deviation requires discussion and a documented amendment to this constitution.

**Version**: 1.0 | **Ratified**: 2025-11-30 | **Last Amended**: 2025-11-30
