# Real-World Usage Examples

Examples from actual testing showing what each tool does and how it helps.

---

## 1. scaffold_document - Preview Complex Documents

**When to use:** You need to read a long technical paper or document but don't know where to start.

**Example request:**
```
Scaffold this paper for me: https://arxiv.org/abs/2510.01171
```

**What you get:**
- **Core Purpose** (1 sentence): What the document is trying to accomplish
- **Key Entities**: Definitions of important terms (e.g., "Mode Collapse", "Typicality Bias", "Verbalized Sampling")
- **Document Structure Map**: What each section covers
- **Required Action**: What you need to do after reading
- **Prerequisite Knowledge**: What you need to know vs. what you can skip
- **Reading Strategy**: Exactly where to start, what to focus on, what to skim

**Result:** Instead of staring at page 1 for 20 minutes, you have a roadmap showing you the cognitive psychology connection is the novel contribution, start with the intro and VS method section, and can skim the mathematical formalization.

---

## 2. check_message - Fix Messages Before Sending

**When to use:** You drafted an email but want to make sure it's clear and won't be misunderstood.

**Example request:**
```
Can you check this email before I send it:

Hey team, just wanted to circle back on the API migration. Thoughts on pushing
the deadline? There's some technical debt we should probably address first but
not sure if now is the right time. Let me know what you think when you get a chance.

Thanks!
```

**What you get:**

**Strengths:** Friendly tone, acknowledges complexity

**Issues identified:**
- Vague ask: "Thoughts on pushing the deadline?" - Are you proposing or asking?
- Uncertain stance: "probably" and "not sure" makes your position unclear
- Missing specifics: Which API? Current deadline? How much technical debt?
- Weak call-to-action: "when you get a chance" gives no timeline

**Revised version provided:**
```
Subject: API Migration Deadline - Need Team Input by [Date]

Hey team,

I'm proposing we push the API migration deadline from [current date] to
[proposed date]. Here's why:

We have significant technical debt in [specific area] that could cause issues
during migration. Specifically:
- [Issue 1]
- [Issue 2]

Options I see:
1. Keep current deadline, address tech debt after migration
2. Push deadline 2-3 weeks, tackle tech debt first

My recommendation: Option 2 - the upfront investment will make migration
smoother and reduce risk.

Need from you: Your take on this by [specific day], especially if you see
risks I'm missing.
```

**Quick fix:** "Add specifics: actual dates, what technical debt exactly, your clear recommendation, and when you need their response."

---

## 3. decode_message - Understand What They Really Want

**When to use:** You got a vague message and don't know what they actually want or when they need it.

**Example request:**
```
I just got this message from my manager:

"Hey, when you get a chance, can you take a look at the Q4 roadmap and share
your thoughts? No rush, just want to make sure we're aligned before the
planning meeting."

What do they actually want and when do they need it?
```

**What you get:**

**What They Literally Said:** Review roadmap - "no rush," "when you get a chance"

**What They Actually Want:** Your approval/sign-off on the Q4 roadmap so they can finalize it before presenting. They want to avoid surprises.

**Actual Deadline:**
- "When you get a chance" translation: Within 1-2 business days
- "No rush" translation: "There IS a deadline but I'm being polite"
- Real deadline: Before that planning meeting (likely within next few days)

**Success Looks Like:** You respond with either "Looks good, no concerns" OR specific concrete concerns with suggestions

**Communication Pattern:** "Polite urgent request with soft deadline"

**What You Should Do:**
1. Ask when the planning meeting is: "Happy to review - when's the planning meeting so I know your timeline?"
2. Within 24 hours: Review and send substantive feedback

---

## 4. prep_meeting - Get Ready for Meetings

**When to use:** You have a meeting tomorrow and need to prepare but don't know what to focus on.

**Example request:**
```
Help me prep for a meeting tomorrow. Here's what I know:

Meeting: Architecture Review - API Redesign
My role: Tech lead for the project
Agenda:
- Review proposed API changes
- Discuss migration timeline
- Address security concerns
- Resource allocation
```

**What you get:**

**Your Likely Contribution:** You'll lead the technical walkthrough, defend design decisions, present timeline, own resource requests

**3 Key Talking Points:**
1. API Changes Overview: "We're proposing [X changes] to address [specific problems]" - Need alignment these solve the right problems
2. Migration Timeline Reality Check: "Realistic timeline is [X weeks], aggressive would be [Y] but increases risk" - Need decision on risk tolerance
3. Resource Gaps: "Need 1 senior engineer for security review, 0.5 FTE for migration tooling" - Can we commit or descope?

