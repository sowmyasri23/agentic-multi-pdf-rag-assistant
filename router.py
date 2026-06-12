def route_query(query):

    query = query.lower()

    if (
        "resume" in query
        and (
            "analyze" in query
            or "analyse" in query
            or "review" in query
            or "ats" in query
        )
    ):
        return "resume"

    elif (
        "interview" in query
        or "mock interview" in query
        or "interview questions" in query
    ):
        return "interview"

    elif (
        "job" in query
        or "jd" in query
        or "match" in query
        or "job description" in query
    ):
        return "job_match"

    elif (
        "quiz" in query
        or "mcq" in query
        or "questions" in query
        or "test me" in query
    ):
        return "quiz"

    elif (
        "flashcard" in query
        or "flashcards" in query
        or "study cards" in query
    ):
        return "flashcards"
    elif (
        "skill gap" in query
        or "missing skills" in query
        or "skill analysis" in query
    ):
        return "skill_gap"
    elif (
       "roadmap" in query
       or "learning plan" in query
       or "career path" in query
    ):
       return "roadmap"

    else:
        return "chat"