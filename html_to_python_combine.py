if __name__ == "__main__":
    from utils import create_llm

    llm = create_llm()

    category_urls = [
        "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/individual-adults",
        "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/parents-and-caretakers",
        "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/pregnant-individuals",
        # "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/children",
        # "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/noncitizens",
        "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/aged-blind-or-disabled",
        # "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/age-65-and-older-or-medicare-eligible",
        # "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/foster-care",
        # "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/long-term-care-and-hospice",
        # "https://www.hca.wa.gov/free-or-low-cost-health-care/i-need-medical-dental-or-vision-care/medicare-savings-program",
    ]

    from html_to_python_clean_example import url_to_python

    python_snippets_joined = "\n\n".join(
        url_to_python(url, llm=llm) for url in category_urls
    )

    from langchain_core.chat_history import (
        BaseChatMessageHistory,
        InMemoryChatMessageHistory,
    )
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.runnables.history import RunnableWithMessageHistory

    store = {}

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "The following is a conversation between a human and an AI. The AI is an expert on Medicaid eligibility and is able to write quality Python code. If the AI does not know the answer to a question, it truthfully says it does not know.",
            ),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )
    chain_with_history = RunnableWithMessageHistory(
        prompt | llm,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    prompts = [
        f"""Below are {len(category_urls)} Python code snippets. Combine all the snippets into a single Python program that determines whether the user is eligible for Medicaid. The code should not only executable but should also accurately encode eligibility rules for all programs. The code should incorporate all of the above code snippets. Write the code to determine whether a user is eligible for any of the above Medicaid programs: 

{python_snippets_joined}""",
        "Ensure that the code incorporates all information from the income tables, and not just a single value. Re-write the code: ",
    ]

    for prompt in prompts:
        output = chain_with_history.invoke(
            {"input": prompt}, config={"configurable": {"session_id": "session"}}
        )
        chain_with_history.get_session_history("session").messages[-2].pretty_print()
        output.pretty_print()
