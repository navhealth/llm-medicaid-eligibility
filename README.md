# llm-medicaid-eligibility

Source code for "A methodology for using large language models to create user-friendly applications for Medicaid redetermination and other social services" (Ratna et al., 2024)

## Getting Started

This project was developed with Python 3.12.4. 

```sh
git clone git@github.com:navhealth/llm-medicaid-eligibility.git
cd llm-medicaid-eligibility
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
cat > .env <<EOF
OPENAI_API_KEY=sk-proj-1234567890abcdefghijklmnopqrstuvwxABCDEFGHIJKLMN
EOF
python3 -m llm_medicaid_eligibility.nd.html_to_text_to_python
python3 -m llm_medicaid_eligibility.sc.html_to_text_to_python
python3 -m llm_medicaid_eligibility.wa.html_to_text_combine_to_python
python3 -m llm_medicaid_eligibility.wa.html_to_text_to_python_combine
```

## Disclaimer

The contents of this GitHub public repository are provided for informational and educational purposes only. The repository owners make no warranties, express or implied, regarding the accuracy, reliability, or completeness of any code, documentation, or other materials contained within this repository.

Users of this repository are solely responsible for their own actions and the manner in which they utilize the information and code provided. It is important to exercise caution and use the contents of this repository responsibly and in compliance with applicable laws and regulations.

The repository owners shall not be held accountable for any misuse, damage, or consequences arising from the use or misuse of any code, information, or materials contained within this repository. Users are encouraged to thoroughly review and understand the code before implementing it in their own projects or systems.

By accessing and using this repository, users acknowledge and agree to hold the repository owners harmless from any liability, loss, or damage incurred as a result of the use or misuse of the contents herein.

Please note that this disclaimer applies to the repository as a whole and all its contents, including but not limited to code, documentation, and any accompanying materials.

If you do not agree with these terms, please refrain from using this repository.
 
## Reference

If you find our work useful in your research or if you use parts of this code please consider citing our [paper](https://doi.org/10.3389/ijph.2024.1607317):

Ratna, S., Weeks, W. B., Ferres, J. L., Chopra, A., & Pereira, M. (2024). A methodology for using large language models to create user-friendly applications for Medicaid redetermination and other social services. _International Journal of Public Health_, _69_, 1607317. https://doi.org/10.3389/ijph.2024.1607317

```
@ARTICLE{10.3389/ijph.2024.1607317,
    AUTHOR={Ratna, Sumanth  and Weeks, William B.  and Ferres, Juan Lavista  and Chopra, Aneesh  and Pereira, Mayana },
    TITLE={A Methodology for Using Large Language Models to Create User-Friendly Applications for Medicaid Redetermination and Other Social Services},
    JOURNAL={International Journal of Public Health},
    VOLUME={69},
    YEAR={2024},
    URL={https://www.ssph-journal.org/journals/international-journal-of-public-health/articles/10.3389/ijph.2024.1607317},
    DOI={10.3389/ijph.2024.1607317},
    ISSN={1661-8564},
}
```
