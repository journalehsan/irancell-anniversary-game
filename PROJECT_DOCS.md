# 📚 PAC-IRANCELL Project Documentation

Welcome to the **PAC-IRANCELL 20th Anniversary Game** project! This document serves as an index for all project documentation and resources.

---

## 📖 Documentation Files

### 1. **ROADMAP.md** - Complete Project Plan
**Purpose:** Detailed 11-month development roadmap with 6 phases  
**Contains:**
- Phase-by-phase breakdown (Nov 2025 → Oct 2026)
- Milestones for each phase
- Deliverables and timelines
- Stretch goals and success metrics
- Team requirements and development workflow

**When to Use:**
- Planning long-term development strategy
- Understanding project scope and timeline
- Communicating with stakeholders
- Tracking overall progress

---

### 2. **CHECKLIST.md** - Implementation Checklist
**Purpose:** Actionable task checklist with checkboxes for each phase  
**Contains:**
- Per-phase task breakdown
- Specific deliverables
- Pre-launch final checklist
- Progress tracking

**When to Use:**
- Daily development tasks
- Tracking completion of specific features
- Verifying phase readiness
- Ensuring nothing is forgotten

---

### 3. **IMPROVEMENTS.md** - Current Improvements Summary
**Purpose:** Summary of recent refactoring and improvements  
**Contains:**
- Gameplay improvements (Pacman fix, speed reduction)
- Design patterns applied (6 patterns explained)
- Code organization structure
- Configuration settings
- How to adjust difficulty
- Future enhancement possibilities

**When to Use:**
- Understanding current code architecture
- Learning about design patterns used
- Tuning game difficulty
- Onboarding new team members

---

### 4. **README.md** - Getting Started (To Be Created)
**Purpose:** Installation, setup, and basic usage guide  
**Suggested Contents:**
- Project overview
- System requirements
- Installation instructions
- How to run the game
- Command reference
- Contributing guidelines
- License information

**When to Create:** Phase 1, End of November

---

## 🗂️ Project Structure

```
irancell-anniversary-game/
├── main.py                  # Game entry point and loop
├── config.json              # Configuration settings
├── IMPROVEMENTS.md          # ✅ Current improvements (Game design patterns)
├── ROADMAP.md               # ✅ 11-month development plan
├── CHECKLIST.md             # ✅ Implementation checklist
├── PROJECT_DOCS.md          # ✅ This file
├── README.md                # 📝 To be created
├── CHANGELOG.md             # 📝 To be created
├── LICENSE                  # 📝 To be created
│
├── assets/                  # 📁 To be created (Phase 2)
│   ├── sprites/
│   ├── sounds/
│   ├── music/
│   └── fonts/
│
├── src/                     # 📁 To be created (Phase 1)
│   ├── entities.py          # Game objects
│   ├── levels.py            # Level builder
│   ├── ui.py                # Rendering and UI
│   └── config.py            # Config management
│
├── tests/                   # 📁 To be created (Phase 1)
│   ├── test_player.py
│   ├── test_enemy.py
│   ├── test_levels.py
│   └── test_collision.py
│
└── build/                   # 📁 Build outputs (Phase 4)
    ├── windows/
    ├── linux/
    └── web/
```

---

## 🎯 Quick Start Guide

### For New Team Members:
1. Read **IMPROVEMENTS.md** (understand current state)
2. Read **ROADMAP.md** (understand the vision)
3. Check **CHECKLIST.md** (see current tasks)
4. Run `python main.py` to see the game in action

### For Phase Leaders:
1. Reference **ROADMAP.md** for your phase timeline
2. Check **CHECKLIST.md** for detailed tasks
3. Mark items complete as you progress
4. Report blockers and dependencies

### For Designers/Artists:
1. Phase 2 starts in January 2026
2. See **ROADMAP.md** → Phase 2 for visual requirements
3. Character specs: Irancell Hero + 4 Ghost types
4. See **CHECKLIST.md** for detailed deliverables

