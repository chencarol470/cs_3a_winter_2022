# function definitions -----------------------------

def state_purpose():
    """ gives an overview to user """

    instructions = \
        "\nThe following program will calculate the \n" \
        "monthly payment required for a loan of D dollars \n" \
        "over a period of Y years at an annual \n" \
        "interest rate of R%.\n";
    print(instructions)


def get_input(the_loan=None):
    """ get input from user; result in in MortgageData ("MD")
       for flexibility, give client choice of passing MD
       object or not -- if not, we instantiate for them and
       return as functional return """

    # if they aren't passing a MD object, create one here
    if the_loan == None:
        the_loan = MortgageData()

    # get principal
    prompt = ("\nEnter amount of the loan. (only use numbers, no\n" \
              "commas or characters like '$'.)\n" \
              "(Valid range: {} - {})\n" \
              "Your principal loan amount: ").format(MortgageData.MIN_LOAN,
                                                     MortgageData.MAX_LOAN)
    validated = False
    while not validated:
        user_answer = float(input(prompt))

        # let the mutator tell us whether user answer is valid
        if the_loan.set_pricipal(user_answer):
            validated = True
        else:
            print("\n *** Input error. Try again *** ")

    # get interest
    prompt = "\nNow enter the interest rate (If the quoted rate is 6.5%, \n" \
             "for example, enter 6.5 without the %.)\n" \
             "Your annual interest rate: "
    validated = False
    while not validated:
        user_answer = float(input(prompt))

        if the_loan.set_interest(user_answer):
            validated = True
        else:
            print("\n *** Input error. Try again *** ")

    # get length of loan
    prompt = "\nEnter term of the loan in years: "
    validated = False
    while not validated:
        user_answer = float(input(prompt))

        if (the_loan.set_loan_len(user_answer)):
            validated = True
        else:
            print("\n *** Input error. Try again *** ")


def compute_monthly_payment(mtg_data):
    """ mtg_data assumed to reference a MortgageData object """

    # remember the multi-variable assignment statement
    mtg_principal, annual_int_rate, mtg_years \
        = \
        mtg_data.get_principal(), \
        mtg_data.get_rate(), \
        mtg_data.get_years()

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


class MortgageData():
    """ each object represents the
           -principal- amount borrowed
           -rate- of interested charged
           -year- that the mortange will take to payoff
        """
    # class ("static") intended constants
    MIN_LOAN = 0
    MAX_LOAN = 1000000
    MIN_RATE = 0.00001
    MAX_RATE = 25.0
    MIN_YRS = 1
    MAX_YRS = 100
    MIN_STRING_LENGTH = 1
    MAX_STRING_LENGTH = 50
    ORIGINAL_DEFAULT_PRINC = MIN_LOAN
    ORIGINAL_DEFAULT_RATE = MIN_RATE
    ORIGINAL_DEFAULT_YEARS = MIN_YRS

    # class attributed that will change over time
    default_principal = ORIGINAL_DEFAULT_PRINC
    default_rate = ORIGINAL_DEFAULT_RATE
    default_years = ORIGINAL_DEFAULT_YEARS

    # initializer method -------------------------------

    def __init__(self,
                 principal=None,
                 rate=None,
                 years=None):

        # repair mutable defaults
        if (principal == None):
            self.principal = self.default_principal
        if (rate == None):
            self.rate = self.default_rate
        if (years == None):
            self.years = self.default_years

        # instance attributes
        if (not self.set_principal(principal)):
            self.width = self.default_principal
        if (not self.set_rate(rate)):
            self.rate = self.default_rate
        if (not self.set_years(years)):
            self.years = self.default_years

    def get_principal(self):
        return self.principal

    def get_rate(self):
        return self.rate

    def get_years(self):
        return self.years

    def set_principal(self, new_principal):
        if not self.MIN_LOAN <= new_principal <= self.MAX_LOAN:
            print(f"Value error, loan amount must be between {self.MIN_LOAN} to {self.MAX_LOAN}")
        self.principal = new_principal

    def set_rate(self, new_rate):
        self.rate = new_rate

    def set_years(self, new_years):
        if not self.MIN_LOAN <= new_years <= self.MAX_LOAN:
            print(f"Value error, loan length must be between {self.MIN_LOAN} to {self.MAX_LOAN}")
        self.years = new_years


# main program -----------------------------------

""" program that computes and displays monthly payments for mortgages  """
state_purpose()

# one way to get input into a MD object using our new class
user_input = get_input()
loan = MortgageData(user_input)


# alternate way to do it (no need to instantiate loan above if use this)
# loan = get_input()

answer = compute_monthly_payment(loan)  # does the math
report_results_and_signoff(answer)  # reports to user
