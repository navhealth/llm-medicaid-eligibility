from langchain_community.callbacks import get_openai_callback
from llm_medicaid_eligibility.core.html_to_python_clean_example import url_to_python
from llm_medicaid_eligibility.sc.html_extractor import html_extractor


if __name__ == "__main__":
    with get_openai_callback() as cb:
        print(
            url_to_python(
                state="South Carolina Department of Health and Human Services",
                url="https://www.scdhhs.gov/members/program-eligibility-and-income-limits",
                html_extractor=html_extractor,
            )
        )
    print(cb)
