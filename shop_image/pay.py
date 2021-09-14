
from paystack.resource import TransactionResource

import random
import string


def main():
    rand = ''.join(
        [random.choice(
            string.ascii_letters + string.digits) for n in range(16)])
    secret_key = 'sk_test_bccfb1827d1e81b18073ca06a5239f60ff16740b'
    random_ref = rand
    test_email = 'ex@mail.com'
    test_amount = '10000'
    # plan = 'Basic'
    client = TransactionResource(secret_key, random_ref)
    response = client.initialize(test_amount,
                                 test_email)
    print(response)
    client.authorize()  # Will open a browser window for client to enter card details
    verify = client.verify()  # Verify client credentials
    print(verify)
    print(client.charge())  # Charge an already exsiting client


main()
