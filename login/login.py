def file_to_dict(file):
    user_pass_map = {}

    line = file.readline()
    while line:
        line_arr = line.split(":")
        user_pass_map.update({line_arr[0] : line_arr[1]})

        line = file.readline()

    return user_pass_map

def main():
    # get existing user/password mappings
    user_pass_file = open("userpass.txt", "rw")
    user_pass_map = file_to_dict(user_pass_file)

    



if __name__ == "__main__":
