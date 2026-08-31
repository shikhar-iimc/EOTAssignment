"""
data.py - Single source of truth for all content on the site.
Every factual claim here traces to a source in SOURCES. Interpretive/
analytical content (narrative placement, our commentary) is kept in
separate fields and labeled as such in the UI - never mixed silently
with sourced facts.
"""

# ---------------------------------------------------------------------------
# COLOR SCHEME - dark, high-contrast, operations-console palette
# ---------------------------------------------------------------------------
INK = "#0A0E12" # near-black background
PANEL = "#12181F" # panel/card background
PANEL_LIGHT = "#1A2229" # slightly lighter panel
PAPER = INK # kept for backward compatibility with older imports
PAPER_DARK = PANEL
RUST = "#D9663B" # warm alert/accent
GOLD = "#D4A72C" # amber accent
STEEL = "#7FA8C9" # cool steel-blue accent
SAGE = "#8FBB8C" # muted green accent
GREY = "#9AA5AD" # secondary text on dark
TEXT = "#E8EDF1" # primary text on dark
LINE = "#2A343D" # hairline borders on dark

COMPANY_COLOR = {
 "Palantir": RUST,
 "Google": GOLD,
 "Anthropic": SAGE,
 "DoD": STEEL,
 "OpenAI": "#C9CDD3",
 "Microsoft": "#7FA8C9",
 "NVIDIA": "#8FBB8C",
 "UN": "#B08FD6",
}

