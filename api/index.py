"""Quest Engine Roadmap — deployed as a Vercel serverless function."""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quest Engine — Roadmap</title>
<meta name="description" content="The gold standard educational game engine. 6 games, 178 chapters, 7,800+ challenges.">
<meta property="og:title" content="Quest Engine Roadmap">
<meta property="og:description" content="6 games, 178 chapters, 7,800+ challenges across education, DevOps, AI, and 3 languages.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root { --bg: #0a1628; --s: #0f1e35; --r: #152540; --b: #1e3a5f; --bb: #2a5080;
    --p: #00e5a0; --sec: #00b4d8; --acc: #ff3c78; --w: #ffa500;
    --t: #c8d8e8; --tb: #e8f4ff; --td: rgba(200,216,232,0.4); }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); color: var(--t); font-family: 'Nunito', system-ui, sans-serif; min-height: 100vh; }
  a { color: var(--p); text-decoration: none; } a:hover { text-decoration: underline; }
  .app { max-width: 960px; margin: 0 auto; padding: 2.5rem 1.5rem; }

  .hero { text-align: center; margin-bottom: 3rem; }
  .hero h1 { font-size: 2.2rem; font-weight: 800; color: var(--tb); margin-bottom: 0.3rem; }
  .hero h1 span { color: var(--p); }
  .hero p { color: var(--td); font-size: 0.95rem; max-width: 600px; margin: 0 auto; }

  .stats { display: flex; justify-content: center; gap: 2.5rem; margin: 2rem 0 3rem; flex-wrap: wrap; }
  .stat { text-align: center; }
  .sv { font-size: 2.4rem; font-weight: 800; line-height: 1.1; }
  .sl { font-size: 0.7rem; color: var(--td); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.2rem; }

  .sec { margin-bottom: 3rem; }
  .sec-title {
    font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em;
    color: var(--td); margin-bottom: 1.25rem; display: flex; align-items: center; gap: 0.6rem;
  }
  .badge { font-size: 0.65rem; padding: 0.2rem 0.6rem; border-radius: 100px; font-weight: 800; }
  .b-ship { background: rgba(0,229,160,0.15); color: var(--p); }
  .b-prog { background: rgba(255,165,0,0.15); color: var(--w); }
  .b-plan { background: rgba(0,180,216,0.15); color: var(--sec); }

  .games { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 0.85rem; }
  .gc {
    padding: 1.1rem; background: var(--s); border: 1px solid var(--b); border-radius: 12px;
    transition: border-color 0.15s, transform 0.1s;
  }
  .gc:hover { border-color: var(--p); transform: translateY(-2px); }
  .gc-name { font-weight: 700; color: var(--tb); font-size: 0.95rem; }
  .gc-stats { font-size: 0.78rem; color: var(--td); margin-top: 0.3rem; }
  .gc-url { font-size: 0.7rem; color: var(--sec); margin-top: 0.3rem; font-family: 'JetBrains Mono', monospace; }
  .gc-bar { height: 4px; background: var(--b); border-radius: 2px; margin-top: 0.5rem; overflow: hidden; }
  .gc-fill { height: 100%; border-radius: 2px; background: linear-gradient(90deg, var(--p), var(--sec)); }

  .items { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 0.85rem; }
  .item {
    padding: 1.1rem; background: var(--s); border: 1px solid var(--b); border-radius: 12px;
    border-top: 3px solid var(--p); transition: transform 0.1s;
  }
  .item:hover { transform: translateY(-2px); }
  .item-b { border-top-color: var(--w); }
  .item-p { border-top-color: var(--sec); opacity: 0.7; }
  .item-icon { font-size: 1.5rem; margin-bottom: 0.4rem; }
  .item-title { font-weight: 700; color: var(--tb); font-size: 0.95rem; margin-bottom: 0.2rem; }
  .item-desc { font-size: 0.8rem; color: var(--td); line-height: 1.5; }

  .tl { position: relative; padding-left: 2.5rem; margin-top: 1rem; }
  .tl::before { content: ""; position: absolute; left: 10px; top: 0; bottom: 0; width: 2px; background: var(--b); }
  .tl-item { position: relative; margin-bottom: 1.75rem; }
  .tl-dot { position: absolute; left: -2.5rem; top: 3px; width: 14px; height: 14px; border-radius: 50%; border: 2px solid var(--p); background: var(--bg); }
  .tl-done { background: var(--p); }
  .tl-active { background: var(--w); border-color: var(--w); }
  .tl-title { font-weight: 700; color: var(--tb); font-size: 0.95rem; }
  .tl-desc { font-size: 0.82rem; color: var(--td); margin-top: 0.15rem; line-height: 1.5; }
  .tl-date { font-size: 0.7rem; color: var(--td); margin-top: 0.2rem; font-family: 'JetBrains Mono', monospace; }

  .footer { text-align: center; padding: 2rem 0; color: var(--td); font-size: 0.75rem; border-top: 1px solid var(--b); margin-top: 2rem; }
