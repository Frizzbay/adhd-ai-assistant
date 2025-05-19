# System prompts and context management

def get_minimal_testing_prompt() -> str:
    """
    Basic system prompt for testing basic functionality.
    Keep this minimal to save on API credits during development.
    """

    return "You are a helpful assistant designed to support people with ADHD"


# TODO: Replace with optimized prompt after basic functionality is confirmed
def get_direct_adhd_prompt() -> str:
    """
    Direct, no-nonsense, ADHD support approach.
    Focus on reality checks, cutting through distractions, and action-oriented responses.
    """
    return get_minimal_testing_prompt()


def get_supportive_adhd_prompt() -> str:
    """
    Gentle, encouraging ADHD support approach.
    Focus on validation, building confidence, and patient guidence.
    """
    return get_minimal_testing_prompt()


def get_structured_adhd_prompt() -> str:
    """
    Highly structured, step-by-step ADHD support approach.
    Focus on breaking things down, clear organization, and systemic approaches
    """
    return get_minimal_testing_prompt()


def get_system_prompt(mode: str = "minimal") -> str:
    """
    Main function to get system prompt based on selected mode.

    Available modes:
    - "minimal": Basic testing prompt (default during development)
    - "direct": Direct, reality-focused, ADHD support
    - "supportive": Gentle, encouraging ADHD support
    - "structured": Highly organised, step-by-step ADHD support
    """
    if mode == "direct":
        return get_direct_adhd_prompt()
    elif mode == "supportive":
        return get_supportive_adhd_prompt()
    elif mode == "structured":
        return get_structured_adhd_prompt()
    else:
        return get_minimal_testing_prompt()