# ---------------------------------------------------------------------------
# SOURCES - every citation used anywhere on the site, keyed by short id
# ---------------------------------------------------------------------------
SOURCES = {
 "malmio2023": {
 "label": "Malmio, I. (2023). Ethics as an enabler and a constraint. Technology in Society, 72, 102193.",
 "url": "https://doi.org/10.1016/j.techsoc.2022.102193",
 "type": "Course reading (assigned, Session 15)",
 },
 "floridi2023": {
 "label": "Floridi, L. (2023). On good and evil, the mistaken idea that technology is ever neutral. Philosophy & Technology, 36, 60.",
 "url": "https://doi.org/10.1007/s13347-023-00661-4",
 "type": "Course reading (Session 9)",
 },
 "winner1980": {
 "label": "Winner, L. (1980). Do artifacts have politics? Daedalus, 109(1), 121–136.",
 "url": "https://www.jstor.org/stable/20024652",
 "type": "Course reading (Session 9)",
 },
 "palantir_manifesto": {
 "label": "Palantir (@PalantirTech). \u201cThe Technological Republic, in brief.\u201d X, 19 April 2026.",
 "url": "https://x.com/PalantirTech",
 "type": "Primary source",
 },
 "karp_book": {
 "label": "Karp, A. C., & Zamiska, N. W. (2025). The Technological Republic. Crown Currency.",
 "url": "https://techrepublicbook.com/",
 "type": "Primary source",
 },
 "cnbc_google2025": {
 "label": "CNBC. \u201cGoogle removes pledge to not use AI for weapons, surveillance.\u201d 4 Feb 2025.",
 "url": "https://www.cnbc.com/2025/02/04/google-removes-pledge-to-not-use-ai-for-weapons-surveillance.html",
 "type": "News",
 },
 "wapo_google2025": {
 "label": "Washington Post. \u201cGoogle drops pledge not to use AI for weapons or surveillance.\u201d 4 Feb 2025.",
 "url": "https://www.washingtonpost.com/technology/2025/02/04/google-ai-policies-weapons-harm/",
 "type": "News",
 },
 "dcd_google": {
 "label": "Data Center Dynamics. \u201cGoogle ditches promise not to develop AI weapons.\u201d",
 "url": "https://www.datacenterdynamics.com/en/news/google-ditches-promise-not-to-develop-ai-weapons/",
 "type": "News",
 },
 "stopkillerrobots": {
 "label": "Stop Killer Robots. \u201cArtificial intelligence experts call for ban.\u201d",
 "url": "https://www.stopkillerrobots.org/news/aicall/",
 "type": "Primary source (2015 open letter)",
 },
 "markey_letter": {
 "label": "Markey, E. Letter to Google on AI Principles Revisions. 19 Feb 2025.",
 "url": "https://www.markey.senate.gov/download/letter-to-google-on-ai-principles-revisions?download=1",
 "type": "Primary source",
 },
 "engadget_manifesto": {
 "label": "Engadget. \u201cPalantir posted a manifesto that reads like the ramblings of a comic book villain.\u201d",
 "url": "https://www.engadget.com/big-tech/palantir-posted-a-manifesto-that-reads-like-the-ramblings-of-a-comic-book-villain-181947361.html",
 "type": "News/commentary",
 },
 "wion_manifesto": {
 "label": "WION. \u201cPalantir's manifesto calls for AI militarisation; critics call it technofascism.\u201d",
 "url": "https://www.wionews.com/world/palantir-manifesto-ai-militarisation-technofascism-debate-1776774249138",
 "type": "News/commentary",
 },
 "bloomberg_karp": {
 "label": "Bloomberg. \u201cPalantir's Call to Arms Is Also a Sales Pitch.\u201d 21 Feb 2025.",
 "url": "https://www.bloomberg.com/news/articles/2025-02-21/palantir-ceo-s-new-book-is-a-call-to-arms-and-a-sales-pitch",
 "type": "News/commentary",
 },
 "conversation_anthropic": {
 "label": "Schwarz, E., & Renic, N. \u201cAnthropic v the US military.\u201d The Conversation, 2026.",
 "url": "https://theconversation.com/anthropic-v-the-us-military-what-this-public-feud-says-about-the-use-of-ai-in-warfare-276999",
 "type": "News/academic commentary",
 },
 "npr_anthropic": {
 "label": "NPR. \u201cAnthropic sues the Trump administration over \u2018supply chain risk\u2019 label.\u201d 9 Mar 2026.",
 "url": "https://www.npr.org/2026/03/09/nx-s1-5742548/anthropic-pentagon-lawsuit-amodai-hegseth",
 "type": "News",
 },
 "cnbc_court": {
 "label": "CNBC. \u201cAnthropic, Defense Department face off in DC court over blacklisting.\u201d 19 May 2026.",
 "url": "https://www.cnbc.com/2026/05/19/anthropic-dod-blacklist-court-opening-arguments.html",
 "type": "News",
 },
 "yahoo_goldendome": {
 "label": "Yahoo/AP. \u201cPentagon's chief tech officer says he clashed with AI company Anthropic over autonomous warfare.\u201d",
 "url": "https://www.yahoo.com/news/articles/pentagons-chief-tech-officer-says-001423249.html",
 "type": "News",
 },
 "techcrunch_filing": {
 "label": "TechCrunch. \u201cNew court filing reveals Pentagon told Anthropic the two sides were nearly aligned...\u201d 20 Mar 2026.",
 "url": "https://techcrunch.com/2026/03/20/new-court-filing-reveals-pentagon-told-anthropic-the-two-sides-were-nearly-aligned-a-week-after-trump-declared-the-relationship-kaput/",
 "type": "News",
 },
 "wikipedia_dispute": {
 "label": "Wikipedia. \u201cAnthropic\u2013United States Department of Defense dispute.\u201d (Overview; verify against primary reporting.)",
 "url": "https://en.wikipedia.org/wiki/Anthropic%E2%80%93United_States_Department_of_Defense_dispute",
 "type": "Reference (secondary)",
 },
 "afsc_ecosystem": {
 "label": "American Friends Service Committee. \u201cPalantir's Tech Ecosystem.\u201d April 2026 (based on 2025 tax filings, press releases, and company documentation).",
 "url": "https://afsc.org/sites/default/files/2026-04/palantir-tech-ecosystem-final.pdf",
 "type": "Research report",
 },
 "semafor_rift": {
 "label": "Semafor. \u201cExclusive: Palantir partnership is at heart of Anthropic, Pentagon rift.\u201d 17 Feb 2026.",
 "url": "https://www.semafor.com/article/02/17/2026/palantir-partnership-is-at-heart-of-anthropic-pentagon-rift",
 "type": "News",
 },
 "cnbc_blacklist": {
 "label": "CNBC. \u201cDefense tech companies are dropping Claude after Pentagon's Anthropic blacklist.\u201d 4 Mar 2026.",
 "url": "https://www.cnbc.com/2026/03/04/pentagon-blacklist-anthropic-defense-tech-claude.html",
 "type": "News",
 },
 "bloomberg_palantir_shop": {
 "label": "Bloomberg. \u201cPalantir Explores New AI Partners After Pentagon Bars Anthropic From Contracts.\u201d 12 Mar 2026.",
 "url": "https://www.bloomberg.com/news/articles/2026-03-12/palantir-looks-to-expand-beyond-anthropic-after-pentagon-spat",
 "type": "News",
 },
 "csis_maven": {
 "label": "Center for Strategic and International Studies. \u201cWhat Is Maven Smart System, and What Does It Do?\u201d",
 "url": "https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do",
 "type": "Research / think tank analysis",
 },
 "aimagazine_replace": {
 "label": "AI Magazine. \u201cWhy did the US Government Replace Anthropic with OpenAI?\u201d 5 Mar 2026.",
 "url": "https://aimagazine.com/news/why-did-the-us-government-replace-anthropic-with-openai",
 "type": "News",
 },
 "yahoo_palantir_challenge": {
 "label": "Reuters (via Yahoo Finance). \u201cPalantir faces challenge to remove Anthropic from Pentagon's AI software.\u201d 4 Mar 2026.",
 "url": "https://finance.yahoo.com/news/palantir-faces-challenge-remove-anthropic-213754143.html",
 "type": "News",
 },
 "defensenews_iran": {
 "label": "The Defense News. \u201cPentagon Used Anthropic's Claude AI and Palantir Maven to Identify 1,000 Targets in Iran Strikes.\u201d 5 Mar 2026.",
 "url": "https://www.thedefensenews.com/news-details/Pentagon-Used-Anthropics-Claude-AI-and-Palantir-Maven-to-Identify-1000-Targets-in-Iran-Strikes/",
 "type": "News",
 },
 "defensefinance_dod4": {
 "label": "Defense Finance Monitor. \u201cAI at War: Google, OpenAI, Anthropic, and xAI Secure $200M DoD Contracts.\u201d",
 "url": "https://defencefinancemonitor.substack.com/p/ai-at-war-google-openai-anthropic",
 "type": "News",
 },
 "nvidia_palantir": {
 "label": "NVIDIA. \u201cPalantir and NVIDIA Team Up to Operationalize AI.\u201d 28 October 2025.",
 "url": "https://nvidianews.nvidia.com/news/nvidia-palantir-ai-enterprise-data-intelligence",
 "type": "Primary source (press release)",
 },
 "suchman_2020": {
 "label": "Suchman, L. (2020). Algorithmic warfare and the reinvention of accuracy. Critical Studies on Security, 8(2), 175\u2013187.",
 "url": "https://doi.org/10.1080/21624887.2020.1760587",
 "type": "Academic (peer-reviewed)",
 },
 "santoni_de_sio_2018": {
 "label": "Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful human control over autonomous systems: A philosophical account. Frontiers in Robotics and AI, 5, 15.",
 "url": "https://doi.org/10.3389/frobt.2018.00015",
 "type": "Academic (peer-reviewed)",
 },
 "shandler_2026": {
 "label": "Shandler, R., Gross, M. L., & Shereshevsky, Y. (2026). Black box warfare: Human judgment and military decision-making in the age of AI. Journal of Conflict Resolution.",
 "url": "https://journals.sagepub.com/doi/10.1177/00220027261463443",
 "type": "Academic (peer-reviewed)",
 },
 "abraham_2024": {
 "label": "Abraham, Y. (2024, April 3). \u2018Lavender\u2019: The AI machine directing Israel\u2019s bombing spree in Gaza. +972 Magazine.",
 "url": "https://www.972mag.com/lavender-ai-israeli-army-gaza/",
 "type": "News (investigative)",
 },
 "campolo_crawford_2020": {
 "label": "Campolo, A., & Crawford, K. (2020). Enchanted determinism: Power without responsibility in artificial intelligence. Engaging Science, Technology, and Society, 6, 1\u201319.",
 "url": "https://doi.org/10.17351/ests2020.277",
 "type": "Academic (course pack, Session 1)",
 },
 "un_resolution_79_62": {
 "label": "United Nations. (2024, December 2). General Assembly resolution 79/62: Lethal autonomous weapons systems.",
 "url": "https://documents.un.org/doc/undoc/gen/n24/391/35/pdf/n2439135.pdf",
 "type": "Primary source (UN document)",
 },
 "un_news_2026": {
 "label": "United Nations News. (2026, August 25). UN chief, Red Cross renew call for rules on lethal autonomous weapons.",
 "url": "https://news.un.org/en/story/2026/08/1168196",
 "type": "News",
 },
}

