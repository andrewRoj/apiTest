from Customer import users
from payments import PaymentInfo
from helpers import getResponseData


class TestBrainTreeTokenization:

    def test_adding_credit_card_to_braintree(self):
        user_object = users.User("HOST")
        new_user_object = user_object.signup()
        new_user = getResponseData.response_data(new_user_object)
        new_user_auth_token = user_object.get_user_auth(new_user)

        client_token = "Xzyo34242SO3uTmLQ1229lmofawC"
        payment_object = PaymentInfo.CreditCard(client_token)
        credit_card_token = payment_object.tokenize_credit_card()

        assert credit_card_token is not None