from mailchimp3 import MailChimp
from os import getenv


class MailChimpAPI:

    def __init__(self):
        self.client = MailChimp(mc_api=getenv('API_KEY'), mc_user=getenv('MC_USER'))

    def add_subscriber(self, list_id: str, name: str, email: str) -> None:
        """
        Adds a subscriber to the list
        :param email: email address of the subscriber
        :param name: name of the subscriber
        :param list_id: id of the list
        """

        first_name, last_name = name.split(' ')

        self.client.lists.members.create(list_id, {
            'email_address': email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': first_name,
                'LNAME': last_name
            },
        })