# ---------------------------------------------------------------------------
# TIMELINE - dated, factual events only. Each entry cites a source id.
# ---------------------------------------------------------------------------
TIMELINE = [
 {"date": "2018-04", "actor": "Google", "event": "3,000+ Google employees petition Sundar Pichai to withdraw from Project Maven.", "src": None},
 {"date": "2018-06", "actor": "Google", "event": "Google does not renew Project Maven contract; publishes AI Principles listing weapons and surveillance as applications it will not pursue.", "src": None},
 {"date": "2020-01", "actor": "Palantir", "event": "Palantir builds the Maven Smart System for the US military, consolidating multiple intelligence streams into one targeting platform.", "src": "csis_maven"},
 {"date": "2023-01", "actor": "Google", "event": "Project Nimbus (Israel cloud contract) prompts internal employee protest; dismissals follow.", "src": None},
 {"date": "2024-04", "actor": "DoD", "event": "+972 Magazine and Local Call report on Israel's Lavender AI-targeting system; officers describe spending roughly twenty seconds per target, serving largely as a 'stamp of approval', against a system with a reported ten per cent error rate.", "src": "abraham_2024"},
 {"date": "2024-07", "actor": "Anthropic", "event": "Palantir announces partnership to embed Anthropic's Claude into US government intelligence and defense operations, deployed via AWS's classified infrastructure.", "src": "conversation_anthropic"},
 {"date": "2024-08", "actor": "Palantir", "event": "Palantir and Microsoft announce a partnership to deliver Foundry, Gotham, Apollo, and AI Platform on Azure Government for classified and top-secret networks.", "src": "afsc_ecosystem"},
 {"date": "2024-12", "actor": "UN", "event": "UN General Assembly adopts Resolution 79/62 on lethal autonomous weapons systems by a vote of 166 to 3, placing the issue formally on the agenda.", "src": "un_resolution_79_62"},
 {"date": "2025-02", "actor": "Google", "event": "Google removes the 2018 prohibition list from its AI Principles; Hassabis and Manyika cite global AI competition.", "src": "cnbc_google2025"},
 {"date": "2025-02", "actor": "Google", "event": "Senator Ed Markey sends formal letter of concern to Google over the AI Principles revision.", "src": "markey_letter"},
 {"date": "2025-02", "actor": "Palantir", "event": "Karp and Zamiska publish 'The Technological Republic.'", "src": "karp_book"},
 {"date": "2025-07", "actor": "DoD", "event": "DoD's Chief Digital and AI Office awards parallel $200M contracts to Google, OpenAI, Anthropic, and xAI, each integrating frontier models into classified and unclassified defense systems.", "src": "defensefinance_dod4"},
 {"date": "2025-10", "actor": "Palantir", "event": "Palantir and NVIDIA announce a partnership integrating NVIDIA's AI stack directly into Palantir Foundry and AI Platform.", "src": "nvidia_palantir"},
 {"date": "2026-01", "actor": "Anthropic", "event": "Claude, deployed via Palantir's Maven Smart System, reportedly supports mission planning in the US operation that captures former Venezuelan president Nicolas Maduro.", "src": "semafor_rift"},
 {"date": "2026-02", "actor": "Anthropic", "event": "Defense Secretary Hegseth gives Anthropic an ultimatum for unrestricted access; Anthropic refuses.", "src": "semafor_rift"},
 {"date": "2026-02", "actor": "Anthropic", "event": "The DoD designates Anthropic a 'supply chain risk'; Trump orders all federal agencies to phase out Anthropic products within six months.", "src": "cnbc_blacklist"},
 {"date": "2026-02", "actor": "DoD", "event": "The Claude-Maven system, per Washington Post reporting, is used to prioritize roughly 1,000 targets in the opening 24 hours of coordinated US-Israel strikes on Iranian sites.", "src": "defensenews_iran"},
 {"date": "2026-03", "actor": "Anthropic", "event": "Anthropic files two federal lawsuits against the DoD and Hegseth alleging illegal retaliation.", "src": "npr_anthropic"},
 {"date": "2026-03", "actor": "Palantir", "event": "Reuters reports Palantir's Maven Smart System must remove Claude and rebuild affected workflows, a process expected to take months and touch over $1B in contracts.", "src": "yahoo_palantir_challenge"},
 {"date": "2026-03", "actor": "OpenAI", "event": "OpenAI moves quickly to fill the gap left by Anthropic, becoming a primary AI supplier to federal agencies including parts of the State Department (StateChat) and DoD.", "src": "aimagazine_replace"},
 {"date": "2026-03", "actor": "Palantir", "event": "Karp states publicly that Palantir's products, integrated with Anthropic, will 'probably' also integrate with other large language models going forward.", "src": "bloomberg_palantir_shop"},
 {"date": "2026-03", "actor": "Anthropic", "event": "Court filings reveal the DoD privately told Anthropic the two sides were 'nearly aligned' a week before Trump publicly declared the relationship over.", "src": "techcrunch_filing"},
 {"date": "2026-04", "actor": "Palantir", "event": "Palantir's official account publishes a 22-point manifesto thread distilling 'The Technological Republic'; goes viral and draws 'technofascism' criticism.", "src": "engadget_manifesto"},
 {"date": "2026-05", "actor": "Anthropic", "event": "A federal judge rules the DoD illegally retaliated against Anthropic over its AI-safety guardrails.", "src": "cnbc_court"},
 {"date": "2026-05", "actor": "Anthropic", "event": "The DoD awards AI-integration contracts to eight other major firms (Meta, Google, OpenAI, Microsoft, Amazon, NVIDIA, SpaceX, Oracle); Anthropic is the sole exclusion.", "src": "cnbc_court"},
 {"date": "2026-08", "actor": "UN", "event": "Guterres's end-2026 deadline for a binding treaty on lethal autonomous weapons lapses with no treaty concluded; Guterres and ICRC President Mirjana Spoljaric jointly warn states are 'dangerously close to crossing a moral red line.'", "src": "un_news_2026"},
]

