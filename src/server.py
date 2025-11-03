"""
Neurodivergent Communication MCP Server

Provides communication assistance tools and resources for neurodivergent
professionals in technical workplaces.
"""

from mcp.server.fastmcp import FastMCP
from pathlib import Path
import json

# Initialize MCP server
mcp = FastMCP("Neurodivergent Communications")

# Load resources
RESOURCES_DIR = Path(__file__).parent / "resources"


# ============================================================================
# RESOURCES - Background knowledge for the LLM
# ============================================================================

@mcp.resource("comms://rules/message-clarity")
def get_message_clarity_rules() -> str:
    """Communication clarity guidelines and patterns"""
    rules_path = RESOURCES_DIR / "message-clarity.md"
    return rules_path.read_text()


@mcp.resource("comms://rules/context-interpretation")
def get_context_interpretation_rules() -> str:
    """Guidelines for interpreting implicit context and subtext in messages"""
    rules_path = RESOURCES_DIR / "context-interpretation.md"
    return rules_path.read_text()


@mcp.resource("comms://rules/tone-calibration")
def get_tone_calibration_rules() -> str:
    """Guidelines for assessing and calibrating message tone"""
    rules_path = RESOURCES_DIR / "tone-calibration.md"
    return rules_path.read_text()


@mcp.resource("comms://rules/meeting-structure")
def get_meeting_structure_rules() -> str:
    """Guidelines for preparing, participating in, and following up on meetings"""
    rules_path = RESOURCES_DIR / "meeting-structure.md"
    return rules_path.read_text()


@mcp.resource("comms://rules/document-scaffolding")
def get_document_scaffolding_rules() -> str:
    """Guidelines for scaffolding and previewing complex documents"""
    rules_path = RESOURCES_DIR / "document-scaffolding.md"
    return rules_path.read_text()


# ============================================================================
# TOOLS - Functions the LLM can execute
# ============================================================================

@mcp.tool()
def check_message(draft: str, recipient: str = "", context: str = "") -> str:
    """
    Analyze a message draft before sending.

    Checks for:
    - Clarity (is the ask clear? is context sufficient?)
    - Tone (professional level, emotional tone, potential misinterpretations)
    - Structure (key info upfront, organized logically, appropriate length)
    - Completeness (all necessary context, action items clear, timeline specified)

    Args:
        draft: The message text to analyze
        recipient: Who will receive this message (optional, helps with tone assessment)
        context: Additional context about the situation (optional)

    Returns:
        Structured analysis with strengths, issues, revised version, and quick fix
    """

    # Build the analysis prompt
    analysis_sections = {
        "draft": draft,
        "recipient": recipient if recipient else "Not specified",
        "context": context if context else "Not provided"
    }

    # Return structured format for LLM to fill in
    return json.dumps({
        "input": analysis_sections,
        "analysis_framework": {
            "clarity_check": {
                "questions": [
                    "Is the ask/point clear?",
                    "Is context sufficient?",
                    "Are there ambiguous terms?",
                    "Would recipient know what to do next?"
                ]
            },
            "tone_assessment": {
                "questions": [
                    "Professional level appropriate?",
                    "Emotional tone clear?",
                    "Any unintended subtext?",
                    "Matches relationship with recipient?"
                ]
            },
            "structure": {
                "questions": [
                    "Key info upfront?",
                    "Organized logically?",
                    "Appropriate length?",
                    "Easy to skim?"
                ]
            },
            "completeness": {
                "questions": [
                    "All necessary context included?",
                    "Questions answered proactively?",
                    "Action items clear?",
                    "Timeline specified if needed?"
                ]
            }
        },
        "output_format": {
            "strengths": "List what works well",
            "issues": "List what needs fixing (be specific)",
            "revised_version": "Show improved version if issues found",
            "quick_fix": "One-liner summary of main change needed"
        }
    }, indent=2)


