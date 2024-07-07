from google_sheet import GoogleSheetAPI
from mailchimp_api import MailChimpAPI
from mailchimp3.mailchimpclient import MailChimpError
from os import getenv


def main() -> None:
    """
    Main function
    """
    google_sheet = GoogleSheetAPI(service_account_filename='expanded-guide-392113-3d87472fc006.json',
                                  sheet_name='mailchimp',
                                  work_sheet_name='Sheet1')
    mailchimp = MailChimpAPI()

    data = google_sheet.get_data()

    for record in data:
        try:
            mailchimp.add_subscriber(list_id=getenv('LIST_ID'),
                                     name=record['First Name:'],
                                     email=record['Email Address'])
        except MailChimpError as error_mailchimp:
            print(f"Failed to add a subscriber {record['Email Address']} to the list. Error: {error_mailchimp}")


if __name__ == "__main__":
    main()
