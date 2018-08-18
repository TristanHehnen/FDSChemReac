# Started out from table 12.1 in the FDS Users Guide, page 134,
# January 18, 2017, Revision: FDS6.5.3-569-ge3d0d6c
#
# It contains molecules, as well as individual chemical elements.
# Format: key as chemical formula
#         value as list of lists, first element is FDS name, second list of
#         chemical elements used in this molecule.


ChemicalSpecies = {
    "C3H6O": ["ACETONE", [["C", 3], ["H", 6], ["O", 1]]],
    "C2H2": ["ACETYLENE", [["C", 2], ["H", 2]]],
    "C3H4O": ["ACROLEIN", [["C", 3], ["H", 4], ["O", 1]]],
    "NH3": ["AMMONIA", [["N", 1], ["H", 3]]],
    "Ar": ["ARGON", [["Ar", 1]]],
    "C6H6": ["BENZENE", [["C", 6], ["H", 6]]],
    "C4H10": ["BUTANE", [["C", 4], ["H", 10]]],
    "CO2": ["CARBON DIOXIDE", [["C", 1], ["O", 2]]],
    "CO": ["CARBON MONOXIDE", [["C", 1], ["O", 1]]],
    "Cl2": ["CHLORINE", [["Cl", 1]]],
    "C12H26": ["DODECANE", [["C", 12], ["H", 26]]],
    "C2H6": ["ETHANE", [["C", 2], ["H", 6]]],
    "C2H5OH": ["ETHANOL", [["C", 2], ["H", 6], ["O", 1]]],
    "C2H4": ["ETHYLENE", [["C", 2], ["H", 4]]],
    "CH2O": ["FORMALDEHYDE", [["C", 1], ["H", 2], ["O", 1]]],
    "H2": ["HYDROGEN", [["H", 2]]],
    "HBr": ["HYDROGEN BROMIDE", [["H", 1], ["Br", 1]]],
    "HCl": ["HYDROGEN CHLORIDE", [["H", 1], ["Cl", 1]]],
    "HCN": ["HYDROGEN CYANIDE", [["C", 1], ["H", 1], ["N", 1]]],
    "HF": ["HYDROGEN FLUORIDE", [["H", 1], ["F", 1]]],
    "H2O2": ["HYDROGEN PEROXIDE", [["H", 2], ["O", 2]]],
    "HO2": ["HYDROPEROXY RADICAL",[["H", 1], ["O", 2]]],
    "OH": ["HYDROXYL RADICAL", [["H", 1], ["O", 1]]],
    "C3H7OH": ["ISOPROPANOL", [["C", 3], ["H", 8], ["O", 1]]],
    "CH4": ["METHANE", [["C", 1], ["H", 4]]],
    "CH3OH": ["METHANOL", [["C", 3], ["H", 4], ["O", 1]]],
    "C10H22": ["N-DECANE", [["C", 10], ["H", 22]]],
    "C7H16": ["N-HEPTANE", [["C", 7], ["H", 16]]],
    "C6H12": ["N-HEXANE", [["C", 6], ["H", 12]]],
    "C8H18": ["N-OCTANE", [["C", 8], ["H", 18]]],
    "NO": ["NITRIC OXIDE", [["N", 1], ["O", 1]]],
    "N2": ["NITROGEN", [["N", 2]]],
    "NO2": ["NITROGEN DIOXIDE", [["N", 1], ["O", 2]]],
    "N2O": ["NITROUS OXIDE", [["N", 2], ["O", 1]]],
    "O2": ["OXYGEN", [["O", 2]]],
    "C3H8": ["PROPANE", [["C", 3], ["H", 8]]],
    "C3H6": ["PROPYLENE", [["C", 3], ["H", 6]]],
    "SO2": ["SULFUR DIOXIDE", [["S", 1], ["O", 2]]],
    "SF6": ["SULFUR HEXAFLUORIDE", [["S", 1], ["F", 6]]],
    "C6H5CH3": ["TOLUENE", [["C", 7], ["H", 8]]],
    "H2O": ["WATER VAPOR", [["H", 2], ["O", 1]]]}