"""
data.py — Single source of truth for all content on the site.
Every factual claim here traces to a source in SOURCES. Interpretive/
analytical content (narrative placement, our commentary) is kept in
separate fields and labeled as such in the UI — never mixed silently
with sourced facts.
"""

# ---------------------------------------------------------------------------
# COLOR SCHEME — muted defense/policy-brief palette (matches the essay doc)
# ---------------------------------------------------------------------------
INK = "#1C2126"
PAPER = "#F7F5F0"
PAPER_DARK = "#EFEBE1"
RUST = "#B5462E"
GOLD = "#8A6D22"
STEEL = "#4B5A64"
SAGE = "#6E7F63"
GREY = "#5B5B5B"
LINE = "#C9C2B4"

COMPANY_COLOR = {
    "Palantir": RUST,
    "Google": GOLD,
    "Anthropic": SAGE,
    "DoD": STEEL,
}

# ---------------------------------------------------------------------------
# SOURCES — every citation used anywhere on the site, keyed by short id
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
}

# ---------------------------------------------------------------------------
# TIMELINE — dated, factual events only. Each entry cites a source id.
# ---------------------------------------------------------------------------
TIMELINE = [
    {"date": "2018-04", "actor": "Google", "event": "3,000+ Google employees petition Sundar Pichai to withdraw from Project Maven.", "src": None},
    {"date": "2018-06", "actor": "Google", "event": "Google does not renew Project Maven contract; publishes AI Principles listing weapons & surveillance as \u2018applications we will not pursue.\u2019", "src": None},
    {"date": "2020-01", "actor": "Palantir", "event": "Palantir builds the Maven Smart System for the US military, consolidating 8-9 intelligence streams.", "src": None},
    {"date": "2023-01", "actor": "Google", "event": "Project Nimbus (Israel cloud contract) prompts internal employee protest; dismissals follow.", "src": None},
    {"date": "2024-07", "actor": "Anthropic", "event": "Palantir announces partnership to embed Anthropic's Claude into US government intelligence & defense operations.", "src": "conversation_anthropic"},
    {"date": "2025-02", "actor": "Google", "event": "Google removes the 2018 prohibition list from its AI Principles; Hassabis & Manyika cite global AI competition.", "src": "cnbc_google2025"},
    {"date": "2025-02", "actor": "Google", "event": "Senator Ed Markey sends formal letter of concern to Google over the AI Principles revision.", "src": "markey_letter"},
    {"date": "2025-02", "actor": "Palantir", "event": "Karp & Zamiska publish \u2018The Technological Republic.\u2019", "src": "karp_book"},
    {"date": "2025-07", "actor": "Anthropic", "event": "Anthropic signs $200M DoD contract with acceptable-use limits (no mass surveillance, no fully autonomous lethal weapons).", "src": "npr_anthropic"},
    {"date": "2026-02", "actor": "Anthropic", "event": "Defense Secretary Hegseth gives Anthropic ultimatum; DoD designates Anthropic a \u2018supply chain risk.\u2019", "src": "npr_anthropic"},
    {"date": "2026-03", "actor": "Anthropic", "event": "Anthropic files two federal lawsuits against DoD/Hegseth alleging illegal retaliation.", "src": "npr_anthropic"},
    {"date": "2026-03", "actor": "Anthropic", "event": "Court filings reveal DoD told Anthropic the two sides were \u2018nearly aligned\u2019 a week before Trump declared the relationship over.", "src": "techcrunch_filing"},
    {"date": "2026-04", "actor": "Palantir", "event": "Palantir's official account publishes a 22-point manifesto thread distilling \u2018The Technological Republic\u2019; goes viral, draws \u2018technofascism\u2019 criticism.", "src": "engadget_manifesto"},
    {"date": "2026-05", "actor": "Anthropic", "event": "Federal judge rules DoD illegally retaliated against Anthropic.", "src": "cnbc_court"},
    {"date": "2026-05", "actor": "Anthropic", "event": "DoD awards AI-integration contracts to 8 other major firms (Meta, Google, OpenAI, Microsoft, Amazon, Nvidia, SpaceX, Oracle); Anthropic the sole exclusion.", "src": "cnbc_court"},
]