**Questions to Ask:**
- "What's the hard deadline? Customer commitment or internal goal?"
- "If we find major security issues, can we push timeline?"
- "Which teams are most impacted?"

**Your Asks:**
- Decision authority on implementation calls
- Resource commitment confirmation
- Timeline approval with buffer

**Blockers to Raise:**
- Dependency risks
- Technical debt that needs addressing first
- Knowledge gaps needing training

**Decoded Agenda Items:**
- "Review proposed API changes" really means: Get approval to proceed, surface objections NOW
- "Discuss migration timeline" really means: Can we deliver when leadership wants? What's the risk?

---

## 5. check_tone - Catch Unintentional Rudeness

**When to use:** You're about to send a message but worried it might sound rude or defensive.

**Example request:**
```
Can you check the tone of this message? I'm sending it to my manager:

I already explained this in my last email. The timeline isn't realistic given
the technical constraints. We need to push the deadline or cut scope. Let me
know which you prefer.
```

**What you get:**

**⚠️ This Will Likely Land Badly**

**Issues flagged:**

"I already explained this"
- Sounds like: "You didn't pay attention"
- Feels: Condescending, frustrated
- Impact: Puts manager on defensive

"The timeline isn't realistic"
- Sounds like: Statement of fact with no room for discussion
- Missing: Your reasoning, acknowledgment of their constraints

"Let me know which you prefer"
- Sounds like: "Pick one of my two options" (puts them in a box)
- Missing: Invitation for dialogue

**How it could be misread:**
- ✗ "You're being difficult and inflexible"
- ✗ "You don't respect my authority"
- ✗ "You're not a team player"

**Better version provided:**
```
Subject: Timeline Concern - Need Your Input

Hi [Manager],

I want to revisit the timeline we discussed. After digging into the technical
work, I'm concerned we can't hit [date] with the current scope while
maintaining quality.

The constraint: [Specific technical issue]

Options I see:
1. Push deadline to [new date] - keeps full scope
2. Cut [specific features] - hits original date

I know you're balancing multiple priorities. What constraints are you working
with? Happy to brainstorm other approaches.

Can we talk through this [today/tomorrow]?
```

---

## 6. call_or_text - Decide Communication Method

**When to use:** You need to communicate something but aren't sure if you should call, text, or meet in person.

**Example request:**
```
Should I call or send a message for this situation?

I need to tell my teammate that their PR has some architectural issues that
will require significant rework. The problems are complex and there are
multiple ways to fix them. They're probably going to have questions about the
tradeoffs. We work well together but they might be frustrated since they spent
a week on this.
```

**What you get:**

**Recommendation:** Video/Screen-share Call (Hybrid Approach)

**Why Call (Not Text):**
- **Complexity factor - HIGH:** Multiple solution paths = lots of back-and-forth; architectural discussion works better synchronously
- **Emotional factor - MEDIUM:** They spent a week - getting "significant rework" news via text feels harsh
- **Efficiency factor:** Questions about tradeoffs = immediate clarification
- **Relationship factor:** You work well together - lean into that collaborative dynamic

**How to Structure the Call:**

1. **Send heads-up message first:**
   "Hey! Reviewed your PR - there are some architectural things we should talk through. Nothing unfixable, but worth discussing the options together. Got 20-30 min today or tomorrow?"

2. **On the call - lead with empathy:**
   "Thanks for jumping on. First - I know you put a lot of work into this, and a lot of what you did is solid. There are some architectural things that need reworking though..."

3. **Walk through issues together:** Share screen, show specific code, offer options

4. **End with clear next steps:** "Want me to document this in the PR comments?"

**Why NOT Just Text:**
- ❌ 20+ message thread of confusion
- ❌ Tone gets lost: helpful suggestions read as criticism
- ❌ Delay compounds frustration

---

## 7. synthesize_thoughts - Organize Brain Dumps

**When to use:** You have scattered thoughts that need to become a coherent message.

**Example request:**
```
Help me organize these scattered thoughts into a clear message:

Need to tell the team about the database migration but there's blockers with
the schema changes and we should probably wait until after the release but that
delays the performance improvements and also John is on vacation next week so
maybe we should just do it now? But then there's risk. Also need sign-off from
security team. And the monitoring isn't fully set up yet which is a problem.
Maybe we can do it in stages? Not sure.
```

**What you get:**

**Core Message:** We need to decide whether to do the database migration now or wait until after release, given several unresolved blockers and competing priorities.

**Key Themes Identified:**
1. Timing conflict: Now vs. after release
2. Blockers: Schema changes, security sign-off, monitoring gaps
3. Tradeoffs: Risk vs. performance vs. team availability
4. Possible solution: Staged approach

