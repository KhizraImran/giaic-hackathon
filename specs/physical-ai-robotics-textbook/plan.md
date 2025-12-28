# Implementation Plan: Physical AI & Humanoid Robotics Textbook

**Branch**: `feature/physical-ai-robotics-textbook` | **Date**: 2025-11-30 | **Spec**: specs/physical-ai-robotics-textbook/spec.md
**Input**: Feature specification from `/specs/physical-ai-robotics-textbook/spec.md`

## Summary

This plan outlines the architecture and implementation steps for creating a Physical AI & Humanoid Robotics Textbook. The project involves building a Docusaurus-based book, integrating a Retrieval-Augmented Generation (RAG) chatbot using FastAPI, Gemini API, Neon Serverless Postgres, and Qdrant Cloud. Additionally, it details the implementation of bonus features such as reusable Claude Code intelligence, user authentication via better-auth.com, content personalization, and Urdu translation.

## Technical Context

**Language/Version**: TypeScript (for Docusaurus frontend), Python 3.10+ (for FastAPI backend and Claude Code agents)
**Primary Dependencies**: Docusaurus, React, Gemini API, FastAPI, SQLAlchemy, Neon Postgres driver, Qdrant Client, better-auth.com SDK (if available or direct API integration)
**Storage**: Neon Serverless Postgres (for user data, personalization settings), Qdrant Cloud (for vector embeddings of book content)
**Testing**: Jest/React Testing Library (for Docusaurus components), Pytest (for FastAPI backend and agents), potentially Playwright/Cypress for E2E tests.
**Target Platform**: Web (Docusaurus deployed on GitHub Pages), Serverless (FastAPI backend)
**Project Type**: Web application with an AI-driven backend
**Performance Goals**:
- Docusaurus site loads within 2 seconds (p95).
- Chatbot responses within 5 seconds (p95).
- User authentication/personalization actions within 3 seconds (p95).
**Constraints**:
- Must use specified technologies: Docusaurus, GitHub Pages, Claude Code, Spec-Kit Plus, Gemini API, FastAPI, Neon Serverless Postgres, Qdrant Cloud Free Tier, better-auth.com.
- Chatbot must answer questions *only* from book content.
- Bonus features should be optional but integrated gracefully.
**Scale/Scope**: Single textbook deployment, designed for educational use. Initial scope targets ~1000 active users, with consideration for future scaling.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development**: Adhered to. This plan directly follows `spec.md` and leverages Spec-Kit Plus/Claude Code.
- **II. AI-Native Content and Tooling**: Adhered to. The plan explicitly includes a RAG chatbot and reusable Claude Code intelligence.
- **III. Docusaurus for Content, GitHub Pages for Deployment**: Adhered to. Docusaurus and GitHub Pages are central to the book deployment.
- **IV. Integrated RAG Chatbot**: Adhered to. The plan specifies the required technical stack for the chatbot.
- **V. Reusable Intelligence**: Adhered to. Bonus points encourage explicit development of Subagents/Skills.
- **VI. User-Centric Features**: Adhered to. Authentication, personalization, and translation are included as optional features.

## Project Structure

```text
./
├── .claude/                                  # Claude Code specific configurations
├── .github/workflows/                        # GitHub Actions for CI/CD (Docusaurus deploy, etc.)
├── .specify/                                 # SpecKit Plus templates and scripts
├── docs/                                     # Docusaurus content (chapters, modules)
├── src/                                      # Docusaurus frontend components/styles
├── static/                                   # Docusaurus static assets
├── blog/                                     # Docusaurus blog (optional)
├── docusaurus.config.js                      # Docusaurus configuration
├── package.json                              # Docusaurus dependencies
├── chatbot_backend/                          # FastAPI backend for RAG chatbot
│   ├── app/                                  # FastAPI application code
│   │   ├── api/                              # API endpoints
│   │   ├── services/                         # Business logic, OpenAI/Qdrant integration
│   │   ├── models/                           # Pydantic models, database models
│   │   └── main.py                           # FastAPI app entry point
│   ├── tests/                                # Pytest tests for backend
│   ├── .env.example                          # Environment variables
│   └── requirements.txt                      # Python dependencies
├── agents/                                   # Claude Code Subagents and Agent Skills (bonus)
│   ├── subagent_rag/                         # Example RAG subagent
│   └── skill_translate/                      # Example translation skill
├── specs/                                    # Feature specifications (this feature)
│   └── physical-ai-robotics-textbook/
│       ├── spec.md                           # This feature's specification
│       ├── plan.md                           # This file
│       └── tasks.md                          # Implementation tasks
├── history/
│   ├── prompts/                              # Prompt history records
│   └── adr/                                  # Architectural Decision Records
├── node_modules/                             # Docusaurus JS dependencies
├── .gitignore
├── CLAUDE.md                                 # Claude Code instructions
├── Hackathon I_ Physical AI & Humanoid Robotics Textbook.md  # Original hackathon brief
└── README.md                                 # Project README
```

**Structure Decision**: The project will adopt a monorepo-like structure where the Docusaurus frontend, FastAPI backend for the chatbot, and Claude Code agents/skills reside in separate top-level directories (`docs/`, `src/`, `chatbot_backend/`, `agents/`). This separation facilitates independent development and deployment of the different components while maintaining a unified project context. The Docusaurus `docs/` and `src/` will handle the book content and UI. The `chatbot_backend/` will contain the FastAPI application and its logic for RAG. `agents/` will house the bonus Claude Code reusable intelligence. Standard SpecKit Plus directories like `specs/`, `history/`, and `.specify/` will be maintained.