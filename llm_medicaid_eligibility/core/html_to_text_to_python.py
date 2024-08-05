from llm_medicaid_eligibility.core.utils import create_llm, url_to_html


def url_to_rules(state, url, llm=None, html_extractor=lambda soup: soup.body):
    if llm is None:
        llm = create_llm()

    soup = url_to_html(url)

    prompt_html_to_text = f"""
Below is HTML from a Webpage by the {state} describing state Medicaid eligibility rules. 

Accurately and precisely extract all of the eligibility rules from the HTML as text. Be sure to include all relevant information, such as income charts. 

{html_extractor(soup)}"""
    return llm.invoke(prompt_html_to_text).content


def rules_to_python(rules, llm=None):
    if llm is None:
        llm = create_llm()

    prompt_text_to_python = f"""Below are eligibility rules for a state Medicaid program. 

Using these eligibility rules, write a Python program that asks the user questions and based on their answers, determines whether they are eligible for Medicaid. The program should implement eligibility calculation for all Medicaid programs provided as input, and the program should output which specific Medicaid program the user is eligible for. 

{rules}"""
    return llm.invoke(prompt_text_to_python).content


def url_to_python(state, url, llm=None, html_extractor=lambda soup: soup.body):
    if llm is None:
        llm = create_llm()
    return rules_to_python(
        url_to_rules(state, url, llm=llm, html_extractor=html_extractor),
        llm=llm,
    )
