# ZenTasker Roadmap 

## 🚀 Vision
ZenTasker is on a mission to build a calm, accessible, distraction-free GTD task manager that supports focus and clarity for all users. This roadmap outlines our development priorities and phased goals.

---

## ✅ Phase 1: Foundation (MVP)
**Objective:** Build the core functionality and establish a solid, scalable foundation.

- ✅ Set up GitHub repo, documentation, and community guidelines
- ✅ Publish manifesto, design principles, and accessibility commitments
- ✅ Issue and PR templates in place
- **Backend:**
  - Flask app structure
  - Database models (Programme, Subproject, Next Action, Categories)
  - Basic authentication (single-user mode with future multi-user in mind)
  - File-based settings system (settings.yaml)
- **Frontend:**
  - React app scaffold with Tailwind CSS and internationalization setup
  - Minimal UI: Inbox, Project List, Next Action View
  - Gradual Reveal functionality
- Docker Compose for easy deployment
- Initial accessibility testing integration (axe, Lighthouse)

**Target:** Open alpha release for testing & contributor onboarding.

---

## ✅ Phase 2: Core GTD & Focus Features
**Objective:** Complete core GTD workflow support.

- Classical GTD mode toggle
- Weekly review checklist
- Context tagging and filters
- Defer/tickler system
- Focus Mode with Pomodoro timer
- Basic notifications (opt-in)
- Export to Markdown
- Logging completed actions with timestamps

**Target:** Stable beta release.

---

## 🚧 Phase 3: Plugin Architecture
**Objective:** Build a plugin framework to enable optional feature expansion.

- Dynamic plugin loading
- Plugin development documentation
- Example plugins:
  - Kanban View
  - Eisenhower Matrix
  - PARA Method
  - Time Blocking Planner
- Plugin governance guidelines published

**Target:** Public launch and outreach.

---

## 🚀 Phase 4: Accessibility & Neurodiverse Enhancements
**Objective:** Refine and expand inclusive design.

- Neurodiverse Mode: energy tagging, sequential reveal, micro-rewards
- Text-to-speech (Whisper integration)
- Switch-based navigation
- Keyboard shortcuts customization
- Expanded i18n support (community-led translations)

---

## 🌟 Future Enhancements (Post-Launch)
- Multi-user support with role-based access
- M365 integration (premium plugin)
- Zapier & IFTTT integration (premium plugins)
- Mobile app versions (React Native or Flutter)
- Community-curated plugin marketplace

> This roadmap will evolve with community feedback. Contributions, feature suggestions, and plugin ideas are welcome!