# ---------------------------------------------------------------------------
# PALANTIR MANIFESTO - all 22 points, verbatim (primary source), with our
# separate, clearly-labeled interpretive gloss.
# ---------------------------------------------------------------------------
MANIFESTO_POINTS = [
 (1, "Silicon Valley owes a moral debt to the country that made its rise possible.", "The engineering elite has an affirmative obligation to participate in the defense of the nation.", "Sovereignty / obligation"),
 (2, "We must rebel against the tyranny of the apps.", "Is the iPhone our greatest creative achievement, or now a constraint on our sense of the possible?", "Cultural critique"),
 (3, "Free email is not enough.", "A culture's decadence is forgiven only if it delivers economic growth and security for the public.", "Legitimacy / performance"),
 (4, "The limits of soft power have been exposed.", "Free societies require hard power, and hard power this century will be built on software.", "Maintenance narrative (core)"),
 (5, "The question is not whether A.I. weapons will be built; it is who will build them.", "Adversaries will not pause for theatrical debates - they will proceed.", "Maintenance narrative (core)"),
 (6, "National service should be a universal duty.", "Society should consider moving away from an all-volunteer force.", "Militarization of civic life"),
 (7, "If a US Marine asks for a better rifle, we should build it - and the same for software.", "Debate the appropriateness of military action; remain unflinching in support of those who serve.", "Maintenance narrative"),
 (8, "Public servants need not be our priests.", "No business compensating like the federal government would survive.", "Institutional critique"),
 (9, "We should show far more grace towards those in public life.", "Eradicating space for forgiveness may leave us with leaders we come to regret.", "Institutional critique"),
 (10, "The psychologization of modern politics is leading us astray.", "Those seeking meaning in distant political figures will be disappointed.", "Cultural critique"),
 (11, "Society has grown too eager to hasten, and gleeful at, the demise of its enemies.", "Vanquishing an opponent is a moment to pause, not rejoice.", "Cultural critique"),
 (12, "The atomic age is ending.", "A new era of deterrence built on AI is set to begin.", "Maintenance narrative (core)"),
 (13, "No other country has advanced progressive values more than this one.", "The US offers more opportunity for non-hereditary elites than any nation on the planet.", "American exceptionalism"),
 (14, "American power has made possible an extraordinarily long peace.", "Nearly a century without great-power conflict, now taken for granted.", "Maintenance narrative"),
 (15, "The postwar neutering of Germany and Japan must be undone.", "An overcorrection Europe is now paying for; a similar commitment in Japan threatens Asia's balance of power.", "Contested - reverses 1945 pacifist settlement"),
 (16, "We should applaud those who build where the market has failed to act.", "Curiosity about Musk's grand narrative is dismissed with thinly veiled scorn.", "Techno-optimism"),
 (17, "Silicon Valley must play a role in addressing violent crime.", "Politicians have shrugged at violent crime; tech should experiment with solutions.", "Domestic surveillance implication"),
 (18, "Ruthless exposure of public figures' private lives drives talent away from government.", "The republic is left with ineffectual vessels whose ambition would be forgiven if belief lurked within.", "Institutional critique"),
 (19, "The caution we encourage in public life is corrosive.", "Those who say nothing wrong often say nothing at all.", "Cultural critique"),
 (20, "The pervasive intolerance of religious belief must be resisted.", "Elite intolerance of religion signals a less open intellectual movement than claimed.", "Culture-war framing"),
 (21, "Some cultures have produced vital advances; others remain dysfunctional and regressive.", "Criticism and value judgments are not forbidden - cultures are not all equal.", "Contested - echoes civilizational-hierarchy tropes"),
 (22, "We must resist the shallow temptation of a vacant and hollow pluralism.", "Fifty years of resisting defining national culture in the name of inclusivity - but inclusion into what?", "Culture-war framing"),
]

