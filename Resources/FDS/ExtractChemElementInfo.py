with open('elements_data.f90') as el_raw:
    el_raw_content = el_raw.readlines()


def extract_string(begin, end, string):
    """
    Takes a sub-string out of a string, which is located between 'begin'
    and 'end'.
    :param begin: sub-string of 'string'
    :param end: sub-string of 'string'
    :param string: string in which to look for 'begin' and 'end'
    :return: sub-string of 'string' between 'begin' and 'end'
    """
    b = string.find(begin) + len(begin)
    e = string.find(end, b)

    return string[b:e]


# Template for the individual lines of the new dictionary.
new_dict_line = "'{}': ['{}', {}],"


# Header of the new file.
periodic_table_dict_content = ["# Data taken from FDS 6.5.3 source code, file 'data.f90', lines 3687 to 3804.",
"# https://github.com/firemodels/fds/blob/eff7cba5ef7e452d6b646f9e3293a5b0b7dfbd4f/Source/data.f90#L3687",
"# https://github.com/firemodels/fds/blob/eff7cba5ef7e452d6b646f9e3293a5b0b7dfbd4f/Source/data.f90#L3804",
                               "",
                               "PeriodicTable = {"]


# Iterate over the input file and extract the chemical element information.
# Skip the first 4 lour lines.
for i in el_raw_content[4:]:
    line = i.split(';')

    aa = extract_string("ABBREVIATION='", "'", line[0])
    bb = extract_string("NAME='", "'", line[1])
    cc = extract_string("MASS=", "_EB", line[2])

    periodic_table_dict_content.append(new_dict_line.format(aa, bb, cc))

periodic_table_dict_content.append("                 }")


# Write new Python file, that contains the periodic table dictionary.
with open("PeriodicTableFDS653.py", "w") as text_file:
    for i in periodic_table_dict_content:
        print(i, file=text_file)
