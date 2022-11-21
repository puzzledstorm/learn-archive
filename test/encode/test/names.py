import uuid


class NamePair(object):

    def __init__(self, temp_out, final_out):
        self.temp_out = temp_out
        self.final_out = final_out


def get_name_group(count):
    group = []
    for i in range(count):
        uuid_t = str(uuid.uuid4()).replace('-', '')
        temp_out = f"{uuid_t}temp.mp4"
        final_out = f"{uuid_t}final.mp4"
        group.append(NamePair(temp_out, final_out))
    return group


names = get_name_group(2)
print(names)
print(names[0].temp_out)
print(names[0].final_out)