# ---------------------------------------------------------------------------
# NODE MAP - factual relationships only (partnerships, contracts, disputes).
# Each edge cites a source. Expanded per AFSC's "Palantir's Tech Ecosystem"
# (Apr 2026) and current defense-tech reporting on the Anthropic-DoD dispute.
# ---------------------------------------------------------------------------
NODES = [
 "Palantir", "Google", "Anthropic", "OpenAI", "Microsoft", "NVIDIA", "Amazon (AWS)",
 "U.S. DoD", "Israel (IDF)", "ICE / DHS", "UK NHS",
]

# (source, target, label, kind, source_id)
# kind values used for edge styling: partnership | contract | contract+dispute |
# contract (ended/replaced) | contract (contested) | infrastructure
EDGES = [
 ("Anthropic", "Palantir", "Claude integrated into Palantir's AI Platform (Nov 2024 partnership with AWS); powers Maven Smart System workflows", "partnership (disrupted)", "afsc_ecosystem"),
 ("Anthropic", "Amazon (AWS)", "Claude available on AWS's classified Top Secret Cloud", "infrastructure", "semafor_rift"),
 ("Palantir", "Amazon (AWS)", "Palantir Foundry integrated with AWS SageMaker; relies on AWS for cloud operations", "infrastructure", "afsc_ecosystem"),
 ("Palantir", "Microsoft", "Foundry, Gotham, Apollo, and AI Platform deployed on Azure Government for classified/top-secret networks (Aug 2024)", "partnership", "afsc_ecosystem"),
 ("Palantir", "NVIDIA", "NVIDIA's AI stack directly integrated into Palantir Foundry and AI Platform (Oct 2025)", "partnership", "nvidia_palantir"),
 ("Palantir", "Google", "Palantir Foundry integrated with BigQuery, Vertex AI, and Google Kubernetes Engine; Gemini supported as an AI Platform model", "partnership", "afsc_ecosystem"),
 ("Palantir", "U.S. DoD", "Maven Smart System (built 2020) fuses intelligence streams for targeting; contracts worth over $1B", "contract", "csis_maven"),
 ("Anthropic", "U.S. DoD", "$200M contract (Jul 2025) with acceptable-use limits; DoD designates Anthropic a 'supply chain risk' (Feb 2026); litigation ongoing, Anthropic won May 2026 ruling", "contract+dispute", "cnbc_blacklist"),
 ("Google", "U.S. DoD", "Project Maven (2017-18, ended under employee pressure); parallel $200M contract awarded Jul 2025; AI Principles revised 2025 to permit broader engagement", "contract (past+present)", "defensefinance_dod4"),
 ("OpenAI", "U.S. DoD", "Parallel $200M contract (Jul 2025); moved quickly to replace Anthropic across federal agencies after Feb 2026 blacklist, including State Department's StateChat", "contract (expanded)", "aimagazine_replace"),
 ("OpenAI", "Palantir", "Palantir's Maven Smart System is model-agnostic; explored as a Claude replacement after Feb 2026 DoD order", "partnership (emerging)", "yahoo_palantir_challenge"),
 ("Palantir", "Israel (IDF)", "AI-based targeting and intelligence analysis contracts, renewed 2024", "contract", None),
 ("Palantir", "ICE / DHS", "'ImmigrationOS' contract (approx. $30M, no-bid)", "contract", None),
 ("Palantir", "UK NHS", "Patient-data platform contract; subject of a 200,000+ signature petition", "contract (contested)", None),
 ("Google", "Israel (IDF)", "Project Nimbus, cloud/AI contract (2023, ongoing)", "contract", None),
]

