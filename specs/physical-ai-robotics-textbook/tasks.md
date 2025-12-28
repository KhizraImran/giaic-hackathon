---

description: "Task list for Physical AI & Humanoid Robotics Textbook implementation"
---

# Tasks: Physical AI & Humanoid Robotics Textbook

**Input**: Design documents from `/specs/physical-ai-robotics-textbook/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: All major features will have associated tests.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below assume the structure defined in `plan.md`.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create Docusaurus project: `npx create-docusaurus@latest website classic`
- [ ] T002 Initialize `chatbot_backend/` as a Python project with FastAPI dependencies (`requirements.txt`)
- [ ] T003 [P] Configure initial `.gitignore` for both Docusaurus and FastAPI projects
- [ ] T004 [P] Create `agents/` directory for Claude Code Subagents and Skills

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Set up Neon Serverless Postgres database and obtain connection string
- [ ] T006 Configure Qdrant Cloud Free Tier and obtain API key
- [ ] T007 Initialize database clients in `chatbot_backend/app/services/database.py` for Neon and `chatbot_backend/app/services/qdrant.py` for Qdrant
- [ ] T008 [P] Implement basic FastAPI app structure in `chatbot_backend/app/main.py`
- [ ] T009 Create a base Claude Code agent structure in `agents/base_agent.py` (if common logic is required)
- [ ] T010 Configure environment variable loading for `chatbot_backend/` (e.g., `.env` file)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - AI/Spec-Driven Book Creation (P1) 🎯 MVP

**Goal**: Deployable Docusaurus textbook with initial content.

**Independent Test**: The Docusaurus site is accessible via GitHub Pages, displaying the "Physical AI & Humanoid Robotics" course details and modules.

### Tests for User Story 1

- [ ] T011 [US1] Run Docusaurus build command (`npm run build`) and assert no errors.
- [ ] T012 [US1] Manually verify deployed GitHub Pages site loads correctly.

### Implementation for User Story 1

- [ ] T013 [P] [US1] Populate `docs/introduction.md` with an overview of Physical AI & Humanoid Robotics from the hackathon brief.
- [ ] T014 [P] [US1] Create `docs/module1_ros2.md` with content for Module 1 (The Robotic Nervous System (ROS 2)).
- [ ] T015 [P] [US1] Create `docs/module2_digital_twin.md` with content for Module 2 (The Digital Twin (Gazebo & Unity)).
- [ ] T016 [P] [US1] Create `docs/module3_ai_robot_brain.md` with content for Module 3 (The AI-Robot Brain (NVIDIA Isaac™)).
- [ ] T017 [P] [US1] Create `docs/module4_vla.md` with content for Module 4 (Vision-Language-Action (VLA)).
- [ ] T018 [P] [US1] Create `docs/assessments.md` and `docs/hardware_requirements.md` based on the brief.
- [ ] T019 [US1] Configure Docusaurus `docusaurus.config.js` to include all created markdown files in the sidebar.
- [ ] T020 [US1] Set up GitHub Actions workflow (`.github/workflows/deploy.yml`) for deploying Docusaurus to GitHub Pages.

**Checkpoint**: User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Integrated RAG Chatbot (P1)

**Goal**: A functional RAG chatbot embedded within the Docusaurus book that answers questions based on its content.

**Independent Test**: The chatbot UI is visible and interactive in the deployed book. When asked a question about a specific chapter, it provides an accurate answer.

### Tests for User Story 2

- [X] T021 [US2] Unit test for Qdrant client connection and upsertion in `chatbot_backend/app/services/qdrant.py`.
- [X] T022 [US2] Integration test for FastAPI RAG endpoint (simulating a query and verifying response format) in `chatbot_backend/tests/test_rag.py`.
- [X] T023 [US2] End-to-end test: Ask chatbot a question in the UI and verify response.

### Implementation for User Story 2

- [X] T024 [US2] Develop content ingestion script (`scripts/ingest_docs.py`) to parse Docusaurus markdown and create embeddings with Gemini, then store in Qdrant.
- [X] T025 [US2] Implement RAG service in `chatbot_backend/app/services/rag_service.py` (query Qdrant, call Gemini Chat, format response).
- [X] T026 [US2] Create FastAPI endpoint `/chat` in `chatbot_backend/app/api/endpoints/chat.py` to expose RAG service.
- [X] T027 [P] [US2] Design and implement Docusaurus React component for chatbot UI in `src/components/Chatbot.js`.
- [X] T028 [US2] Integrate chatbot component into Docusaurus layout or specific pages (`src/theme/Layout/index.js`).
- [X] T029 [US2] Implement frontend logic to send selected text to the chatbot along with a query.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Reusable Intelligence via Claude Code Subagents and Agent Skills (P2)

**Goal**: Demonstrate reusable AI components for development tasks.

**Independent Test**: A created Subagent/Skill can be invoked via Claude Code and successfully performs its intended function (e.g., summarizing a chapter).

### Tests for User Story 3

- [ ] T030 [US3] Unit test for the custom Claude Code Subagent logic (e.g., `agents/subagent_chapter_summarizer/agent.py`).
- [ ] T031 [US3] Manually invoke the developed Subagent/Skill through Claude Code and verify output.

### Implementation for User Story 3

- [ ] T032 [US3] Create a Claude Code Subagent in `agents/subagent_chapter_summarizer/` to summarize a given chapter from the book.
- [ ] T033 [US3] Create a Claude Code Agent Skill in `agents/skill_code_snippet_explainer/` to explain a code snippet from the book.
- [ ] T034 [US3] Document how to use the created Subagents/Skills in a `README.md` within their respective directories.

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - User Authentication (Signup/Signin) (Priority: P2)

**Goal**: Implement user authentication with better-auth.com, collecting user background.

**Independent Test**: Users can sign up, log in, and their software/hardware background is stored and retrievable.

### Tests for User Story 4

- [ ] T035 [US4] Integration test for user registration (sending data to better-auth.com and verifying database storage).
- [ ] T036 [US4] Integration test for user login and session management.

### Implementation for User Story 4

- [ ] T037 [US4] Integrate better-auth.com SDK/API into `chatbot_backend/app/services/auth_service.py`.
- [ ] T038 [US4] Create FastAPI endpoints `/signup` and `/signin` in `chatbot_backend/app/api/endpoints/auth.py`.
- [ ] T039 [US4] Implement user model in `chatbot_backend/app/models/user.py` to store background information (software, hardware).
- [ ] T040 [P] [US4] Create Docusaurus React components for Signup and Signin forms in `src/components/AuthForms.js`.
- [ ] T041 [US4] Add client-side logic for authentication flows in Docusaurus.

---

## Phase 7: User Story 5 - Content Personalization (Priority: P3)

**Goal**: Allow logged-in users to personalize chapter content.

**Independent Test**: A logged-in user can toggle personalization, and a specific chapter's content visibly adapts based on their stored background.

### Tests for User Story 5

- [ ] T042 [US5] Unit test for backend content personalization logic (e.g., `chatbot_backend/app/services/personalization.py`).
- [ ] T043 [US5] End-to-end test: Log in, set a background, personalize a chapter, and verify content change.

### Implementation for User Story 5

- [ ] T044 [US5] Implement FastAPI endpoint `/personalize/{chapter_id}` in `chatbot_backend/app/api/endpoints/personalization.py` to dynamically adjust content based on user background.
- [ ] T045 [US5] Develop backend logic in `chatbot_backend/app/services/personalization.py` to fetch user background and modify chapter text (e.g., add/remove details, simplify explanations).
- [ ] T046 [P] [US5] Create a Docusaurus React component for a "Personalize Content" button at the start of each chapter (`src/components/PersonalizationToggle.js`).
- [ ] T047 [US5] Implement frontend integration to send personalization requests to the backend and display updated content.

---

## Phase 8: User Story 6 - Urdu Translation (Priority: P3)

**Goal**: Allow logged-in users to translate chapter content into Urdu.

**Independent Test**: A logged-in user can toggle Urdu translation, and a specific chapter's content is accurately rendered in Urdu.

### Tests for User Story 6

- [ ] T048 [US6] Unit test for translation service (e.g., `chatbot_backend/app/services/translation.py`).
- [ ] T049 [US6] End-to-end test: Log in, toggle Urdu translation for a chapter, and verify translated content.

### Implementation for User Story 6

- [ ] T050 [US6] Implement FastAPI endpoint `/translate/{chapter_id}` in `chatbot_backend/app/api/endpoints/translation.py` for Urdu translation.
- [ ] T051 [US6] Develop backend logic in `chatbot_backend/app/services/translation.py` using an LLM or translation API to translate chapter content to Urdu.
- [ ] T052 [P] [US6] Create a Docusaurus React component for a "Translate to Urdu" button at the start of each chapter (`src/components/TranslationToggle.js`).
- [ ] T053 [US6] Implement frontend integration to send translation requests and display Urdu content.

---

## Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T054 [P] Documentation updates for API endpoints and new components.
- [ ] T055 Code cleanup and refactoring across all implemented components.
- [ ] T056 Security hardening for FastAPI backend (input validation, rate limiting, etc.).
- [ ] T057 Configure CI/CD for FastAPI backend deployment (e.g., to a serverless platform).
- [ ] T058 Ensure all environment variables are properly managed and not hardcoded.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories (though it interacts with US1's content)
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Depends on User Story 4 (Authentication) for user profiles.
- **User Story 6 (P3)**: Can start after Foundational (Phase 2) - No direct dependency on other stories, but benefits from US4 (Authentication) for logged-in user experience.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, User Stories 1, 2, 3, 4, 6 can start in parallel (US5 depends on US4)
- All tests for a user story marked [P] can run in parallel
- Components within a story marked [P] (e.g., Docusaurus components) can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Deployable Book)
4. Complete Phase 4: User Story 2 (Integrated RAG Chatbot)
5. **STOP and VALIDATE**: Test User Stories 1 & 2 independently and together.
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (Enhanced MVP!)
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 (depends on US4) → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Book Content & Deployment)
   - Developer B: User Story 2 (RAG Chatbot Backend & Integration)
   - Developer C: User Story 3 (Claude Code Agents) and User Story 6 (Urdu Translation)
   - Developer D: User Story 4 (Authentication) then User Story 5 (Personalization)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
