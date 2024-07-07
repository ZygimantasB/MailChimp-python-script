import gspread
from dotenv import load_dotenv

load_dotenv()


class GoogleSheetAPI:

    def __init__(self, service_account_filename: str, sheet_name: str, work_sheet_name: str) -> None:
        service_account = gspread.service_account(filename=service_account_filename)
        sheet_name = service_account.open(sheet_name)  # mailchimp
        self.work_sheet_name = sheet_name.worksheet(work_sheet_name)  # Sheet1

    def get_data(self) -> list:
        """
        Read data from Google Sheets
        """

        records = self.work_sheet_name.get_all_records()

        data = [{'First Name:': record['First Name'],
                 'Last Name': record['Last Name'],
                 'Email Address': record['Email Address']}
                for record in records]

        return data
