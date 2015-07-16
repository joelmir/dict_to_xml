#!/usr/bin/python
# -*- coding: utf-8 -*-

from dict_to_xml import dict_to_xml
from lxml import etree

'''
    Exemple:
'''

mydict = {
    'name': 'The Andersson\'s',
    'size': 4,
    'children': {
        'total-age': 62,
        'child': [
            { 'name': 'Tom', 'sex': 'male', },
            {
                'name': 'Betty',
                'sex': 'female',
                'grandchildren': {
                    'grandchild': [
                        { 'name': 'herbert', 'sex': 'male', },
                        { 'name': 'lisa', 'sex': 'female', }
                    ]
                },
            }
        ]
    },
}

obj_xml = dict_to_xml(mydict, 'family')
print(etree.tostring(obj_xml, encoding='utf-8',xml_declaration=True, pretty_print=True))

'''
<?xml version='1.0' encoding='utf-8'?>
<family name="The Andersson's" size="4">
  <children total-age="62">
    <child name="Tom" sex="male"/>
    <child name="Betty" sex="female">
      <grandchildren>
        <grandchild name="herbert" sex="male"/>
        <grandchild name="lisa" sex="female"/>
      </grandchildren>
    </child>
  </children>
</family>

'''