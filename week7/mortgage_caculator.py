""" Version 1 """
# globals shared by more than one function and/or our program ---
# (initialize to None to force program to define them later)
mtg_pricipal = None
annual_int_rate = None
mtg_years = None


# function definitions ------------------

def state_purpose():
    """ gives an overview to user """

    instructions = \
        "\nThe following program will calculate the \n" \
        "monthly payment required for a loan of D dollars \n" \
        "over a period of Y years at an annual \n" \
        "interest rate of R%. \n";
    print(instructions)


def get_input():
    """ get input from user; stores into globals for the other functions/main """
    global mtg_pricipal
    global annual_int_rate
    global mtg_years

    # get principal
    prompt = "\nEnter amount of the loan. (only use numbers, \n" \
             "please, no commas or characters like '$')\n" \
             "Your loan amount: "
    mtg_pricipal = float(input(prompt))

    # get annual interest rate
    prompt = "\nNow enter the interest rate (if the quoted rate if 6.5%, \n" \
             "for example, enter 6.5 without the %.)\n" \
             "Your annual interest rate: "
    annual_int_rate = float(input(prompt))

    # get length of loan
    prompt = "\nEnter term of the loan in years: "
    mtg_years = float(input(prompt))


def compute_monthly_payment():
    """ use values in globals to compute an return monthly payment """
    # convert years to months
    mtg_months = mtg_years * 12

    # convert rate to decimal and months
    monthly_int_rate = annual_int_rate / (100 * 12)

    # use formular to get result
    temp = (1 + monthly_int_rate) ** mtg_months
    payment = mtg_pricipal * monthly_int_rate * temp \
              / (temp - 1)

    return payment


def say_goodbye():
    """ display a farewell message """

    signoff = "\nThanks for using the Foothill Mortgage Calculator. \n" \
              "We hope you'll come back and see u again, soon. \n\n"
    print(signoff)




# main program ----------------------------------

""" program that computes and displays monthly payments for mortages """
state_purpose()
get_input()
answer = compute_monthly_payment()
print("Your Monthly Payment: ${:,.2f}".format(answer))
say_goodbye()