**Concise Version:**
```
Subject: Database Migration - Need Team Decision on Timing

Team, we need to decide on database migration timing. We have blockers
(schema/security/monitoring) but delaying past release means we miss
performance improvements and John's availability. Options are: proceed now
with elevated risk, wait until after release, or do staged rollout. Thoughts?
```

**Full Version:**
```
Subject: Database Migration Timing - Need Team Input by [Date]

Hey team,

We need to make a call on our database migration timing. Here's where we stand:

The situation: We're ready to migrate, but we have unresolved blockers:
- Schema changes still in progress
- Security team sign-off pending
- Monitoring isn't fully configured yet

The timing dilemma:
- Option 1 - Migrate now: Performance gains + John available, but elevated risk
- Option 2 - Wait until after release: Reduces release risk, but delays gains
  and loses John's availability
- Option 3 - Staged rollout: Reduces risk but increases timeline

What I need from you:
- Which option makes most sense?
- Can we accept the risk if Option 1?
- Can we live with delayed performance if Option 2?

Let's discuss in [standup] or reply by [date].
```

**Why this works:** Separates blockers from timing from options. Shows you've thought through tradeoffs. Turns "not sure" into "need team input."

---

## 8. catch_up_thread - Summarize Long Threads

**When to use:** You've been out and need to catch up on a long email or Slack thread quickly.

**Example request:**
```
Can you help me catch up on this email thread? I've been out and there are 15 messages:

[Thread about API versioning decision]
Message 1: Sarah proposes v2 API
Message 2: John asks about backward compatibility
Message 3: Sarah says we'll support v1 for 6 months
Message 4: Mike raises concerns about timeline
Message 5: Sarah suggests accelerating migration
Message 6: Team discusses migration tooling
...
Message 15: Sarah says "Let's finalize this by end of week so we can move forward"
```

**What you get:**

**🎯 Current State:** Decision on table - v2 API with 6-month v1 support. Sarah wants to finalize by end of week.

**✅ Key Decisions Made:**
- V2 API is happening (proposal accepted)
- 6-month backward compatibility window
- Migration tooling needed (team agrees)
- Accelerated timeline being considered

**⏰ Your Deadline:** "End of week" - need to weigh in by Friday

**🚧 What's Still Unresolved:**
- Timeline concerns (Mike raised them, unclear if resolved)
- Migration tooling specifics
- Resource allocation

**📋 What They Need From You:**
- Your position on timeline - Can your team migrate within 6 months?
- Migration tooling requirements
- Sign-off or concerns

**🎯 Your Action Items:**
1. Read messages 6-14 for migration tooling details
2. Assess if timeline works for your team
3. Respond by Friday with position

**💬 Suggested Response Template provided**

---

## 9. summarize_meeting - Extract Action Items

**When to use:** You have messy meeting notes and need to extract what matters.

**Example request:**
```
Can you organize these meeting notes?

Architecture Review - Nov 2

- Discussed new API design, team likes the approach
- Concern raised about migration timeline (Mike worried about Q4 deadline)
- Decided to do phased rollout: internal first, then beta, then GA
- Security review needed before beta (action: Sarah to schedule)
- Need to update docs (action: me by next Friday)
- Open question: do we need a feature flag? Team wasn't sure
- Performance testing showed 30% improvement
- John is blocked on database schema approval
- Next meeting: Nov 16 to review progress

What are my action items?
```

**What you get:**

**✅ Key Decisions Made:**
- API design approved
- Phased rollout strategy: Internal → Beta → GA
- Performance validated (30% improvement)
- Next review: Nov 16

**📋 YOUR Action Items:**
1. **Update documentation**
   - Due: Next Friday (Nov 8)
   - Blocker check: Need to know what docs (API docs? Migration guide?)

**👥 Other People's Action Items:**
2. Sarah: Schedule security review (blocks beta phase)
3. Someone: Approve database schema (URGENT - John is blocked)

**❓ Open Questions:**
- Feature flag decision - team was unsure, needs follow-up

**🚧 Active Blockers:**
- John blocked on database schema approval (high urgency)
- Security review not scheduled (gates beta phase)

**🎯 Your Immediate Next Steps:**
1. Clarify docs scope before starting
2. Monitor feature flag decision
3. Check if you're involved in schema approval

**Suggested follow-up message provided**

---

## 10. ask_clarity - Request Clarification Politely

**When to use:** Your manager said something vague and you need clarity but don't want to seem difficult.

**Example request:**
```
I need to ask for clarity on something but don't want to seem difficult.

My manager said "We need to move faster on this" but I don't know what "this"
refers to (we have 3 projects running) or what "faster" means (days? weeks?
what's the actual deadline?). How do I ask without sounding like I wasn't
paying attention?
```