@mcp.tool()
def decode_message(message: str, sender: str = "", relationship: str = "") -> str:
    """
    Decode confusing or vague messages to extract actual meaning.

    Extracts:
    - Explicit ask (what they literally said)
    - Implicit ask (what they actually want)
    - Actual deadline (decode "when you get a chance" type phrases)
    - Success criteria (what does done look like?)
    - Expected response (do they want action, info, or just acknowledgment?)
    - Common pattern (identifies typical workplace communication patterns)

    Args:
        message: The confusing message to decode
        sender: Who sent it (e.g., "manager", "peer", "direct report")
        relationship: Nature of relationship (optional, helps with context)

    Returns:
        Structured breakdown of explicit vs implicit meaning
    """

    analysis_data = {
        "message": message,
        "sender": sender if sender else "Not specified",
        "relationship": relationship if relationship else "Not specified"
    }

    return json.dumps({
        "input": analysis_data,
        "decode_framework": {
            "explicit_ask": "What they literally said they want",
            "implicit_ask": "What they actually want (read between the lines)",
            "actual_deadline": "Real timeline (decode vague phrases like 'when you get a chance')",
            "success_criteria": "What does 'done' look like? What are they trying to unblock?",
            "expected_response": "Do they want: action, information, acknowledgment, or something else?",
            "communication_pattern": "Identify pattern (e.g., 'polite urgent request', 'checking in', 'soft deadline')"
        },
        "common_vague_phrases": {
            "when you get a chance": "Usually means within 1-2 days unless stated otherwise",
            "no rush": "Often still has implicit deadline - check context",
            "thoughts?": "Usually wants specific feedback or approval to proceed",
            "can you take a look?": "Wants review/feedback, possibly approval",
            "just checking in": "Either needs status update or gentle deadline reminder"
        }
    }, indent=2)


@mcp.tool()
def prep_meeting(title: str, your_role: str, agenda: str = "") -> str:
    """
    Prepare for an upcoming meeting.

    Generates:
    - Your likely contribution (what you'll need to speak about)
    - 2-3 concise talking points
    - Questions you should ask
    - Your asks (what you need from others)
    - Potential blockers to raise
    - Decoded agenda items (what each item really means)

    Args:
        title: Meeting title/subject
        your_role: Your role in the meeting (e.g., "tech lead", "IC contributor", "project owner")
        agenda: Meeting agenda if available (optional)

    Returns:
        Structured meeting preparation guide
    """

    prep_data = {
        "meeting_title": title,
        "your_role": your_role,
        "agenda": agenda if agenda else "No agenda provided"
    }

    return json.dumps({
        "input": prep_data,
        "preparation_framework": {
            "your_contribution": "What you'll likely need to speak about based on your role",
            "talking_points": "2-3 concise points to communicate (structure: context → options → ask)",
            "questions_to_ask": "What you should clarify or ask others",
            "your_asks": "What you need from others in this meeting",
            "blockers_to_raise": "Issues that might block progress",
            "decoded_agenda": "What each agenda item actually means / what's expected"
        },
        "meeting_structure_tips": {
            "opening": "State your point upfront if asked to speak",
            "middle": "Provide necessary context only",
            "closing": "End with clear question or next step",
            "fallback": "If unsure when to speak, ask 'Would it help if I shared context on X?'"
        }
    }, indent=2)


@mcp.tool()
def scaffold_document(document_content: str, document_title: str = "") -> str:
    """
    Preview document structure before deep reading.

    Provides scaffolding to help with:
    - ADHD: Focus strategy before diving in
    - Dyslexia: Structure before detailed reading
    - Executive function: Clear approach reduces overwhelm

    Extracts:
    - Core purpose (1 sentence summary)
    - Key entities with definitions
    - Document structure map (sections and what they cover)
    - Required action/decision from the reader
    - Prerequisite knowledge needed
    - Reading strategy for this specific document

    Args:
        document_content: The document text to analyze
        document_title: Document title if available (optional)

    Returns:
        Structured document preview with reading strategy
    """

    scaffold_data = {
        "document_title": document_title if document_title else "Untitled document",
        "content_length": f"{len(document_content)} characters"
    }

    return json.dumps({
        "input": scaffold_data,
        "scaffolding_framework": {
            "core_purpose": "What this document is trying to accomplish (1 sentence)",
            "key_entities": "Main concepts, systems, or terms with brief definitions",
            "structure_map": {
                "description": "List sections and what each covers",
                "format": "Section name → What it contains"
            },
            "required_action": "What the reader needs to do after reading",
            "prerequisite_knowledge": "What you need to know before this makes sense",
            "reading_strategy": {
                "start_with": "Which section to read first",
                "focus_on": "Key information to prioritize",
                "skip_if_needed": "Less critical parts you can skim",
                "watch_for": "Important details not to miss"
            }
        },
        "document_content": document_content
    }, indent=2)


