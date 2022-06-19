#kreiranje XML fajla za lokalni kontroler
import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="interval").text = "5min"

tree = ET.ElementTree(root)
ET.indent(tree, space=' ', level=0) #za formatiranje xml-a
tree.write("buffer.xml")



#NE KORISTIMO