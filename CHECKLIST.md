# ✅ PAC-IRANCELL Development Checklist

## Phase 1: Foundation Polish (Nov–Dec 2025)

### Code Architecture
- [x] Core gameplay mechanics completed
- [x] Design patterns implemented (Singleton, Factory, Strategy, Builder, MVC)
- [ ] Split code into modules:
  - [ ] `entities.py` - Player, Enemy, Coin, PowerPellet, Wall
  - [ ] `levels.py` - Level builder and maze generation
  - [ ] `ui.py` - Rendering, HUD, screens
  - [ ] `config.py` - Configuration management
  - [ ] Keep `main.py` as entry point and game loop

### Gameplay Improvements
- [x] Fixed Pacman character (C-shape, directional mouth)
- [x] Reduced game speed (Player: 40→20, Enemy: 40→15)
- [x] Movement update rate implemented
- [ ] Improve ghost AI:
  - [ ] Chase mode (8 seconds)
  - [ ] Scatter mode (8 seconds)
  - [ ] Intelligent pathfinding
- [ ] Delta-time movement (frame-independent)

### Audio & UX
- [ ] Sound effects:
  - [ ] Coin collection sound
  - [ ] Power-up sound
  - [ ] Enemy eaten sound
  - [ ] Game over sound
- [ ] Background music loop (2 minutes)
- [ ] Settings screen:
  - [ ] Sound toggle
  - [ ] Difficulty selector (Easy/Normal/Hard)
  - [ ] Theme selector
  - [ ] Save to config.json

### Testing
- [ ] Gameplay testing on multiple machines
- [ ] FPS consistency check
- [ ] Memory usage profiling
- [ ] Edge case testing (collisions, boundaries)

**Deliverable:** Alpha 0.3 (Dec 15, 2025)

---

## Phase 2: Branding & Visual Identity (Jan–Feb 2026)

