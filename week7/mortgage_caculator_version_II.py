""" Version 2 """


# function definitions -----------------------------

def state_purpose():
    """ gives an overview to user """

    instructions = \
        "\nThe following program will calculate the \n" \
        "monthly payment required for a loan of D dollars \n" \
        "over a period of Y years at an annual \n" \
        "interest rate of R%.\n";
    print(instructions)


def get_input(input_list):
    """ get input from user; result in param input_list [princ, rate, yrs] """

    # make sure no garbage left it input_list
    input_list.clear()

    # get principal
    prompt = "\nEnter amount of the loan. (only use numbers, \n" \
             "please, no commas or characters like '$')\n" \
             "Your loan amount: "
    input_list.append(float(input(prompt)))

    # get interest
    prompt = "\nNow enter the interest rate (If the quoted rate is 6.5%, \n" \
             "for example, enter 6.5 without the %.)\n" \
             "Your annual interest rate: "
    input_list.append(float(input(prompt)))

    # get length of loan
    prompt = "\nEnter term of the loan in years: "
    input_list.append(float(input(prompt)))


def compute_monthly_payment(mtg_val_list):
    # check out this new (for us) multi-variable assignment statement
    mtg_principal, annual_int_rate, mtg_years \
        = mtg_val_list[0], mtg_val_list[1], mtg_val_list[2]

    # convert years to months
    mtg_months = mtg_years * 12

    # convert rate to decimal and months
    monthly_int_rate = annual_int_rate / (100 * 12)

    # use formula to get result
    temp = (1 + monthly_int_rate) ** mtg_months
    payment = mtg_principal * monthly_int_rate * temp \
              / (temp - 1)

    return payment


def report_results_and_signoff(payment):
    """ display results and say goodbye """

    print("\n*** Your Monthly Payment: ${:,.2f} ***".format(answer))
    print("\nThanks for using the Foothill Mortgage Calculator. \n" \
          "We hope you'll come back and see us again, soon.\n\n")


# main program -----------------------------------

""" program that computes and displays monthly payments for mortages  """
state_purpose()
input_list = []  # arg for get_input()
get_input(input_list)
answer = compute_monthly_payment(input_list)  # does the math
report_results_and_signoff(answer)  # reports to user
