# llm-medicaid-eligibility
Using large language models to create user-friendly applications for Medicaid eligibility determination

## Getting Started

This project was developed with Python 3.11.6. 

```sh
git clone git@github.com:navhealth/llm-medicaid-eligibility.git
cd llm-medicaid-eligibility
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip wheel setuptools
python3 -m pip install -r requirements.txt
cat > .env <<EOF
OPENAI_API_TYPE=azure
OPENAI_API_BASE=https://carejourney.openai.azure.com
OPENAI_API_KEY=alphanumeric0api0key
OPENAI_API_VERSION=2023-05-15
EOF
python3 html_to_text_to_python_combine.py # or html_to_text_combine_to_python.py
```
