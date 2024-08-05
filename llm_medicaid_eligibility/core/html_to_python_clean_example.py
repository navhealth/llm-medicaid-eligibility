from llm_medicaid_eligibility.core.utils import create_llm, url_to_html


def url_to_python(state, url, llm=None, html_extractor=lambda soup: soup.body):
    if llm is None:
        llm = create_llm()

    soup = url_to_html(url)

    prompt_html_to_python = f"""Below is HTML from a webpage by the Washington state Health Care Authority describing state Medicaid eligibility rules. 

<div>
  <h2>Program requirements</h2>
  <p>You may be eligible for Apple Health for Pregnant individuals coverage if you:</p>
  <ul>
    <li>Are pregnant.</li>
    <li>Live in Washington State.</li>
    <li>Have income at or below 193% of the Federal Poverty Level (FPL)&nbsp;(see income chart below).*</li>
  </ul>
  <h3>What is the most I can make per month to qualify?</h3>
  <div>
    <table summary="Table outlining the income standards for Apple Health for Pregnant Individuals">
      <thead>
        <tr>
          <th>
            <p>Program**</p>
          </th>
          <th>
            <p>Single<br>
              person
            </p>
          </th>
          <th>
            <p>2-person household</p>
          </th>
          <th>
            <p>3-person household</p>
          </th>
          <th>
            <p>4-person household</p>
          </th>
          <th>
            <p>5-person household</p>
          </th>
          <th>
            <p>6-person household</p>
          </th>
          <th>
            <p>7-person household</p>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>
            <p><strong>Apple<br>
              Health<br>
              for<br>
              Pregnant Individuals</strong>
            </p>
          </th>
          <td>
            <p><strong>n/a</strong></p>
          </td>
          <td>
            <p><strong>$3,254</strong><br>
              monthly
            </p>
          </td>
          <td>
            <p><strong>$4,102</strong><br>
              monthly
            </p>
          </td>
          <td>
            <p><strong>$4,950</strong><br>
              monthly
            </p>
          </td>
          <td>
            <p><strong>$5,799</strong><br>
              monthly
            </p>
          </td>
          <td>
            <p><strong>$6,647</strong><br>
              monthly
            </p>
          </td>
          <td>
            <p><strong>$7,495</strong><br>
              monthly
            </p>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <p>*The income standards listed in these examples are&nbsp;subject to change annually&nbsp;every&nbsp;April.&nbsp;<br>
    ** Household includes the unborn child. For example, a single individual expecting one child is a 2-person household.
  </p>
  <p>This program provides coverage to pregnant individuals with countable income at or below the Apple Health standard, regardless of citizenship or immigration status. Your&nbsp;household size includes yourself, the&nbsp;unborn children, and&nbsp;additional household members such as a spouse and children.</p>
  <h2>After-Pregnancy Coverage</h2>
  <p>If you are enrolled in Apple Health coverage and are pregnant, your coverage will automatically transition to <a href="/node/24191">After-Pregnancy Coverage (APC)</a> once your pregnancy ends. APC lasts for 12 months, starting the first day of the month after your pregnancy ends. For example, if your pregnancy ended June 10, your health care coverage would continue through June 30 of the following year.</p>
  <p>You may be eligible for APC if you were pregnant in the last 12 months and were not on Apple Health during the pregnancy. After you are enrolled in APC, changes to your income will&nbsp;not affect your APC&nbsp;coverage regardless of how your pregnancy ends.</p>
  <div>
    <p><strong>Note</strong>: If you are on Apple Health coverage, report your pregnancy with an estimated due date to receive APC for up to 12 months after your pregnancy ends. We cannot guarantee a smooth transition into the APC program without this information. Learn <a href="/node/9091">how to report a change</a>.</p>
  </div>
  <h2>Confidential services</h2>
  <p>If you are a teen (under age 19) and you want your pregnancy-related services to be kept confidential, you may apply for coverage through a <a href="/assets/free-or-low-cost/14-430.pdf">paper application</a> process.</p>
  <h2>Applying for Apple Health coverage</h2>
  <p>You have many options to apply for Apple Health coverage. Visit our <a href="/node/256">Apply for or renew coverage</a>&nbsp;webpage to learn more.</p>
  <p>When you're ready to apply, you'll need:</p>
  <ul>
    <li>Your household monthly income.</li>
    <li>The Social Security numbers and dates of birth for each member of your household.</li>
    <li>Your immigration information, if that applies to you.</li>
  </ul>
  <h2>Enrollment next steps</h2>
  <p>If you're accepted, you'll receive a ProviderOne services card&nbsp;in about two weeks. Coverage will begin on the first day of the month in which the application was submitted. You'll have the option to select a managed care plan online or you'll be auto-enrolled into a plan. Learn more about <a href="/node/836">enrollment next steps</a>.</p>
  <div>
    <p>If you're not eligible for Apple Health, you may qualify for help with your health insurance or for other health services. Visit&nbsp;<a href="https://www.wahealthplanfinder.org/">Washington Healthplanfinder<span><span></span></span></a>&nbsp;or use the&nbsp;<a href="https://www.wahbexchange.org/mobile/">WAPlanfinder app<span><span></span></span></a>&nbsp;to learn if you qualify.</p>
  </div>
</div>

From the HTML, extract the eligibility rules (be as precise and detailed as possible). Then, write a Python program that asks the user questions and based on their answers, determines whether they are eligible for Medicaid under the Washington state Health Care Authority. The program should implement eligibility calculation for all Medicaid programs provided as input, and the program should output which specific Medicaid program the user is eligible for. 

Program requirements
You may be eligible for Apple Health for Pregnant individuals coverage if you:
- Are pregnant.
- Live in Washington State.
- Have income at or below 193% of the Federal Poverty Level (FPL) (see income chart below).*

What is the most I can make per month to qualify?
Apple Health for Pregnant Individuals
- n/a for a single person
- $3,254 monthly for a 2-person household
- $4,102 monthly for a 3-person household
- $4,950 monthly for a 4-person household
- $5,799 monthly for a 5-person household
- $6,647 monthly for a 6-person household
- $7,495 monthly for a 7-person household

After-Pregnancy Coverage
If you are enrolled in Apple Health coverage and are pregnant, your coverage will automatically transition to After-Pregnancy Coverage (APC) once your pregnancy ends. APC lasts for 12 months, starting the first day of the month after your pregnancy ends. 

Confidential services
If you are a teen (under age 19) and you want your pregnancy-related services to be kept confidential, you may apply for coverage through a paper application process.

Applying for Apple Health coverage
You have many options to apply for Apple Health coverage. Visit our Apply for or renew coverage webpage to learn more.

# Python program to determine eligibility for Apple Health for Pregnant Individuals

print("Welcome to the Apple Health for Pregnant Individuals eligibility checker!")
print("Please answer the following questions to determine your eligibility.")

# Prompt user for pregnancy status
pregnant = input("Are you pregnant? (y/n) ")

# Check if user is pregnant
if pregnant.lower() == "y":
    # Prompt user for Washington residency status
    residency = input("Do you live in Washington State? (y/n) ")

    # Check if user live in Washington State
    if residency.lower() == "y":
        # Prompt user for household size
        household_size = int(input("What is your household size? "))

        # Determine income limit based on household size
        if household_size == 1:
            print("Your household size includes yourself, the unborn children, and additional household members such as a spouse and children. For example, a single individual expecting one child is a 2-person household.")
            exit()
        elif household_size == 2:
            income_limit = 3254
        elif household_size == 3:
            income_limit = 4102
        elif household_size == 4:
            income_limit = 4950
        elif household_size == 5:
            income_limit = 5799
        elif household_size == 6:
            income_limit = 6647
        else:
            income_limit = 7495

        # Prompt user for monthly household income
        monthly_income = float(input("What is your monthly household income? "))

        # Check if monthly income is within limit
        if monthly_income <= income_limit:
            print("Congratulations, you are eligible for Apple Health for Pregnant Individuals!")
        else:
            print("Sorry, you are not eligible for Apple Health for Pregnant Individuals.")
    else:
        print("Sorry, you are not eligible for Apple Health for Pregnant Individuals.")
else:
    print("Sorry, you are not eligible for Apple Health for Pregnant Individuals.")

================================

Below is HTML from a webpage by the {state} describing state Medicaid eligibility rules: 

{html_extractor(soup)}

From the HTML, extract the eligibility rules (be as precise and detailed as possible). Then, write a Python program that asks the user questions and based on their answers, determines whether they are eligible for Medicaid under the {state}. The program should implement eligibility calculation for all Medicaid programs provided as input, and the program should output which specific Medicaid program the user is eligible for. 

"""
    return llm.invoke(prompt_html_to_python).content
