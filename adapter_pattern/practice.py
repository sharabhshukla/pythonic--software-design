

class XMLData(object):
    def __init__(self, name):
        self.name = name

    def get_xml_data(self):
        return "XML Data get everything"


class PanData(object):
    def __init__(self, name):
        self.name = name

    def get_pd_data(self):
        return "This is a pandas data frame"


class JSONData(object):
    def __init__(self, name):
        self.name = name

    def get_json_data(self):
        return "This is a sample json data"


class Adapter(object):

    def __init__(self, obj, **updated_methods):
        self.obj = obj
        self.__dict__.update(updated_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr, 'Not Found')

    def original_dict(self):
        return self.obj.__dict__



if __name__ == '__main__':
    xml_data = XMLData('xml test')
    pnd_data = PanData('pd data')
    json_data = JSONData('JSON Data')
    # Convert different types of data into str format

    adapter_objects = [ Adapter(pnd_data, output_data=pnd_data.get_pd_data),
                        Adapter(xml_data, ouput_data=xml_data.get_xml_data)]

    for adapter_object in adapter_objects:
        temporary_output = adapter_object.output_data()
        print(temporary_output)

