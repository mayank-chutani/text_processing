__author__ = 'mayank'
import xmltodict

class XmlToJson:
    """
    Converts XML to Nested Json object.
    While creating the object (constructor):
    Pass filepath as parameter if you want to convert it from a .xml file
     Else pass xml as content = <xml string> to convert it from string
    """
    content = None

    def __init__(self, filepath=None, content=None):
        if filepath:
            f = open(filepath, 'r')
            self.content = f.read()
            f.close()
        elif content:
            self.content = content

    def __parse_ordered_dict(self, node):
        item = {}
        keys = node.keys()
        for key in keys:
            if isinstance(node[key], xmltodict.OrderedDict):
                doc = self.__parse_ordered_dict(node[key])
                item[key] = doc
            else:
                item[key] = node[key]
        return item

    def convert(self):
        """
        Converts XML passed to the constructor into Json Object
        :return: dict
        """
        content = self.content
        rootNode = xmltodict.parse(content)
        return self.__parse_ordered_dict(rootNode)


# obj = XmlToJson(filepath='')
# print obj.convert()