# ---------------------------------------------------------------------------
# PALANTIR MANIFESTO — all 22 points, verbatim (primary source), with our
# separate, clearly-labeled interpretive gloss.
# ---------------------------------------------------------------------------
MANIFESTO_POINTS = [
    (1, "Silicon Valley owes a moral debt to the country that made its rise possible.", "The engineering elite has an affirmative obligation to participate in the defense of the nation.", "Sovereignty / obligation"),
    (2, "We must rebel against the tyranny of the apps.", "Is the iPhone our greatest creative achievement, or now a constraint on our sense of the possible?", "Cultural critique"),
    (3, "Free email is not enough.", "A culture's decadence is forgiven only if it delivers economic growth and security for the public.", "Legitimacy / performance"),
    (4, "The limits of soft power have been exposed.", "Free societies require hard power, and hard power this century will be built on software.", "Maintenance narrative (core)"),
    (5, "The question is not whether A.I. weapons will be built; it is who will build them.", "Adversaries will not pause for theatrical debates \u2014 they will proceed.", "Maintenance narrative (core)"),
    (6, "National service should be a universal duty.", "Society should consider moving away from an all-volunteer force.", "Militarization of civic life"),
    (7, "If a US Marine asks for a better rifle, we should build it \u2014 and the same for software.", "Debate the appropriateness of military action; remain unflinching in support of those who serve.", "Maintenance narrative"),
    (8, "Public servants need not be our priests.", "No business compensating like the federal government would survive.", "Institutional critique"),
    (9, "We should show far more grace towards those in public life.", "Eradicating space for forgiveness may leave us with leaders we come to regret.", "Institutional critique"),
    (10, "The psychologization of modern politics is leading us astray.", "Those seeking meaning in distant political figures will be disappointed.", "Cultural critique"),
    (11, "Society has grown too eager to hasten, and gleeful at, the demise of its enemies.", "Vanquishing an opponent is a moment to pause, not rejoice.", "Cultural critique"),
    (12, "The atomic age is ending.", "A new era of deterrence built on AI is set to begin.", "Maintenance narrative (core)"),
    (13, "No other country has advanced progressive values more than this one.", "The US offers more opportunity for non-hereditary elites than any nation on the planet.", "American exceptionalism"),
    (14, "American power has made possible an extraordinarily long peace.", "Nearly a century without great-power conflict, now taken for granted.", "Maintenance narrative"),
    (15, "The postwar neutering of Germany and Japan must be undone.", "An overcorrection Europe is now paying for; a similar commitment in Japan threatens Asia's balance of power.", "Contested \u2014 reverses 1945 pacifist settlement"),
    (16, "We should applaud those who build where the market has failed to act.", "Curiosity about Musk's grand narrative is dismissed with thinly veiled scorn.", "Techno-optimism"),
    (17, "Silicon Valley must play a role in addressing violent crime.", "Politicians have shrugged at violent crime; tech should experiment with solutions.", "Domestic surveillance implication"),
    (18, "Ruthless exposure of public figures' private lives drives talent away from government.", "The republic is left with ineffectual vessels whose ambition would be forgiven if belief lurked within.", "Institutional critique"),
    (19, "The caution we encourage in public life is corrosive.", "Those who say nothing wrong often say nothing at all.", "Cultural critique"),
    (20, "The pervasive intolerance of religious belief must be resisted.", "Elite intolerance of religion signals a less open intellectual movement than claimed.", "Culture-war framing"),
    (21, "Some cultures have produced vital advances; others remain dysfunctional and regressive.", "Criticism and value judgments are not forbidden \u2014 cultures are not all equal.", "Contested \u2014 echoes civilizational-hierarchy tropes"),
    (22, "We must resist the shallow temptation of a vacant and hollow pluralism.", "Fifty years of resisting defining national culture in the name of inclusivity \u2014 but inclusion into what?", "Culture-war framing"),
]

# ---------------------------------------------------------------------------
# NODE MAP — factual relationships only (partnerships, contracts, disputes).
# Each edge cites a source.
# ---------------------------------------------------------------------------
NODES = ["Palantir", "Google", "Anthropic", "U.S. DoD", "Israel (IDF)", "ICE / DHS", "UK NHS"]

