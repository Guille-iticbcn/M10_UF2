import xml.etree.ElementTree as ET

def crear_xml():
    root = ET.Element("students")

    for i in range(1, 6):
        student = ET.SubElement(root, "student")
        student.set("id", str(i))  

        name = ET.SubElement(student, "name")
        name.text = f"nom_{i}"

        surname = ET.SubElement(student, "surname")
        surname.text = f"cognom_{i}"

        email = ET.SubElement(student, "email")
        email.text = f"estudiant{i}@gmail.com"

        dni = ET.SubElement(student, "dni")
        dni.text = f"DNI{i}123456"

    tree = ET.ElementTree(root)

    tree.write("students.xml")

    with open("students.xml", "r") as xml_file:
        xml_content = xml_file.read()
        print(xml_content)

crear_xml()
