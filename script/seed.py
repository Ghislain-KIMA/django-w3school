import datetime

members_list = [ {'firstname': 'Emil', 'lastname': 'Refsnes', 'phone': 5551234, 'joined_date': datetime.date(2022, 1, 5)}, {'firstname': 'Tobias', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}, {'firstname': 'Linus', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}, {'firstname': 'Lene', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}, {'firstname': 'Stalikken', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}]

from members.models import Member

for member in members_list:
    Member.objects.create(
        firstname=member["firstname"],
        lastname=member["lastname"],
        phone=member["phone"],
        joined_date=member["joined_date"]
    )
