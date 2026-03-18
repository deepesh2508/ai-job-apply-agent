from config import USER_PROFILE

def get_rule_based_answer(question):
    q = question.lower()

    if "phone" in q:
        return USER_PROFILE["basic"]["phone"]

    if "email" in q:
        return USER_PROFILE["basic"]["email"]

    if "notice" in q:
        return USER_PROFILE["basic"]["notice_period"]

    if "authorized" in q:
        return "Yes"

    if "experience" in q:
        return USER_PROFILE["summary"]

    if "skills" in q:
        return ", ".join(USER_PROFILE["skills"]["languages"])

    return None