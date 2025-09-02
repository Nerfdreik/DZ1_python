from address import Address
from mailing import Mailing

to_address = Address("11111", "Moscow", "Gagarina", "6", "12")
from_address = Address("22222", "Gzhel", "Pushkina", "4", "22")

mail = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=1000,
    track="рейс123"
)

output = (
    f"Отправление {mail.track}"
 f"из{mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house}, {mail.from_address.apartment}"
 f"в {mail.to_address.index}. {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house}, {mail.to_address.apartment}"
 f"стоимость {mail.cost} рублей"
)
print(output)
