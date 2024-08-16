def read_dict(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            input_dict = {}
            for line in lines:
                key, value = line.strip().split(': ')
                # Multiple values separated by commas
                value_list = value.split(', ')
                for v in value_list:
                    if v not in input_dict:
                        input_dict[v] = []
                    input_dict[v].append(key)
            return input_dict
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def write_dict(filename, dictionary):
    try:
        with open(filename, 'w') as file:
            for key in sorted(dictionary.keys()):
                values = ', '.join(sorted(dictionary[key]))
                file.write(f"{key}: {values}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def invert(input_dict):
    invert = {}
    for key, values in input_dict.items():
        for value in values:
            if value not in invert:
                invert[value] = []
            invert[value].append(key)
    return invert


# Main program
input_filename = 'input_dict.txt'
output_filename = 'inverted_dict.txt'

# Read the main dictionary from the file
main_dict = read_dict(input_filename)

if main_dict:
    # Invert the dictionary
    inverted_dict = invert(main_dict)

    # Write the inverted dictionary to the output file
    write_dict(output_filename, inverted_dict)

    print("Dictionary inverted and written to the output file.")
