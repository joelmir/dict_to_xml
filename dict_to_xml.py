#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	Simple xml serializer to lxml.etree Elemets.
	@author Joelmir Ribacki 2015
"""

from lxml import etree

def dict_to_xml(d, root_node=None):
	root = 'objects' if None == root_node else root_node
	if isinstance(d, dict):
		obj_xml = etree.Element(root)
		for key, value in dict.items(d):
			if isinstance(value, dict) or isinstance(value, list):
				_obj_xml = dict_to_xml(value, key)
				if isinstance(_obj_xml, list):
					for elem in _obj_xml:
						obj_xml.append(elem)	
				else:
					obj_xml.append(_obj_xml)
			else:
				obj_xml.attrib[str(key)] = str(value)
	else:
		root_singular = root[:-1] if 's' == root[-1] and None == root_node else root
		children_obj  = []
		for value in d:
			children_obj.append(dict_to_xml(value, root_singular))
		return children_obj		
	return obj_xml