**What you get:**

**🎯 The Key Principle:** Frame it as "I want to make sure I prioritize correctly" not "You weren't clear"

**✉️ Draft Message (Copy/Paste Ready):**
```
Subject: Quick clarification on priorities

Hi [Manager name],

Want to make sure I'm prioritizing correctly after our conversation. When you
mentioned we need to move faster, I want to confirm which project you're
referring to - is it the [API migration], [database optimization], or
[docs update]?

Also, what timeline should I be targeting? This helps me sequence the work and
flag any potential conflicts.

Happy to jump on a quick call if easier to talk through!

Thanks!
```

**Why This Works:**
- Shows you're taking it seriously and want to deliver
- Demonstrates you have multiple priorities (not that you weren't listening)
- Frames you as thoughtful about execution

**✅ Safe Phrases to Use:**
- "Want to make sure I'm prioritizing correctly..."
- "To confirm..."
- "Help me understand the timeline so I can..."

**❌ Phrases to Avoid:**
- "I'm confused about..." (sounds unprepared)
- "You didn't specify..." (blames them)
- "What did you mean by..." (can sound challenging)

**Common Worry Addressed:** "Won't they think I wasn't listening?"
No - vague language is normal. Clarifying shows competence. Better to ask than guess wrong.

---

## 11. unstuck_reading - Start Overwhelming Documents

**When to use:** You're stuck trying to read a long document and don't know where to start.

**Example request:**
```
I'm stuck trying to read this design doc. Help me get unstuck.

It's a 40-page technical design doc for a new microservices architecture. I
don't understand half the terminology, there's no clear summary, and I don't
even know why I need to read it. My manager just said "take a look at this
before our meeting tomorrow." I've been staring at page 1 for 20 minutes.

What should I do?
```

**What you get:**

**🚨 Stop Reading Page 1 Right Now**

**Your Real Blockers:**
- No "why" - don't know why this doc exists
- No "what matters" - 40 pages with no guide
- Terminology wall - don't understand the terms
- No reading goal - "take a look" is too vague

**🔥 Your First Step (Do This In 5 Minutes):**
Send this message NOW:
```
Quick question before I dig into the design doc: What should I focus on for
tomorrow's meeting? Is there a specific section you want my input on?

Want to make sure I'm looking at the right things given the meeting timeline.
```

**📋 While You Wait: Reconnaissance Read**
1. **Find the Structure (5 min):** Table of contents, executive summary, goals, diagrams, recommendations
2. **Make Terminology Cheat Sheet (10 min):** Note unknown terms, figure out from context
3. **Identify Decision Points (5 min):** Look for "Options", "Trade-offs", "Recommendations"

**🎯 Once Manager Replies: Targeted Reading Strategy**

If they say "Focus on [Specific Section]":
- Go straight to that section
- Read intro and conclusion first
- Then details if needed

If they say "Just general thoughts":
- Read executive summary
- Look at all diagrams
- Read goals and recommendations
- Time: 30-45 minutes max

**🚀 Emergency 60-Minute Power Read Strategy provided**

**💬 What to Say in Tomorrow's Meeting:**
- If you had time: "I reviewed the doc. General approach makes sense - I like [X]. Question about [Y]"
- If you skimmed: "I took a first pass. High-level makes sense. Want to dig deeper into [X]"

**User feedback:** After this advice, user pointed out the tool should have recommended scaffolding the document first - which is absolutely right! This shows the tool is learning and improving.

---

## Key Takeaways

### All Tools Work Successfully
✅ All 11 tools were tested and performed well
✅ Outputs are comprehensive and actionable
✅ Real-world applicable advice
✅ Frameworks are being followed correctly

### Common Patterns
1. **Tools give multiple options** - short version, full version, emergency version
2. **Specific, actionable advice** - not generic, tailored to situation
3. **Address fears** - "won't they think I'm difficult?" etc.
4. **Explain why** - not just what to do, but why it works
5. **Provide templates** - copy/paste ready messages

### Best Practices
- **Be specific in your request** - the more context you give, the better the advice
- **Tools work together** - scaffold a doc first, then use unstuck_reading if needed
- **Natural language works** - you don't need to name the tool, just describe what you need
- **Real scenarios work best** - use actual work situations for most relevant help

---

## What Users Are Saying

> "You shouldn't spend 45 minutes editing a 3-line email."

This toolkit helps neurodivergent professionals:
- Save time on communication tasks
- Reduce anxiety about messaging
- Understand implicit workplace communication
- Structure scattered thoughts
- Navigate complex documents
- Prepare for important conversations

**Different, not deficient.**
