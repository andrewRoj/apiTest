import json
import requests


class CreditCard:

    def __init__(self, bearer_token):
        self.url = "https://payments.sandbox.braintree-api.com/graphql"

        self.bearer_token = bearer_token

    def tokenize_credit_card(self):

        body = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "custom",
                "sessionId": "665i50bb8c-6odc-9U94-8Km3-5d216177qz78"
            },
            "operationName": "TokenizeCreditCard",
            "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
            "variables": {
                "input": {"creditCard": {
                    "number": "6011000991300009",
                    "expirationMonth": "3",
                    "expirationYear": "2022",
                    "cvv": "323",
                    "billingAddress": {
                        "postalCode": 44323
                    }
                },
                    "options": {
                        "validate": True
                    }
                }
            }
        }


        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json',
            'Braintree-Version': '2018-05-10',
            'Host': 'payments.sandbox.brain_files-api.com'

        }

        response = requests.post(self.url, headers=headers, json=body)

        credit_card_data = json.loads(response.text)
        tokenize_credit_card = credit_card_data["data"]["tokenizeCreditCard"]

        return tokenize_credit_card
