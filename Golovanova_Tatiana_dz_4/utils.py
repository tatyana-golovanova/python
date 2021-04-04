import decimal
import datetime
import xml.etree.ElementTree as ET

from requests import get


def currency_rates(currency_code):
    currency_code = currency_code.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(response.content)
    for element in tree:
        _, code, _, _, value = element.itertext()
        if code == currency_code:
            date = datetime.datetime.strptime(tree.attrib['Date'], '%d.%m.%Y').date()
            quotation = decimal.Decimal(value.replace(',', '.'))
            return {
                'quotation': quotation,
                'date': date
            }
