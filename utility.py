import schwifty
import random


def generate_account_number():
    account_code = [str(random.randint(0, 9)) for _ in range(16)]
    iban = schwifty.IBAN.generate('PL', "102", "".join(account_code))
    without_country_code = str(iban.account_code)[2:]

    return without_country_code


if __name__ == "__main__":
    print(generate_account_number())
