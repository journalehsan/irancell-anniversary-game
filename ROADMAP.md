# 🗓️ PAC-IRANCELL 20th Anniversary Roadmap

**Project Duration:** November 2025 – October 2026 (11 months)  
**Goal:** Transform PAC-IRANCELL from a prototype into a professional, branded mini-game integrated into MTN Irancell's Self-Care app and web portal.

---

## 📊 Project Overview

| Phase | Timeline | Status | Focus |
|-------|----------|--------|-------|
| **Phase 1** | Nov–Dec 2025 | 🟢 In Progress | Foundation Polish |
| **Phase 2** | Jan–Feb 2026 | 🔵 Planned | Branding & Visual Identity |
| **Phase 3** | Mar–Apr 2026 | ⚪ Planned | Advanced Mechanics |
| **Phase 4** | May–Jun 2026 | ⚪ Planned | Integration & Cross-Platform |
| **Phase 5** | Jul–Aug 2026 | ⚪ Planned | UX, Animations & QA |
| **Phase 6** | Sep–Oct 2026 | ⚪ Planned | Launch Prep & Marketing |

---

## 🔧 Phase 1 — Foundation Polish
### **Timeline:** November – December 2025
### **Goal:** Refactor and stabilize the core gameplay

### Milestones:

- [x] **Core maze + collision logic** ✅
  - Status: Completed with refactored design patterns
  - Details: Wall collision, coin collection, power pellets working
  
- [x] **Design patterns implemented** ✅
  - Status: Singleton, Factory, Strategy, Builder, MVC patterns integrated
  - Details: Clean architecture for future expansion

- [ ] **Code structure split into modules**
  - `main.py` → Game entry point and loop
  - `entities.py` → Player, Enemy, Coin, PowerPellet, Wall classes
  - `levels.py` → Level builder and maze generation
  - `ui.py` → Rendering, HUD, screens
  - `config.py` → Configuration management
  - **Target:** End of November

- [ ] **Consistent FPS & delta-time movement**
  - Implement frame-independent movement (currently frame-dependent)
  - Smooth animations across different FPS settings
  - **Target:** Early December

- [ ] **Improve ghost AI**
  - Implement chase mode (follow player)
  - Implement scatter mode (return to corners)
  - Mode switching every 7 seconds
  - Better pathfinding algorithms
  - **Target:** Mid-December

- [ ] **Sound effects**
  - Coin collection sound
  - Power-up activation sound
  - Enemy eaten sound
  - Game over sound
  - Background music loop
  - **Tools:** Pygame mixer or python-pydub
  - **Target:** Late December

- [ ] **Settings screen**
  - Sound on/off toggle
  - Difficulty selector (Easy, Normal, Hard)
  - Visual theme selector
  - Persist settings to JSON
  - **Target:** Late December

### 🎯 Deliverable:
**Alpha 0.3** - Stable, polished gameplay  
✓ Smooth FPS  
✓ Improved AI  
✓ Sound integrated  
✓ Settings functional

---

## 🎨 Phase 2 — Branding & Visual Identity
### **Timeline:** January – February 2026
### **Goal:** Make it feel Irancell-official

### Milestones:

- [ ] **Irancell-themed visuals**
  - Replace walls with **yellow (#FFCC00) outlines** and glowing dots
  - Add Irancell branding colors (Yellow & Blue) throughout
  - Animated glowing corners and edges
  - **Target:** Early January

- [ ] **Splash screen with 20th anniversary messaging**
  - Large text: "🎉 20 Years of Connection — MTN Irancell"
  - Animated star particles and network nodes
  - Countdown timer (if running pre-launch)
  - Skip button for testing
  - **Target:** Mid-January

- [ ] **Irancell-themed character pack**
  - **PAC-Man → "Irancell Hero"**
    - Smiling yellow Irancell logo face instead of generic Pacman
    - Wears tiny headset (EUS staff identity)
  
  - **Ghosts → Network Threats**
    - Red Ghost: "Signal Loss" 📡
    - Pink Ghost: "Data Lag" 🌐
    - Cyan Ghost: "Spam Bot" 🤖
    - Orange Ghost: "Time Drift" ⏰
  
  - Custom sprites and animations for each character
  - **Target:** Late January

- [ ] **Irancell jingle remix (8-bit chiptune)**
  - Compose or commission 8-bit version of MTN Irancell jingle
  - ~2 minute loop for background music
  - Optional: Staff musician collaboration for authenticity
  - **Tools:** FamiTracker or SFXR for chiptune generation
  - **Target:** Early February

- [ ] **Animated intro and game-over screens**
  - Level intro: "Level X - Connection Secured ✓"
  - Animated transitions with Irancell branding
  - Game Over screen with score + "Try Again" animation
  - Victory screen with celebration effects
  - **Target:** Mid-February

### 🎯 Deliverable:
**Beta 0.5** - Branded, engaging experience  
✓ Irancell visual identity  
✓ Themed characters  
✓ Branded music  
✓ Professional UI/UX

---

## 🎮 Phase 3 — Advanced Mechanics
### **Timeline:** March – April 2026
### **Goal:** Add depth and engagement

### Milestones:

- [ ] **Multi-level progression**
  - 5-10 different maze layouts
  - Progressive difficulty scaling
  - Unlock new levels on completion
  - **Difficulty increase per level:**
    - More enemies
    - Faster enemy speed
    - Fewer coins
    - Tighter timing
  - **Target:** Early March

- [ ] **Power-up system**
  - **"5G Turbo"** → Increase player speed by 50% for 5 seconds
  - **"Data Booster"** → Double score for 10 seconds
  - **"Firewall Shield"** → Temporary invulnerability (2 ghosts)
  - **"Network Cache"** → Slow down all enemies
  - Visual indicators showing active power-ups
  - **Target:** Mid-March

- [ ] **Themed collectibles (replace fruit)**
  - **Irancell SIM Card** (500 pts)
  - **WiFi Router** (750 pts)
  - **Fiber Box** (1000 pts)
  - **Data Plan** (250 pts - quick collect)
  - Custom sprites for each item
  - **Target:** Mid-March

- [ ] **Score multipliers & combo system**
  - Collect N coins rapidly → 1.5x multiplier
  - Eat enemies in sequence → increasing score
  - Combo counter display on HUD
  - **Target:** Late March

- [ ] **Local leaderboard system**
  - Store top 10 scores locally
  - Player name entry screen
  - Persistent storage in JSON
  - Display on victory screen
  - **Optional:** Backend sync to Laravel API
  - **Target:** Early April

### 🎯 Deliverable:
**Beta 0.8** - Feature-complete gameplay  
✓ Multiple levels  
✓ Power-up diversity  
✓ Scoring depth  
✓ Replayability  
✓ Leaderboard

---

## 🌐 Phase 4 — Integration & Cross-Platform
### **Timeline:** May – June 2026
### **Goal:** Make it run everywhere

### Milestones:

- [ ] **EUS Self-Care desktop integration**
  - Embed PAC-IRANCELL as a menu option in Self-Care (Rust/Iced)
  - Seamless launch from app
  - Share score back to main app
  - Return to app on exit
  - **Requirement:** Compatibility with EUS architecture
  - **Target:** Early May

- [ ] **Windows EXE standalone build**
  - Use PyInstaller to bundle game
  - Include all assets (sprites, sounds, config)
  - Create installer with shortcuts
  - **Target:** Early May

- [ ] **Linux AppImage build**
  - AppImage package for compatibility
  - Test on Ubuntu 20.04, 22.04
  - Create desktop launcher
  - **Target:** Mid-May

- [ ] **Web playable version**
  - Port to **Pygbag** (Pygame for web)
  - Or compile to **WebAssembly** using Emscripten
  - Host on irancell.ir/pac-irancell
  - Works in Chrome, Firefox, Safari
  - **Target:** Late May

- [ ] **Offline-first architecture**
  - All game logic works without internet
  - Optional: Score sync when connection available
  - Graceful fallback if sync fails
  - **Target:** Early June

- [ ] **Backend score submission (optional)**
  - POST endpoint to Laravel API
  - Store scores with user ID from Self-Care
  - Global leaderboard fetching
  - **Target:** Late June

### 🎯 Deliverable:
**RC 1.0** - Cross-platform ready  
✓ Desktop integration  
✓ Multiple platform packages  
✓ Web version accessible  
✓ Offline-ready

---

## ✨ Phase 5 — UX, Animations & QA
### **Timeline:** July – August 2026
### **Goal:** Polish and refine user experience

### Milestones:

- [ ] **Smooth animations & transitions**
  - Sprite sheet animations for ghosts
  - Pacman mouth animation refinement
  - Level transition effects
  - Score popup animations
  - **Target:** Early July

- [ ] **Avatar integration**
  - Pull user profile from Self-Care
  - Display player name on HUD
  - Show avatar in leaderboard
  - **Target:** Mid-July

- [ ] **Accessibility features**
  - **Colorblind mode** (high contrast palette)
  - **Sound mode** (visual beep indicators instead of audio)
  - **Large font option** for elderly users
  - Keyboard only controls (no mouse needed)
  - **Target:** Mid-July

- [ ] **Localization (i18n)**
  - **Persian (Farsi)** - primary language
  - **English** - secondary
  - Translate all UI text, menus, messages
  - RTL support for Persian text
  - Use i18n library (babel or similar)
  - **Target:** Late July

- [ ] **Internal QA testing**
  - QA round with IT department
  - EUS team testing on real Self-Care builds
  - Bug reports & fixes
  - Performance optimization
  - **Target:** Late July

- [ ] **Performance optimization**
  - Reduce lag on older machines
  - Optimize sprite rendering
  - Profile memory usage
  - Target: 60 FPS on mid-range laptops
  - **Target:** Early August

### 🎯 Deliverable:
**RC 2.0** - Polished experience ready for launch  
✓ Smooth animations  
✓ Accessible to all users  
✓ Multilingual support  
✓ QA tested

---

## 🚀 Phase 6 — Launch Prep & Marketing
### **Timeline:** September – October 2026
### **Goal:** Finalize build and campaign

### Milestones:

- [ ] **Promotional video**
  - 30-second teaser: "20 Years of PAC-IRANCELL Adventure"
  - Show gameplay, characters, and 20th anniversary branding
  - Upload to YouTube, social media
  - **Target:** Early September

- [ ] **Self-Care 20.0 bundling**
  - Package PAC-IRANCELL as Easter egg in app
  - Hidden menu option or unlock achievement
  - Secret button combo to launch
  - **Target:** Mid-September

- [ ] **Web promo landing page**
  - irancell.ir/pac-irancell
  - "Play PAC-IRANCELL — 20 Years of Connection"
  - Game embed or download links
  - High scores leaderboard
  - Social sharing buttons
  - **Target:** Mid-September

- [ ] **Internal staff leaderboard event**
  - Time-limited competition (1 week)
  - Top 3 prizes for EUS and sales teams
  - Live leaderboard display in offices
  - Social sharing within company
  - **Target:** Late September

- [ ] **Press kit & final assets**
  - Logo, screenshots, promo images
  - Game trailer (HD version)
  - Press release
  - Developer notes
  - **Target:** Late September

- [ ] **Version 1.0.0 release**
  - Golden Master build
  - Release notes finalized
  - All platforms ready (Web, Desktop, Integration)
  - **Target:** October 31, 2026 (20th Anniversary Launch!)

### 🎯 Deliverable:
**Version 1.0.0 - Official Launch** 🎉  
✓ Public release  
✓ Marketing campaign complete  
✓ Integrated into Self-Care  
✓ Global leaderboard live

---

## 🎯 Extra Ideas (Stretch Goals)

If time permits or additional resources available:

### 🧠 AI-Generated Level Generation
- Use procedural generation or ML model for infinite levels
- Ensure playability (not too hard, not too easy)
- Difficulty scaling based on player skill

### 🌍 Multiplayer Mode
- "Team Irancell vs Ghost Network" event
- Cooperative gameplay
- Network synchronization (Firebase or custom backend)

### 📱 Android Mobile Port
- Port to Android using Kivy framework
- Touch controls optimized
- Internal showcase on tablets

### 🏆 Engineer Mode
- Hidden debug mode for EUS staff
- Extra lives, speed controls, level skip
- Developer credits screen
- Access code or easter egg unlock

### 🎨 Customization System
- Player skins (different Irancell characters)
- Maze themes (office, network, data center)
- Ghost themes
- Soundtrack selector

### 📊 Advanced Analytics
- Track gameplay patterns
- Most popular levels
- Player skill distribution
- Design insights for future versions

---

## 📋 Success Metrics

At launch (October 2026), success will be measured by:

| Metric | Target |
|--------|--------|
| **Users Playing** | 5,000+ EUS staff & Self-Care users |
| **Avg. Session Length** | 5-10 minutes |
| **Return Players** | 40%+ within 1 week |
| **Leaderboard Engagement** | 500+ scores submitted |
| **Platform Availability** | Web + Desktop + Integrated |
| **Performance** | 60 FPS on 80%+ machines |
| **Accessibility** | 95%+ of users accommodated |

---

## 🔄 Development Workflow

### Recommended Tools & Stack:
- **Version Control:** Git + GitHub (already set up)
- **Project Management:** GitHub Projects or Jira
- **Branching:** `main`, `develop`, `feature/*`, `release/*`
- **CI/CD:** GitHub Actions for builds
- **Code Quality:** Pylint, Black formatter, Type hints
- **Testing:** Pytest for unit tests

### Release Schedule:
- **Alpha (0.3):** December 15, 2025
- **Beta (0.5):** February 28, 2026
- **Beta (0.8):** April 30, 2026
- **RC 1.0:** June 30, 2026
- **RC 2.0:** August 31, 2026
- **Golden Master:** October 15, 2026
- **v1.0.0 Release:** October 31, 2026

---

## 👥 Team Requirements

### Suggested Roles:
1. **Lead Developer** - Architecture, core mechanics
2. **Graphics Designer** - Sprites, UI, animations
3. **Audio Designer** - Sound effects, music
4. **QA Tester** - Testing across platforms
5. **DevOps Engineer** - Builds, deployment, CI/CD
6. **Product Manager** - Timeline, requirements, launch

---

## 📝 Notes & Considerations

- **Backwards Compatibility:** Ensure game runs on Python 3.7+ for older systems
- **Accessibility First:** Colorblind mode and sound-off should not compromise gameplay
- **Performance:** Test on Intel i5 / Ryzen 5 laptops to ensure 60 FPS
- **Network:** Leaderboard sync should handle offline scenarios gracefully
- **Localization:** RTL support for Persian is critical
- **Security:** Sanitize all user input (names, scores) before storing in backend

---

## 🎉 Vision

By October 2026, **PAC-IRANCELL** will be:

> *A polished, branded, nostalgic mini-game celebrating 20 years of MTN Irancell's connection legacy. Available across web, desktop, and integrated into the Self-Care platform, with global leaderboards, accessibility for all users, and memories for generations of Irancell staff and customers.*

---

**Created:** November 2, 2025  
**Last Updated:** November 2, 2025  
**Status:** 🟢 Active Development  
**Version:** 1.0 (Roadmap)