</style>
</head>
<body>
<div class="app">

  <div class="hero">
    <h1>🗺️ <span>Quest Engine</span> Roadmap</h1>
    <p>The gold standard educational game engine — 6 games teaching kids, developers, AI practitioners, and language learners across 178 chapters.</p>
  </div>

  <div class="stats">
    <div class="stat"><div class="sv" style="color:var(--p)">16</div><div class="sl">Games</div></div>
    <div class="stat"><div class="sv" style="color:var(--sec)">178</div><div class="sl">Chapters</div></div>
    <div class="stat"><div class="sv" style="color:var(--w)">7,800</div><div class="sl">Challenges</div></div>
    <div class="stat"><div class="sv" style="color:var(--acc)">82</div><div class="sl">Tests</div></div>
    <div class="stat"><div class="sv" style="color:var(--tb)">8</div><div class="sl">Themes</div></div>
  </div>

  <div class="sec">
    <div class="sec-title">Live Games <span class="badge b-ship">Deployed</span></div>
    <div class="games">
      <div class="gc"><div class="gc-name">🌸 The Primer</div><div class="gc-stats">45 chapters · 2,064 challenges · Ages 5-12</div><div class="gc-url">primer-ecru.vercel.app</div><div class="gc-bar"><div class="gc-fill" style="width:100%"></div></div></div>
      <div class="gc"><div class="gc-name">⚡ NEXUS Quest</div><div class="gc-stats">42 chapters · 2,162 challenges · For developers</div><div class="gc-url">nexus-quest-eta.vercel.app</div><div class="gc-bar"><div class="gc-fill" style="width:100%"></div></div></div>
      <div class="gc"><div class="gc-name">🧠 AI Academy</div><div class="gc-stats">12 chapters · 488 challenges · AI literacy for everyone</div><div class="gc-url">ai-academy-iota-eight.vercel.app</div><div class="gc-bar"><div class="gc-fill" style="width:100%"></div></div></div>
      <div class="gc"><div class="gc-name">🐉 Learn Chinese</div><div class="gc-stats">11 chapters · 460 challenges · Mandarin from English</div><div class="gc-url">learn-chinese-pearl.vercel.app</div><div class="gc-bar"><div class="gc-fill" style="width:100%"></div></div></div>
      <div class="gc"><div class="gc-name">🌅 Learn Spanish</div><div class="gc-stats">11 chapters · 413 challenges · Spanish from English</div><div class="gc-url">learn-spanish-silk.vercel.app</div><div class="gc-bar"><div class="gc-fill" style="width:100%"></div></div></div>
      <div class="gc"><div class="gc-name">🌊 Learn Japanese</div><div class="gc-stats">11 chapters · 424 challenges · Japanese from English</div><div class="gc-url">learn-japanese-rose-two.vercel.app</div><div class="gc-bar"><div class="gc-fill" style="width:100%"></div></div></div>
    </div>
  </div>

  <div class="sec">
    <div class="sec-title">Shipped Features <span class="badge b-ship">✅ Done</span></div>
    <div class="items">
      <div class="item"><div class="item-icon">🛡️</div><div class="item-title">Anti-Cheat System</div><div class="item-desc">Option shuffling per user/challenge/day, streak freeze (50 XP), lesson-first zones, hint XP cost, challenge ID validation.</div></div>
      <div class="item"><div class="item-icon">🤖</div><div class="item-title">AI Tutor</div><div class="item-desc">Claude Haiku explains wrong answers in real-time via "Explain why" button. Shows correct answer with explanation.</div></div>
      <div class="item"><div class="item-icon">🔊</div><div class="item-title">TTS Voices</div><div class="item-desc">Google Cloud Studio voices + ElevenLabs. Character-specific: Puck, CIPHER, ARIA, 龙龙, Sofia, Sensei.</div></div>
      <div class="item"><div class="item-icon">🗄️</div><div class="item-title">Postgres + Auth</div><div class="item-desc">Neon database, bcrypt auth, session cookies, per-user progress. Admin analytics dashboard.</div></div>
      <div class="item"><div class="item-icon">⚡</div><div class="item-title">Speed Bonus XP</div><div class="item-desc">+25% XP for answers under 5s, +10% under 10s. Timer tracks elapsed time with color coding.</div></div>
      <div class="item"><div class="item-icon">🌟</div><div class="item-title">Daily Login Bonus</div><div class="item-desc">10 + (streak_days × 5) XP daily. Streak scaling up to 60 XP at 10-day streak.</div></div>
      <div class="item"><div class="item-icon">🔄</div><div class="item-title">Spaced Repetition</div><div class="item-desc">SM-2 inspired Smart Review with Again/Hard/Good/Easy ratings. Spaced review page per pack.</div></div>
      <div class="item"><div class="item-icon">🎨</div><div class="item-title">8 Visual Themes</div><div class="item-desc">Cyberpunk, Playful, Neural, Medieval, Unicorn, Alien, Ocean, Sunset — switchable in settings.</div></div>
      <div class="item"><div class="item-icon">📱</div><div class="item-title">PWA + Sounds</div><div class="item-desc">Installable on mobile, offline caching, synthesized audio feedback for all game events.</div></div>
      <div class="item"><div class="item-icon">🏆</div><div class="item-title">Engagement</div><div class="item-desc">Daily challenges (2x XP), streaks + combos, leaderboards, achievements, adaptive difficulty, share button.</div></div>
      <div class="item"><div class="item-icon">📊</div><div class="item-title">Analytics</div><div class="item-desc">Admin dashboard, signup notifications, per-challenge pass rates, progress rings, streak calendar.</div></div>
      <div class="item"><div class="item-icon">⚔️</div><div class="item-title">RPG Character System</div><div class="item-desc">4 classes, 3 alignments, 4 narrative tones, 19 gear items, stat system. Full character creation flow.</div></div>
      <div class="item"><div class="item-icon">🔐</div><div class="item-title">Google OAuth</div><div class="item-desc">One-click Google sign-in. Auto account creation. Profile picture sync.</div></div>
      <div class="item"><div class="item-icon">🧪</div><div class="item-title">82 Tests + CI</div><div class="item-desc">Automated tests on Python 3.10/3.11/3.12 via GitHub Actions. Option shuffle, streak freeze, speed bonus all tested.</div></div>
    </div>
  </div>

  <div class="sec">
    <div class="sec-title">In Progress <span class="badge b-prog">🔨 Building</span></div>
    <div class="items">
      <div class="item item-b"><div class="item-icon">🌐</div><div class="item-title">Unified Platform</div><div class="item-desc">One deployment serving all 6 games as courses. Single sign-on, shared progress, admin course controls.</div></div>
      <div class="item item-b"><div class="item-icon">📚</div><div class="item-title">More Content</div><div class="item-desc">Always expanding — crossed 100 chapters, heading to 150+. New subjects every session.</div></div>
      <div class="item item-b"><div class="item-icon">🎙️</div><div class="item-title">Voice Quality</div><div class="item-desc">ElevenLabs premium voices with character differentiation. Needs plan upgrade for credits.</div></div>
      <div class="item item-b"><div class="item-icon">📣</div><div class="item-title">Social Automation</div><div class="item-desc">Automated posting to Twitter/X and YouTube (needs API keys).</div></div>
    </div>
  </div>

  <div class="sec">
    <div class="sec-title">Planned <span class="badge b-plan">📋 Next</span></div>
    <div class="items">
      <div class="item item-p"><div class="item-icon">✏️</div><div class="item-title">Course Creator</div><div class="item-desc">Web UI for users to build their own courses and challenge packs without writing code.</div></div>
      <div class="item item-p"><div class="item-icon">⚔️</div><div class="item-title">Multiplayer</div><div class="item-desc">PvP quiz battles, cooperative learning, real-time rooms.</div></div>
      <div class="item item-p"><div class="item-icon">📱</div><div class="item-title">Mobile App</div><div class="item-desc">React Native for iOS/Android with push notifications and native feel.</div></div>
      <div class="item item-p"><div class="item-icon">📧</div><div class="item-title">Email Reports</div><div class="item-desc">Weekly progress reports and welcome emails via Resend API.</div></div>
      <div class="item item-p"><div class="item-icon">🎬</div><div class="item-title">Video Lessons</div><div class="item-desc">Short video explanations before each zone, integrated with challenge flow.</div></div>
      <div class="item item-p"><div class="item-icon">🏫</div><div class="item-title">Classroom Mode</div><div class="item-desc">Teacher dashboard, class tracking, assignments, LTI integration for LMS.</div></div>
      <div class="item item-p"><div class="item-icon">📜</div><div class="item-title">Certificates</div><div class="item-desc">PDF completion certificates with QR verification and shareable badges.</div></div>
      <div class="item item-p"><div class="item-icon">🔌</div><div class="item-title">Plugin Marketplace</div><div class="item-desc">Community-built themes, challenge types, narrators, and content packs.</div></div>
    </div>
  </div>

  <div class="sec">
    <div class="sec-title">Timeline</div>
    <div class="tl">
      <div class="tl-item"><div class="tl-dot tl-done"></div><div class="tl-title">v1.0 — Terminal RPG</div><div class="tl-desc">Rich TUI, skill packs, XP/levels, achievements</div><div class="tl-date">Mar 25, 2026</div></div>
      <div class="tl-item"><div class="tl-dot tl-done"></div><div class="tl-title">v1.5 — Web Mode</div><div class="tl-desc">FastAPI + Jinja2, 2 themes, multi-pack hub</div><div class="tl-date">Mar 27, 2026</div></div>
      <div class="tl-item"><div class="tl-dot tl-done"></div><div class="tl-title">v2.0 — Full Platform</div><div class="tl-desc">Postgres, auth, 8 themes, PWA, sounds, daily challenges, leaderboards, 13+ page types</div><div class="tl-date">Mar 28, 2026</div></div>
      <div class="tl-item"><div class="tl-dot tl-done"></div><div class="tl-title">6 Games Launch</div><div class="tl-desc">Primer, NEXUS Quest, AI Academy, Learn Chinese, Learn Spanish, Learn Japanese</div><div class="tl-date">Mar 30, 2026</div></div>
      <div class="tl-item"><div class="tl-dot tl-done"></div><div class="tl-title">TTS + Rich Media</div><div class="tl-desc">Google Cloud Studio voices, ElevenLabs, images, code blocks, AI Tutor</div><div class="tl-date">Mar 31, 2026</div></div>
      <div class="tl-item"><div class="tl-dot tl-done"></div><div class="tl-title">v2.5 — Anti-Cheat + Engagement</div><div class="tl-desc">Option shuffle, streak freeze, speed bonus, daily login rewards, spaced repetition, 100+ chapters</div><div class="tl-date">Apr 3, 2026</div></div>
      <div class="tl-item"><div class="tl-dot tl-active"></div><div class="tl-title">v3.0 — Unified Platform</div><div class="tl-desc">One deployment, all games as courses, single sign-on, course creator</div><div class="tl-date">Coming soon</div></div>
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-title">v4.0 — Social + Mobile</div><div class="tl-desc">Multiplayer, mobile app, social automation, email reports</div><div class="tl-date">Planned</div></div>
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-title">v5.0 — Ecosystem</div><div class="tl-desc">Classroom mode, certificates, challenge editor, plugin marketplace</div><div class="tl-date">Future</div></div>
    </div>
  </div>

  <div class="footer">
    <a href="https://github.com/thorski1/quest-engine">Quest Engine</a> · Open Source · MIT License<br>
    Built by <a href="https://github.com/thorski1">thorski1</a> · Last updated Apr 3, 2026
  </div>

</div>
</body>
</html>"""


async def homepage(request):
    return HTMLResponse(HTML)


app = Starlette(routes=[Route("/", homepage), Route("/{path:path}", homepage)])
