"""Dictionary with default config."""

_default_config = {
    'C2F6_halocarbon': {'molarMass': 138.01, 'rho': 0.00026, 'tau': 10000.0},
    'CCl4_halocarbon': {'molarMass': 153.8, 'rho': 0.00013, 'tau': 26.0},
    'CF4_halocarbon': {'H0': (35.0, 'pptv'),
                       'molarMass': 88.0043,
                       'rho': 8e-05,
                       'tau': 50000.0},
    'CFC113_halocarbon': {'molarMass': 187.35, 'rho': 0.0003, 'tau': 85.0},
    'CFC114_halocarbon': {'molarMass': 170.9, 'rho': 0.00031, 'tau': 300},
    'CFC115_halocarbon': {'molarMass': 154.45, 'rho': 0.00018, 'tau': 1700},
    'CFC11_halocarbon': {'molarMass': 137.35, 'rho': 0.00025, 'tau': 45.0},
    'CFC12_halocarbon': {'molarMass': 120.9, 'rho': 0.00032, 'tau': 100},
    'CH3Br_halocarbon': {'H0': 5.8,
                         'molarMass': 94.9,
                         'rho': 1e-05,
                         'tau': 0.7},
    'CH3CCl3_halocarbon': {'molarMass': 133.35, 'rho': 6e-05, 'tau': 5.0},
    'CH3Cl_halocarbon': {'H0': 504.0,
                         'molarMass': 50.45,
                         'rho': 1e-05,
                         'tau': 1.3},
    'CH4': {'CH4N': 300,
            'M0': 653,
            'Tsoil': 160,
            'Tstrat': 120,
            'UC_CH4': 2.78},
    'HCF141b_halocarbon': {'molarMass': 116.9, 'rho': 0.00014, 'tau': 9.3},
    'HCF142b_halocarbon': {'molarMass': 100.45, 'rho': 0.0002, 'tau': 17.9},
    'HCF22_halocarbon': {'molarMass': 86.45, 'rho': 0.0002, 'tau': 12.0},
    'HFC125_halocarbon': {'molarMass': 120.02, 'rho': 0.00023, 'tau': 29.0},
    'HFC134a_halocarbon': {'molarMass': 102.02, 'rho': 0.00016, 'tau': 14.0},
    'HFC143a_halocarbon': {'molarMass': 84.04, 'rho': 0.00013, 'tau': 52.0},
    'HFC227ea_halocarbon': {'molarMass': 170.03, 'rho': 0.00026, 'tau': 34.2},
    'HFC23_halocarbon': {'molarMass': 70.0, 'rho': 0.00019, 'tau': 270.0},
    'HFC245fa_halocarbon': {'molarMass': 134.0, 'rho': 0.00028, 'tau': 7.6},
    'HFC32_halocarbon': {'molarMass': 52.0, 'rho': 0.00011, 'tau': 4.9},
    'HFC4310_halocarbon': {'molarMass': 252.0, 'rho': 0.0004, 'tau': 15.9},
    'N2O': {'N0': 272.9596,
            'N2ON_emissions': [(1765, 11), (2000, 8), (2300, 8)],
            'TN2O0': 132,
            'UC_N2O': 4.8},
    'OH': {'CCH4': -0.32,
           'CCO': -0.000105,
           'CNMVOC': -0.000315,
           'CNOX': 0.0042,
           'TOH0': 6.6},
    'SF6_halocarbon': {'molarMass': 146.06, 'rho': 0.00052, 'tau': 3200.0},
    'carbon-cycle-solver': {'dt': 0.25,
                            'eps_abs': 1e-06,
                            'eps_rel': 1e-06,
                            'eps_spinup': 0.001},
    'core': {'do_spinup': True,
             'endDate': 2300,
             'max_spinup': 2000,
             'run_name': 'pyhector-run',
             'startDate': 1745},
    'forcing': {'baseyear': 1750},
    'halon1211_halocarbon': {'molarMass': 165.35, 'rho': 3e-05, 'tau': 16.0},
    'halon1301_halocarbon': {'molarMass': 148.9, 'rho': 0.00032, 'tau': 65.0},
    'halon2402_halocarbon': {'molarMass': 259.8, 'rho': 0.00033, 'tau': 20.0},
    'ocean': {'enabled': True,
              'k_max': 0.3,
              'k_min': 0.1,
              'slope': 1.0,
              'spinup_chem': 0,
              't_mid': 2.75,
              'tid': 200000000,
              'tt': 72000000,
              'tu': 49000000,
              'twi': 12500000},
    'onelineocean': {'enabled': True, 'ocean_c': 38000},
    'ozone': {'PO3': 30.0},
    'simpleNbox': {'Ftalbedo': [(1750, 0.0), (1950, -0.2)],
                   'atmos_c': 588.071,
                   'beta': 0.36,
                   'detritus_c': 55,
                   'f_litterd': 0.98,
                   'f_lucd': 0.01,
                   'f_lucv': 0.1,
                   'f_nppd': 0.6,
                   'f_nppv': 0.35,
                   'npp_flux0': 50.0,
                   'q10_rh': 2.0,
                   'soil_c': 1782,
                   'veg_c': 550},
    'so2': {'S0': 53841.2, 'SN': 42000},
    'temperature': {'S': 3.0}
}