### Visual Design
- [ ] Irancell-themed visuals:
  - [ ] Yellow (#FFCC00) wall outlines
  - [ ] Glowing dots and edges
  - [ ] Yellow & Blue branding colors
- [ ] Splash screen:
  - [ ] "20 Years of Connection" messaging
  - [ ] Animated particles
  - [ ] Network node effects
  - [ ] Countdown timer (optional)
- [ ] Custom character pack:
  - [ ] **Player:** "Irancell Hero" with headset
  - [ ] **Red Ghost:** "Signal Loss" 📡
  - [ ] **Pink Ghost:** "Data Lag" 🌐
  - [ ] **Cyan Ghost:** "Spam Bot" 🤖
  - [ ] **Orange Ghost:** "Time Drift" ⏰

### Audio & Music
- [ ] 8-bit chiptune remix of Irancell jingle
- [ ] ~2 minute loop for background music
- [ ] Audio quality check

### Screens & Animations
- [ ] Level intro screen: "Level X - Connection Secured ✓"
- [ ] Game over animation
- [ ] Victory celebration animation
- [ ] Smooth screen transitions
- [ ] Score popup animations

### Quality Assurance
- [ ] Visual consistency review
- [ ] Brand guideline compliance check
- [ ] Animation smoothness verification

**Deliverable:** Beta 0.5 (Feb 28, 2026)

---

## Phase 3: Advanced Mechanics (Mar–Apr 2026)

### Level Progression
- [ ] Create 5-10 maze layouts
- [ ] Progressive difficulty:
  - [ ] More enemies per level
  - [ ] Faster enemy speed scaling
  - [ ] Fewer coins to collect
  - [ ] Tighter timing requirements
- [ ] Level unlock system

### Power-ups
- [ ] **5G Turbo:** Speed +50% for 5 sec
- [ ] **Data Booster:** 2x score for 10 sec
- [ ] **Firewall Shield:** Invulnerability (2 ghosts)
- [ ] **Network Cache:** Slow all enemies
- [ ] Visual indicators for active power-ups
- [ ] Sound effects for power-up activation

### Collectibles
- [ ] Replace generic fruit with:
  - [ ] Irancell SIM Card (500 pts)
  - [ ] WiFi Router (750 pts)
  - [ ] Fiber Box (1000 pts)
  - [ ] Data Plan (250 pts)
- [ ] Custom sprites for each item

### Scoring System
- [ ] Score multiplier on rapid collection
- [ ] Combo counter (eating enemies in sequence)
- [ ] Display multiplier on HUD
- [ ] Sound effect for combo achievement

### Leaderboard
- [ ] Local leaderboard (top 10)
- [ ] Player name entry screen
- [ ] Persistent JSON storage
- [ ] Display on victory screen
- [ ] (Optional) Backend sync capability

**Deliverable:** Beta 0.8 (Apr 30, 2026)

---

## Phase 4: Integration & Cross-Platform (May–Jun 2026)

### Self-Care Integration
- [ ] Embed in Rust/Iced Self-Care app
- [ ] Menu option to launch game
- [ ] Score sharing back to app
- [ ] Return to app on exit
- [ ] Architecture compatibility review

### Desktop Builds
- [ ] Windows EXE (PyInstaller):
  - [ ] Bundle all assets
  - [ ] Create installer
  - [ ] Desktop shortcuts
- [ ] Linux AppImage:
  - [ ] Compatibility test (Ubuntu 20.04, 22.04)
  - [ ] Desktop launcher
  - [ ] Permissions handling

### Web Version
- [ ] Choose tech (Pygbag or Emscripten)
- [ ] Port game to web
- [ ] Test on Chrome, Firefox, Safari
- [ ] Responsive design for different screen sizes
- [ ] Deploy to irancell.ir/pac-irancell

### Offline Architecture
- [ ] All game logic works without internet
- [ ] Score sync when connection available
- [ ] Graceful degradation if sync fails

### Backend (Optional)
- [ ] Laravel API endpoint for score submission
- [ ] User ID association from Self-Care
- [ ] Global leaderboard fetching

**Deliverable:** RC 1.0 (Jun 30, 2026)

---

## Phase 5: UX, Animations & QA (Jul–Aug 2026)

### Animations & Polish
- [ ] Sprite sheet animations for ghosts
- [ ] Pacman mouth animation refinement
- [ ] Level transition effects
- [ ] Score popup animations
- [ ] Enemy death animation
- [ ] Smooth collapsing/fading effects

### User Integration
- [ ] Pull user profile from Self-Care
- [ ] Display player name on HUD
- [ ] Show avatar in leaderboard
- [ ] User authentication (if needed)

### Accessibility
- [ ] **Colorblind mode:**
  - [ ] High contrast palette
  - [ ] Pattern-based distinctions
- [ ] **Sound-off mode:**
  - [ ] Visual beep indicators
  - [ ] Visual power-up effects
- [ ] **Large font option:**
  - [ ] For elderly users
  - [ ] Scalable UI elements
- [ ] **Keyboard-only controls:**
  - [ ] No mouse dependency
  - [ ] All actions mappable

### Localization
- [ ] Persian (Farsi) translation:
  - [ ] UI text
  - [ ] Menu labels
  - [ ] In-game messages
- [ ] English translation:
  - [ ] Complete coverage
  - [ ] Consistency check
- [ ] RTL support for Persian:
  - [ ] Text alignment
  - [ ] Menu layout
  - [ ] HUD positioning

### Testing & Optimization
- [ ] QA testing with IT department
- [ ] EUS team internal testing
- [ ] Performance profiling:
  - [ ] Reduce lag on older machines
  - [ ] Optimize sprite rendering
  - [ ] Memory usage optimization
  - [ ] Target: 60 FPS on mid-range systems
- [ ] Bug fixes and regression testing

**Deliverable:** RC 2.0 (Aug 31, 2026)

---

## Phase 6: Launch Prep & Marketing (Sep–Oct 2026)

### Marketing Assets
- [ ] 30-second promotional video
- [ ] Teaser content
- [ ] Social media graphics
- [ ] Screenshots and artwork
- [ ] Press kit with:
  - [ ] Logo and assets
  - [ ] Game trailer (HD)
  - [ ] Press release
  - [ ] Developer notes

### Public Release
- [ ] Web landing page:
  - [ ] irancell.ir/pac-irancell
  - [ ] Game embed or download links
  - [ ] Leaderboard display
  - [ ] Social sharing buttons
- [ ] App Store submissions (if applicable)
- [ ] Distribution on major platforms

### Self-Care Integration
- [ ] Package as Easter egg in Self-Care 20.0
- [ ] Hidden menu option or achievement unlock
- [ ] Secret button combo to launch

### Launch Event
- [ ] Internal staff leaderboard competition (1 week)
- [ ] Prizes for top 3 EUS/Sales staff
- [ ] Live leaderboard display in offices
- [ ] Social sharing campaign
- [ ] Celebrate 20th anniversary milestone

### Final Build
- [ ] Version 1.0.0 release
- [ ] Golden Master build finalization
- [ ] Release notes completion
- [ ] All platforms verified and tested
- [ ] October 31, 2026 launch date 🎉

**Deliverable:** v1.0.0 Official Release (Oct 31, 2026)

---

## 🎯 Stretch Goals (Time Permitting)

- [ ] AI-generated level generation
- [ ] Multiplayer mode ("Team Irancell vs Ghost Network")
- [ ] Android port (Kivy framework)
- [ ] Engineer mode (debug features for staff)
- [ ] Customization system (skins, themes)
- [ ] Advanced analytics dashboard

---

## 📋 Pre-Launch Checklist (Final Week)

- [ ] All code reviewed and tested
- [ ] Documentation complete
- [ ] README.md updated
- [ ] Installation instructions verified
- [ ] System requirements documented
- [ ] Known issues documented
- [ ] Credits and attributions complete
- [ ] License file included
- [ ] All assets properly attributed
- [ ] Security audit passed
- [ ] Performance testing complete (60 FPS verified)
- [ ] Accessibility audit completed
- [ ] Cross-platform testing done
- [ ] User testing feedback incorporated
- [ ] Press kit finalized

---

## Notes

- **Keep this file updated** as you progress through each phase
- **Mark completed items** with `[x]`
- **Update timestamps** when milestones are achieved
- **Link to GitHub issues** where applicable
- **Reference ROADMAP.md** for detailed phase descriptions

**Last Updated:** November 2, 2025  
**Current Phase:** Phase 1 (Foundation Polish)  
**Overall Progress:** ~15% complete
