import os
import hashlib

def get_addon_xml(addon_folder):
    with open(os.path.join(addon_folder, 'addon.xml'), 'r', encoding='utf-8') as f:
        return f.read().strip()

def create_addons_xml(addons_path):
    addons = []
    for addon in sorted(os.listdir(addons_path)):
        addon_path = os.path.join(addons_path, addon)
        if os.path.isdir(addon_path) and os.path.exists(os.path.join(addon_path, 'addon.xml')):
            xml = get_addon_xml(addon_path)
            addons.append(xml)

    full_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n' + '\n'.join(addons) + '\n</addons>'
    with open('addons.xml', 'w', encoding='utf-8') as f:
        f.write(full_xml)

    md5 = hashlib.md5(full_xml.encode('utf-8')).hexdigest()
    with open('addons.xml.md5', 'w') as f:
        f.write(md5)

create_addons_xml('addons')
