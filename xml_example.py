import xml.etree.ElementTree as EL

xml_data = """
<user>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Johnson</last_name>
    <email>john@fakemail.fake</email>
    <address>
        <street>Main</street>
        <city>New York</city>
        <zip>123456</zip>
    </address>
</user>
"""

root = EL.fromstring(xml_data)

print('User ID:', root.find('id').text)
print('First Name:', root.find('first_name').text)