@mcp.tool()
def check_tone(message: str, recipient: str = "", relationship: str = "") -> str:
    """
    Validate message tone and check if it might be misinterpreted.

    Assesses:
    - Professional level (right formality for audience?)
    - Emotional tone (what emotion does it convey?)
    - Potential misinterpretations (could it be read as rude/defensive/dismissive?)
    - Relationship match (appropriate for your relationship with recipient?)

    Flags if message is:
    - Too blunt/direct for the audience
    - Unintentionally sounds annoyed or defensive
    - Missing necessary context that makes it seem abrupt
    - Not following professional norms

    Args:
        message: The message text to check
        recipient: Who will receive this (optional, helps with assessment)
        relationship: Your relationship with recipient (e.g., "manager", "peer", "direct report")

    Returns:
        Tone assessment with flags for potential issues
    """

    tone_data = {
        "message": message,
        "recipient": recipient if recipient else "Not specified",
        "relationship": relationship if relationship else "Not specified"
    }

    return json.dumps({
        "input": tone_data,
        "tone_assessment_framework": {
            "professional_level": {
                "current": "Assess formality (formal/standard/casual)",
                "appropriate": "Should it be at this level for this recipient?"
            },
            "emotional_tone": {
                "perceived_emotion": "What emotion does this convey?",
                "intended_emotion": "What did you intend?"
            },
            "potential_misinterpretations": {
                "could_sound_rude": "Check if direct language might seem rude",
                "could_sound_defensive": "Check if explanation sounds defensive",
                "could_sound_dismissive": "Check if brevity might seem dismissive"
            },
            "relationship_match": "Is tone appropriate for your relationship with recipient?"
        },
        "red_flags_to_check": {
            "all_caps": "ALL CAPS (except acronyms)",
            "multiple_exclamation": "Multiple !!!",
            "sarcasm": "Sarcastic language",
            "unintended_curtness": "Accidentally curt/abrupt"
        }
    }, indent=2)


@mcp.tool()
def call_or_text(situation: str, urgency: str = "", complexity: str = "") -> str:
    """
    Decide communication method - should you call or send a message?

    Considers:
    - Urgency (how time-sensitive is this?)
    - Complexity (how many back-and-forths will text require?)
    - Relationship (what's your working relationship?)
    - Your preference (what works better for you?)
    - Their likely preference (what's their communication style?)

    Args:
        situation: Description of what you need to communicate
        urgency: How urgent is this? (optional)
        complexity: How complex is the topic? (optional)

    Returns:
        Recommendation (call/text/video) with clear reasoning
    """

    decision_data = {
        "situation": situation,
        "urgency": urgency if urgency else "Not specified",
        "complexity": complexity if complexity else "Not specified"
    }

    return json.dumps({
        "input": decision_data,
        "decision_framework": {
            "urgency_assessment": {
                "immediate": "Call/video - needs resolution now",
                "today": "Call or detailed message - needs attention today",
                "this_week": "Message likely fine - can be async",
                "no_deadline": "Message - gives them time to process"
            },
            "complexity_assessment": {
                "needs_discussion": "Call/video - multiple decision points",
                "needs_clarification": "Quick call or video - faster than async",
                "straightforward": "Message - clear enough for async",
                "yes_no_question": "Message - simple response needed"
            },
            "recommendation": {
                "method": "call | text | video",
                "reasoning": "Why this method is best for this situation",
                "alternative": "If primary method doesn't work, try this"
            }
        }
    }, indent=2)


@mcp.tool()
def synthesize_thoughts(brain_dump: str) -> str:
    """
    Organize scattered thoughts into clear message.

    Supports bottom-up processing: Start with details, build to structure.
    Takes the Lego pieces and shows what can be built from them.

    Extracts:
    - Core message (1-2 sentences)
    - Key themes from the details
    - Logical structure for organizing
    - Concise version (3-4 sentences)
    - Full version with all important details

    Args:
        brain_dump: Unstructured thoughts to organize

    Returns:
        Structured message with both concise and full versions
    """

    return json.dumps({
        "input": {
            "brain_dump": brain_dump,
            "word_count": len(brain_dump.split())
        },
        "synthesis_framework": {
            "core_message": "Distill to 1-2 sentence essence",
            "key_themes": "Identify main themes from the details",
            "logical_structure": {
                "suggested_flow": "Best order to present these ideas",
                "groupings": "Which points belong together"
            },
            "concise_version": "3-4 sentences hitting the key points",
            "full_version": "Complete message with all important details organized"
        },
        "bottom_up_process": {
            "details_provided": "The Lego pieces (your brain dump)",
            "structure_identified": "How the pieces fit together",
            "final_built": "The finished structure"
        }
    }, indent=2)


