import uuid
from pprint import pprint


def get_name_group(count):
    temp_path = "/mnt/"
    group = []
    for i in range(count):
        uuid_t = str(uuid.uuid4()).replace('-', '')
        temp_out = f"{temp_path}{uuid_t}temp.mp4"
        final_out = f"{temp_path}{uuid_t}final.mp4"
        group.append(dict(tmep_out=temp_out, final_out=final_out))
    return group


pprint(get_name_group(4))
