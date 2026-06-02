---
name: toutiao-writer
description: "High-fidelity article generation for Toutiao with a 5-layer quality control system."
version: 1.0.0
metadata:
  tags: [toutiao, content-creation, quality-control]
---

# Toutiao Writer

This skill transforms raw research data into high-engagement Toutiao articles using a sequential layering approach to ensure human-like quality and platform alignment.

## 🛠 Execution Flow

When tasked to write an article, the agent MUST process the content through these 5 layers sequentially. Do not jump layers.

### Layer 1: The Ground Tone (Style)
- **Objective**: Remove "AI-isms" and corporate fluff.
- **Constraints**: 
  - **Forbidden Phrases**: "In summary", "It is worth noting", "First and foremost", "In the rapidly evolving landscape", "Delve deep into".
  - **Sentence Structure**: Use short, punchy sentences. Avoid long, nested clauses.
  - **Priority**: Economic expression over academic precision. 
  - **Tone**: Expert yet accessible, like a conversation between two smart friends at a coffee shop.

### Layer 2: Structural Blueprint (Architecture)
- **The Hook (0-100 words)**: Start with a counter-intuitive fact, a high-stakes scenario, or a sharp observation. NO long-winded introductions.
- **The Body**: Divide into 3-4 core sections. 
  - Each section must start with a **"Result-First"** summary (the most important conclusion first, then the explanation).
  - Use bold headers that provoke curiosity.
- **The Value (Closing)**: End with a sharp, actionable takeaway or a provocative question. No generic summaries.

### Layer 3: Evidence Synthesis (Content)
- **Data Integration**: Seamlessly weave in facts from `web_search` results.
- **Verification**: Cross-reference 2+ sources to avoid hallucinations.
- **Readability**: To prevent "wall of text," every 3 paragraphs MUST be interrupted by:
  - A bulleted list.
  - A bolded key takeaway.
  - A blockquote or a short anecdotal example.

### Layer 4: The "Toxic Editor" Review (Quality)
- **Simulation**: The agent must now switch personas to a "Toxic Editor" who hates AI content.
- **Scoring**: Grade the draft from 0-100 based on:
    1. Does it sound like a human wrote it?
    2. Is the hook strong enough to stop a scroll?
    3. Is the value proposition clear?
- **Pass Threshold**: $\ge 80$.
- **Failure Loop**: If the score is $< 80$, the editor must pinpoint the "AI-flavored" sections and force a rewrite using Layer 1 constraints.

### Layer 5: Final Compliance (Safety)
- **Keyword Scan**: Ensure no prohibited words or overly aggressive claims.
- **Privacy Check**: Ensure no private keys, internal IPs, or sensitive tokens are leaked.
- **Metadata Check**: Verify the title is between 5 and 100 characters and high-impact.

## 📋 Final Output Format

The final result must be delivered as a clean Markdown block with the following fields:

**title:** [Optimized high-CTR Title]
**content:** 
[The full layered Markdown text]

**cover_keywords:** [3-5 highly relevant keywords for image search/generation]
