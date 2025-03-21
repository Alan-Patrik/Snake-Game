from datetime import datetime


class Utils:
    @staticmethod
    def get_formatted_date():
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M:%S")
        current_date = current_datetime.strftime("%d/%m/%y")
        return f"{current_time} - {current_date}"
