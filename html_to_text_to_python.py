from utils import create_llm, url_to_html


def url_to_rules(url, llm=None):
    if llm is None:
        llm = create_llm()

    soup = url_to_html(url)

    prompt_html_to_text = f"""
Below is HTML from a Webpage by the Washington state Health Care Authority describing state Medicaid eligibility rules. 

Accurately and precisely extract all of the eligibility rules from the HTML as text. Include all relevant information, such as income charts. 

{soup.body.main if soup.body.find("main") else soup.body}"""
    return llm.invoke(prompt_html_to_text).content


def rules_to_python(rules, llm=None):
    if llm is None:
        llm = create_llm()

    prompt_text_to_python = f"""Below are eligibility rules for Apple Health for Adults (age 19 through 64 years of age). 

Using these eligibility rules, write a Python program that prompts the user for questions, and based on their answers, determines whether they are eligible for Apple Health for Adults (age 19 through 64 years of age).

{rules}"""
    return llm.invoke(prompt_text_to_python).content


def url_to_python(url, llm=None):
    if llm is None:
        llm = create_llm()
    return rules_to_python(url_to_rules(url, llm=llm), llm=llm)


if __name__ == "__main__":
    llm = create_llm()
    print(
        url_to_python(
            "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/individual-adults"
        )
    )
