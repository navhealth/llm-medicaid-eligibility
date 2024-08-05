from llm_medicaid_eligibility.core.html_to_text_to_python import url_to_python
from llm_medicaid_eligibility.nd.html_extractor import html_extractor


if __name__ == "__main__":
    print(
        url_to_python(
            state="North Dakota Department of Health and Human Services",
            url="https://www.hhs.nd.gov/healthcare/medicaid/eligibility",
            html_extractor=html_extractor,
        )
    )
