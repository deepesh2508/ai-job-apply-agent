from utils import get_rule_based_answer
from llm import generate_answer
import time

def fill_form(page):
    labels = page.locator("label").all()

    for label in labels:
        try:
            question = label.inner_text().strip()

            input_box = label.locator("xpath=following::input[1]")
            textarea = label.locator("xpath=following::textarea[1]")

            # Rule-based first
            answer = get_rule_based_answer(question)

            # LLM fallback
            if not answer:
                answer = generate_answer(question)

            # Fill input
            if input_box.count() > 0:
                input_box.first.fill(answer)

            elif textarea.count() > 0:
                textarea.first.fill(answer)

            time.sleep(1)

        except Exception as e:
            print("Error filling field:", e)


def handle_steps(page):
    while True:
        fill_form(page)
        time.sleep(2)

        # Upload resume if required
        if page.locator("input[type='file']").count() > 0:
            page.set_input_files("input[type='file']", "Deepesh_Resume.pdf")

        # Next button
        if page.locator("button:has-text('Next')").is_visible():
            page.click("button:has-text('Next')")
            time.sleep(2)

        else:
            break