# ---------------------------------------------------------------------------
# COMPANY PROFILES - key facts + quotes + our interpretive frame (labeled)
# ---------------------------------------------------------------------------
PROFILES = {
 "Palantir": {
 "narrative": "Maintenance, stated as ideology",
 "color": RUST,
 "summary": "Palantir has built its public identity around the claim that Silicon Valley has an affirmative duty to arm the state, treating the militarisation of AI as historically inevitable rather than a contested choice.",
 "key_quote": ("The question is not whether A.I. weapons will be built; it is who will build them and for what purpose.", "Palantir, \u2018The Technological Republic,\u2019 Point 5"),
 "facts": [
 ("2020", "Builds the Maven Smart System, consolidating multiple intelligence streams into a single targeting-recommendation platform."),
 ("2024", "Partners with Anthropic (Nov), Microsoft (Aug), and expands ties with Google Cloud, AWS, and NVIDIA - a model-agnostic ecosystem by design."),
 ("Feb 2025", "Karp and Zamiska publish 'The Technological Republic.'"),
 ("Mar 2026", "Forced to rebuild Maven workflows after the DoD orders Claude removed; Karp states products will 'probably' integrate other LLMs going forward."),
 ("Apr 2026", "22-point manifesto thread goes viral; draws 'technofascism' criticism from commentators."),
 ],
 "our_reading": "Read through Feenberg's Substantivism, Palantir's manifesto doesn't just describe a trajectory, it recommends one, redescribing a contested political choice as inevitability. Its model-agnostic infrastructure (Anthropic, Google, NVIDIA, and reportedly OpenAI) meant the Anthropic-DoD dispute barely touched Palantir's own position - it simply swapped suppliers, which is itself a demonstration of how little leverage any single AI firm's ethical line carries against integrator platforms built for exactly this contingency.",
 },
 "Google": {
 "narrative": "Disengagement (2018) \u2192 Maintenance (2025)",
 "color": GOLD,
 "summary": "Google's own employees successfully redirected the company away from military AI in 2018 - and the company reversed that redirection under competitive pressure seven years later, in language echoing arguments its own leadership made in 2018.",
 "key_quote": ("There's a global competition taking place for AI leadership within an increasingly complex geopolitical landscape. We believe democracies should lead in AI development.", "Demis Hassabis & James Manyika, Feb 2025"),
 "facts": [
 ("Apr 2018", "3,000+ employees petition Pichai to withdraw from Project Maven."),
 ("Jun 2018", "Google does not renew Maven; publishes AI Principles barring weapons & surveillance."),
 ("2023", "Project Nimbus (Israel) prompts internal protest and dismissals."),
 ("Feb 2025", "Removes the 2018 prohibition list; Senator Markey sends formal objection."),
 ],
 "our_reading": "Demis Hassabis signed a 2015 open letter calling for a ban on autonomous weapons, and reportedly secured a commitment on DeepMind's acquisition against military use. He co-authored the 2025 post removing Google's version of that commitment - evidence about institutional pressure, not personal inconsistency.",
 },
 "Anthropic": {
 "narrative": "Ambivalence - a conditional line",
 "color": SAGE,
 "summary": "Anthropic drew the most restrictive public line of the three and defended it in court, at real commercial cost - while its models remained embedded, through Palantir, in the targeting infrastructure the wider debate concerns, reportedly including a live strike campaign.",
 "key_quote": ("We didn't really feel that with rapid advance of AI, that it makes sense for us to make unilateral commitments... if competitors are blazing ahead.", "Jared Kaplan, Chief Science Officer, Anthropic"),
 "facts": [
 ("Nov 2024", "Claude integrated into Palantir's AI Platform via a partnership with AWS, reaching classified environments."),
 ("Jul 2025", "Signs $200M DoD contract with limits on mass surveillance and fully autonomous weapons."),
 ("Jan 2026", "Claude, via Palantir's Maven system, reportedly supports the operation that captures Nicolas Maduro."),
 ("Feb 2026", "Designated 'supply chain risk' after refusing to remove limits; Claude reportedly used in prioritizing Iran strike targets the same month."),
 ("Mar 2026", "Sues the DoD; Palantir must rebuild Maven workflows to remove Claude; OpenAI moves to fill the gap across federal agencies."),
 ("May 2026", "Wins federal court ruling against DoD retaliation; excluded from a subsequent 8-company contract round."),
 ],
 "our_reading": "Kaplan's own words, that unilateral commitments don't make sense if competitors are 'blazing ahead,' make the ambivalence narrative explicit rather than something inferred from outside. The subsequent Iran-strike reporting, if accurate, means Anthropic's models were reportedly implicated in live targeting decisions during the very period it was publicly defending its human-in-the-loop principle in court - the sharpest version of the tension this essay identifies.",
 },
}
