def create_llm():
    from dotenv import load_dotenv

    load_dotenv()

    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.0,
        top_p=0.5,
    )

    return llm


from urllib.request import urlopen
from bs4 import BeautifulSoup


def url_to_html(url):
    with urlopen(url) as f:
        html = f.read().decode("utf-8")

    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "header", "nav", "footer"]):
        script.decompose()

    return soup
