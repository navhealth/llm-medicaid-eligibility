def create_llm():
    from dotenv import load_dotenv

    load_dotenv()

    from langchain.chat_models import AzureChatOpenAI

    llm = AzureChatOpenAI(
        openai_api_version="2023-05-15",
        deployment_name="gpt-35-turbo",
        model_name="gpt-3.5-turbo",
        model_version="0301",
        temperature=1,
        model_kwargs={"top_p": 0.5},
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
