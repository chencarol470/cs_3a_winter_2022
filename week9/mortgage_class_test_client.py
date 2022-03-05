import locale

locale.setlocale(locale.LC_ALL, '')


class MortgageData:
    """ each object represents the
        -principal- amount borrowed
        -rate- of interested charged
        -year- that the mortange will take to payoff
    """
    # class intended constants
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

    # class attributs that will change over time
    default_principal = ORIGINAL_DEFAULT_PRINC
    default_rate = ORIGINAL_DEFAULT_RATE
    default_years = ORIGINAL_DEFAULT_YEARS

    # initializer method -------------------------------
    def __init__(self,
                 principal=None,
                 rate=None,
                 years=None):
        self.principal = principal
        self.rate = rate
        self.years = years

        # repair mutable defaults
        if self.principal == None:
            self.principal = self.default_principal
        if self.rate == None:
            rate = self.default_rate
        if self.years == None:
            years = self.default_years

        # instance attributes
        if (not self.set_principal(principal)):
            self.width = self.default_principal
        if (not self.set_rate(rate)):
            self.rate = self.default_rate
        if (not self.set_years(years)):
            self.years = self.default_years

    # setters -----------------------------------------------
    def set_principal(self, principal):
        if not (self.MIN_LOAN <= principal <= self.MAX_LOAN):
            return False
        # else
        self.principal = principal
        return True

    def set_rate(self, rate):
        if not (self.MIN_RATE <= rate <= self.MAX_RATE):
            return False
        # else
        self.rate = rate
        return True

    def set_years(self, years):
        if not (self.MIN_YRS <= years <= self.MAX_YRS):
            return False
        # else
        self.years = years
        return True

    # getters -----------------------------------------------
    def get_principal(self):
        return self.principal

    def get_rate(self):
        return self.rate

    def get_years(self):
        return self.years

    # output method  ----------------------------------------
    def show_me(self, client_intro_str=""):
        print(self.to_string(client_intro_str))

    # instance helpers -------------------------------
    def to_string(self, optional_title=" --- "):
        if not self.valid_string(optional_title):
            optional_title = " --- "

        loan_nice = locale.currency(self.principal, grouping=True)

        ret_str = ((optional_title
                    + "\n    loan amount: {}"
                    + "\n    annual rate: {:8.2f}%"
                    + "\n    duration: {} years.").
                   format(loan_nice, self.rate, self.years))
        return ret_str

    # static and class helpers -------------------------------
    @classmethod
    def valid_string(cls, the_str):
        if (type(the_str) != str or not
        (cls.MIN_STRING_LENGTH <= len(the_str) <= cls.MAX_STRING_LENGTH)):
            return False
        # else
        return True

    @classmethod
    def valid_prin(cls, prin_in):
        if ((type(prin_in) != float and type(prin_in) != int)
                or not (cls.MIN_LOAN <= prin_in <= cls.MAX_LOAN)):
            return False
        # else
        return True

    @classmethod
    def valid_rate(cls, rate_in):
        if ((type(rate_in) != float and type(rate_in) != int)
                or not (cls.MIN_RATE <= rate_in <= cls.MAX_RATE)):
            return False
        # else
        return True

    @classmethod
    def valid_years(cls, yrs_in):
        if (type(yrs_in) != int or not
        (cls.MIN_YRS <= yrs_in <= cls.MAX_YRS)):
            return False
        # else
        return True

    # class setters and getters ----------------------------
    @classmethod
    def set_default_principal(cls, new_prin):
        if not cls.valid_prin(new_prin):
            return False
        # else
        cls.default_principal = new_prin
        return True

    @classmethod
    def set_default_rate(cls, new_rate):
        if not cls.valid_rate(new_rate):
            return False
        # else
        cls.default_rate = new_rate
        return True

    @classmethod
    def set_default_years(cls, new_years):
        if not cls.valid_years(new_years):
            return False
        # else
        cls.default_years = new_years
        return True


# client --------------------------------------------

# test parameter-taking instantiation with bad years
loan_1 = MortgageData()

# test class mutators
MortgageData.set_default_principal(250000)
MortgageData.set_default_rate(5.25)
MortgageData.set_default_years(15)

# test default constructor with new defaults just set
loan_2 = MortgageData()

# show original data
loan_1.show_me("Loan 1")
loan_2.show_me("Loan 2")

""" --------------------------- RUN ---------------------------
Loan 1
    loan amount: $100,000.00
    annual rate:     4.30%
    duration: 1 years.
Loan 2
    loan amount: $250,000.00
    annual rate:     5.25%
    duration: 15 years.
------------------------------------------------------------ """