@mcp.tool()
def catch_up_thread(thread_content: str, thread_subject: str = "") -> str:
    """
    Catch up on long email/Slack thread.

    Extracts:
    - Current state (where things stand now)
    - Key decisions made in the thread
    - What they're asking from you now
    - Deadlines mentioned
    - Who's blocked on what

    Args:
        thread_content: The full thread/email chain
        thread_subject: Subject line if available (optional)

    Returns:
        Structured summary of thread with your action items
    """

    thread_data = {
        "subject": thread_subject if thread_subject else "No subject provided",
        "message_count": thread_content.count("\n\n") + 1,
        "content_length": f"{len(thread_content)} characters"
    }

    return json.dumps({
        "input": thread_data,
        "catch_up_framework": {
            "current_state": "Where things stand right now",
            "key_decisions": "Decisions that have been made in this thread",
            "your_action_items": "What they need from you specifically",
            "deadlines": "Any timeline or deadline mentioned",
            "blockers": {
                "who_is_blocked": "Who is waiting on something",
                "blocked_on_what": "What they're waiting for",
                "blocked_on_you": "Are they waiting on you?"
            },
            "next_response": "What you should respond with"
        },
        "thread_content": thread_content
    }, indent=2)


@mcp.tool()
def summarize_meeting(meeting_notes: str, meeting_title: str = "") -> str:
    """
    Organize meeting notes and extract decisions/action items.

    Extracts:
    - Key decisions made
    - Action items (who/what/when)
    - Open questions still unanswered
    - Blockers identified
    - What you need to do next

    Args:
        meeting_notes: Raw meeting notes to organize
        meeting_title: Meeting title if available (optional)

    Returns:
        Structured summary with action items and decisions
    """

    meeting_data = {
        "title": meeting_title if meeting_title else "Untitled meeting",
        "notes_length": f"{len(meeting_notes)} characters"
    }

    return json.dumps({
        "input": meeting_data,
        "summary_framework": {
            "key_decisions": "Decisions that were made",
            "action_items": {
                "format": "List each action with who/what/when",
                "your_items": "Action items assigned to you",
                "others_items": "Action items assigned to others"
            },
            "open_questions": "Questions raised but not answered",
            "blockers": "Issues that could block progress",
            "your_next_steps": "What you need to do immediately after this meeting"
        },
        "meeting_notes": meeting_notes
    }, indent=2)


@mcp.tool()
def ask_clarity(confusing_situation: str, person_to_ask: str = "") -> str:
    """
    Draft a message asking for clarity without seeming difficult.

    Provides:
    - Polite way to ask what they mean
    - Specific questions to ask
    - Tone that sounds collaborative not confrontational

    Uses safe phrases like:
    - "To confirm..."
    - "Want to make sure I understand..."
    - "Just to clarify the timeline..."
    - "Help me understand..."

    Args:
        confusing_situation: What you're confused about
        person_to_ask: Who you're asking (optional, helps with tone)

    Returns:
        Draft message asking for clarity in a collaborative tone
    """

    clarity_data = {
        "situation": confusing_situation,
        "asking": person_to_ask if person_to_ask else "Not specified"
    }

    return json.dumps({
        "input": clarity_data,
        "clarity_request_framework": {
            "safe_opening_phrases": [
                "To confirm...",
                "Want to make sure I understand...",
                "Just to clarify...",
                "Help me understand...",
                "Quick question to make sure we're aligned..."
            ],
            "specific_questions": "List the specific things you need clarified",
            "collaborative_tone": {
                "frame_as": "Ensuring alignment, not questioning their clarity",
                "avoid": "Anything that sounds like 'you were unclear'",
                "emphasize": "Your need to understand, not their failure to explain"
            },
            "draft_message": "Complete draft message asking for clarity"
        }
    }, indent=2)


@mcp.tool()
def unstuck_reading(document_description: str, blocking_issue: str = "") -> str:
    """
    Get unstuck when unable to start reading a document.

    Identifies:
    - What's blocking you (lack of context, unclear purpose, too long, don't know what to focus on)
    - Concrete first step to take
    - Reading strategy for this specific doc
    - What to focus on first (and what to skip for now)

    Args:
        document_description: Brief description of the document you're stuck on
        blocking_issue: What's specifically blocking you (optional)

    Returns:
        Strategy to get unstuck and start reading
    """

    unstuck_data = {
        "document": document_description,
        "blocking_issue": blocking_issue if blocking_issue else "Not specified"
    }

    return json.dumps({
        "input": unstuck_data,
        "unstuck_framework": {
            "identify_blocker": {
                "lack_of_context": "Don't understand why this document exists",
                "unclear_purpose": "Don't know what you need from it",
                "overwhelming_length": "Too long, don't know where to start",
                "focus_uncertainty": "Don't know what's important vs not"
            },
            "concrete_first_step": "Single specific action to take right now",
            "reading_strategy": {
                "order": "What to read in what order",
                "focus": "What to pay attention to",
                "skip": "What you can skip or skim for now"
            },
            "focus_first": "The one thing to focus on first before anything else"
        }
    }, indent=2)


# ============================================================================
# Server startup
# ============================================================================

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