### For Audio Team:
1. Phase 2 starts in January 2026
2. Requirement: 8-bit chiptune remix of Irancell jingle
3. ~2 minute loop for background music
4. Tools: FamiTracker or SFXR recommended

---

## 📋 Current Status

| Phase | Timeline | Status | Docs |
|-------|----------|--------|------|
| **Phase 1** | Nov–Dec 2025 | 🟢 In Progress | [ROADMAP.md](ROADMAP.md#🔧-phase-1--foundation-polish) |
| **Phase 2** | Jan–Feb 2026 | 🔵 Planned | [ROADMAP.md](ROADMAP.md#🎨-phase-2--branding--visual-identity) |
| **Phase 3** | Mar–Apr 2026 | ⚪ Planned | [ROADMAP.md](ROADMAP.md#🎮-phase-3--advanced-mechanics) |
| **Phase 4** | May–Jun 2026 | ⚪ Planned | [ROADMAP.md](ROADMAP.md#🌐-phase-4--integration--cross-platform) |
| **Phase 5** | Jul–Aug 2026 | ⚪ Planned | [ROADMAP.md](ROADMAP.md#✨-phase-5--ux-animations--qa) |
| **Phase 6** | Sep–Oct 2026 | ⚪ Planned | [ROADMAP.md](ROADMAP.md#🚀-phase-6--launch-prep--marketing) |

**Overall Progress:** ~15% complete ✅

---

## 🔑 Key Metrics

### Current Build (Alpha Pre-0.3)
- **Gameplay:** ✅ Core mechanics complete
- **Design Patterns:** ✅ 6 patterns implemented
- **Speed:** ✅ Reduced (Player: 20px, Enemy: 15px)
- **Character:** ✅ Fixed (C-shape Pacman)
- **Audio:** ⏳ Pending (Phase 1)
- **Branding:** ⏳ Pending (Phase 2)
- **Multi-platform:** ⏳ Pending (Phase 4)

### Target at Launch (v1.0.0 - Oct 31, 2026)
- **Users:** 5,000+ EUS staff & Self-Care users
- **Platforms:** Web + Desktop + Integrated
- **Languages:** Persian + English
- **Accessibility:** 95%+ of users accommodated
- **Performance:** 60 FPS on 80%+ machines

---

## 🛠️ Development Stack

### Language & Framework
- **Language:** Python 3.7+
- **Game Engine:** Pygame (with design patterns)

### Tools (Planned)
- **Version Control:** Git + GitHub
- **Project Management:** GitHub Projects
- **CI/CD:** GitHub Actions (Phase 4)
- **Code Quality:** Pylint, Black, Type hints
- **Testing:** Pytest

### Build & Deployment (Phase 4)
- **Windows:** PyInstaller
- **Linux:** AppImage
- **Web:** Pygbag or Emscripten
- **Integration:** Rust/Iced compatibility

### Design Tools (Phase 2)
- **Sprites:** Aseprite or GIMP
- **Audio:** FamiTracker or SFXR
- **UI Design:** Figma (optional)

---

## 📞 Communication & Collaboration

### Documents to Share:
- **With Designers:** [ROADMAP.md](ROADMAP.md#🎨-phase-2--branding--visual-identity) Phase 2
- **With Audio Team:** [ROADMAP.md](ROADMAP.md#🎨-phase-2--branding--visual-identity) (Music section)
- **With QA Team:** [CHECKLIST.md](CHECKLIST.md#phase-5-ux-animations--qa-julaug-2026)
- **With Stakeholders:** [ROADMAP.md](ROADMAP.md) (Full overview)
- **With Marketing:** [ROADMAP.md](ROADMAP.md#🚀-phase-6--launch-prep--marketing)

### Key Milestones to Report:
- Alpha 0.3 → December 15, 2025
- Beta 0.5 → February 28, 2026
- Beta 0.8 → April 30, 2026
- RC 1.0 → June 30, 2026
- RC 2.0 → August 31, 2026
- v1.0.0 → October 31, 2026 🎉

---

## 🚀 Next Steps (Immediate - Phase 1)

### This Month (November 2025):
- [ ] Finalize code module structure (entities, levels, ui, config)
- [ ] Implement delta-time movement
- [ ] Begin ghost AI improvements
- [ ] Start sound effect integration
- [ ] Set up CI/CD pipeline (optional)

### By End of Phase 1 (December 15):
- [ ] Alpha 0.3 build ready
- [ ] All code modules completed
- [ ] Sound effects integrated
- [ ] Settings screen functional
- [ ] Ghost AI improved

---

## 📚 Recommended Reading Order

**For Developers:**
1. IMPROVEMENTS.md (understand current code)
2. ROADMAP.md Phase 1 section
3. CHECKLIST.md (your tasks)
4. Code (`main.py`, review design patterns)

**For Project Managers:**
1. ROADMAP.md (entire document)
2. CHECKLIST.md (for tracking)
3. This file (PROJECT_DOCS.md)

**For Team Leads:**
1. ROADMAP.md (your phase)
2. CHECKLIST.md (your deliverables)
3. IMPROVEMENTS.md (technical context)

**For New Team Members:**
1. This file (PROJECT_DOCS.md)
2. IMPROVEMENTS.md (current state)
3. ROADMAP.md (the vision)
4. CHECKLIST.md (current work)

---

## 🎓 Learning Resources

### Design Patterns Used in Code:
- **Singleton:** Centralized game state management
- **Factory:** Object creation abstraction
- **Strategy:** Drawable and Collidable interfaces
- **Builder:** Level construction
- **MVC:** Game controller architecture
- **Enum:** Type-safe direction system

See **IMPROVEMENTS.md** for detailed pattern explanations.

---

## 📝 Version History

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| 0.1 | Oct 2025 | ✅ Complete | Initial prototype |
| 0.2 | Nov 2, 2025 | ✅ Complete | Refactored with design patterns, fixed Pacman, reduced speed |
| 0.3 | Dec 15, 2025 | ⏳ Target | Alpha with sound & settings |
| 0.5 | Feb 28, 2026 | ⏳ Target | Beta with branding |
| 0.8 | Apr 30, 2026 | ⏳ Target | Beta with full mechanics |
| 1.0 | Oct 31, 2026 | 🎯 Target | Official v1.0.0 Release |

---

## ❓ FAQ

**Q: Where do I find the current game code?**  
A: Main game is in `main.py`. It uses design patterns explained in IMPROVEMENTS.md.

**Q: When does my phase start?**  
A: Check ROADMAP.md timeline table at the top for your phase dates.

**Q: How do I report a bug?**  
A: Use GitHub Issues with clear steps to reproduce.

**Q: Can I work on something from another phase?**  
A: Yes! Communicate with the lead first. Check dependencies in CHECKLIST.md.

**Q: What if I finish early?**  
A: Check "Stretch Goals" in ROADMAP.md or help another team member.

**Q: How often should I update the checklist?**  
A: Daily during active development. Mark items complete immediately.

---

## 🎉 Vision

By October 31, 2026, **PAC-IRANCELL** will be a polished, branded, nostalgic mini-game celebrating 20 years of MTN Irancell's connection legacy—available across web, desktop, and integrated into Self-Care, with global leaderboards and accessibility for all users.

---

**Document Version:** 1.0  
**Created:** November 2, 2025  
**Last Updated:** November 2, 2025  
**Maintained By:** Development Team  
**Status:** 🟢 Active Project

---

## 📞 Quick Links

- 🗺️ [ROADMAP.md](ROADMAP.md) - Full 11-month plan
- ✅ [CHECKLIST.md](CHECKLIST.md) - Task checklist
- 🎮 [IMPROVEMENTS.md](IMPROVEMENTS.md) - Current improvements
- 💻 [main.py](main.py) - Game source code
- ⚙️ [config.json](config.json) - Configuration

---

**Ready to build something awesome? Let's go! 🚀**