EDGES = [
    ("Anthropic", "Palantir", "Claude embedded in Palantir's defense/intel stack", "partnership", "conversation_anthropic"),
    ("Palantir", "U.S. DoD", "Maven Smart System (2020) \u2014 intelligence fusion & targeting", "contract", None),
    ("Anthropic", "U.S. DoD", "$200M contract (Jul 2025); later designated \u2018supply chain risk\u2019; litigation ongoing", "contract+dispute", "npr_anthropic"),
    ("Google", "U.S. DoD", "Project Maven (2017\u201318, ended); AI Principles revised 2025 to permit broader engagement", "contract (past+present)", "cnbc_google2025"),
    ("Palantir", "Israel (IDF)", "AI-based targeting & intelligence analysis contracts, renewed 2024", "contract", None),
    ("Palantir", "ICE / DHS", "\u2018ImmigrationOS\u2019 contract (~$30M, no-bid)", "contract", None),
    ("Palantir", "UK NHS", "Patient-data platform contract \u2014 subject of 200,000+ signature petition", "contract (contested)", None),
    ("Google", "Israel (IDF)", "Project Nimbus \u2014 cloud/AI contract (2023, ongoing)", "contract", None),
]

# ---------------------------------------------------------------------------
# COMPANY PROFILES — key facts + quotes + our interpretive frame (labeled)
# ---------------------------------------------------------------------------
PROFILES = {
    "Palantir": {
        "narrative": "Maintenance, stated as ideology",
        "color": RUST,
        "summary": "Palantir has built its public identity around the claim that Silicon Valley has an affirmative duty to arm the state, treating the militarisation of AI as historically inevitable rather than a contested choice.",
        "key_quote": ("The question is not whether A.I. weapons will be built; it is who will build them and for what purpose.", "Palantir, \u2018The Technological Republic,\u2019 Point 5"),
        "facts": [
            ("2020", "Builds the Maven Smart System, consolidating 9 intelligence streams into a single targeting-recommendation platform."),
            ("2024", "Partners with Anthropic to embed Claude in its defense/intelligence stack."),
            ("Feb 2025", "Karp & Zamiska publish 'The Technological Republic.'"),
            ("Apr 2026", "22-point manifesto thread goes viral; draws 'technofascism' criticism from commentators."),
        ],
        "our_reading": "Read through Feenberg's Substantivism, Palantir's manifesto doesn't just describe a trajectory \u2014 it recommends one, redescribing a contested political choice as inevitability. This is precisely the move Floridi's double-charge thesis is built to expose.",
    },
    "Google": {
        "narrative": "Disengagement (2018) \u2192 Maintenance (2025)",
        "color": GOLD,
        "summary": "Google's own employees successfully redirected the company away from military AI in 2018 \u2014 and the company reversed that redirection under competitive pressure seven years later, in language echoing arguments its own leadership made in 2018.",
        "key_quote": ("There's a global competition taking place for AI leadership within an increasingly complex geopolitical landscape. We believe democracies should lead in AI development.", "Demis Hassabis & James Manyika, Feb 2025"),
        "facts": [
            ("Apr 2018", "3,000+ employees petition Pichai to withdraw from Project Maven."),
            ("Jun 2018", "Google does not renew Maven; publishes AI Principles barring weapons & surveillance."),
            ("2023", "Project Nimbus (Israel) prompts internal protest and dismissals."),
            ("Feb 2025", "Removes the 2018 prohibition list; Senator Markey sends formal objection."),
        ],
        "our_reading": "Demis Hassabis signed a 2015 open letter calling for a ban on autonomous weapons, and reportedly secured a commitment on DeepMind's acquisition against military use. He co-authored the 2025 post removing Google's version of that commitment \u2014 evidence about institutional pressure, not personal inconsistency.",
    },
    "Anthropic": {
        "narrative": "Ambivalence \u2014 a conditional line",
        "color": SAGE,
        "summary": "Anthropic has drawn the most restrictive public line of the three and defended it in court \u2014 while remaining commercially entangled, through Palantir, with the very targeting infrastructure the wider debate concerns.",
        "key_quote": ("We didn't really feel that with rapid advance of AI, that it makes sense for us to make unilateral commitments... if competitors are blazing ahead.", "Jared Kaplan, Chief Science Officer, Anthropic"),
        "facts": [
            ("Jul 2024", "Claude embedded in Palantir's Maven Smart System via partnership."),
            ("Jul 2025", "Signs $200M DoD contract with limits on surveillance & full autonomy."),
            ("Feb 2026", "Designated 'supply chain risk' after refusing to remove limits."),
            ("May 2026", "Wins federal court ruling against DoD retaliation; excluded from a subsequent 8-company contract round."),
        ],
        "our_reading": "Kaplan's own words \u2014 that unilateral commitments don't make sense if competitors are 'blazing ahead' \u2014 make the ambivalence narrative explicit rather than something we're merely inferring from outside.",
    },
}
