# analyze datasets

import modelmgr
import files
import pandas as p

# compare global
def compare_all(start=2025, end=2100):
    df = p.read_csv(files.get_global_all_path())
    df.set_index('year', inplace=True)
    df = df[(df.index >= start) & (df.index <= end)]
    out = p.DataFrame()
    out['peak'] = df.max()
    out['peak_year'] = df.idxmax()
    out['manyears'] = df.sum()/1000000000
    out['mean'] = df.mean()
    out['2025'] = df.loc[2025]
    out['2050'] = df.loc[2050]
    out['2075'] = df.loc[2075]
    out['2100'] = df.loc[2100]            
    return out


# country versions
def merge_all_country(country):
    out = p.DataFrame()
    bmgf_ds = 'bmgf_population'
    bmgf_coll = 'country_pop'
    for val in files.get_coll_vals(bmgf_ds, bmgf_coll):
        df = p.read_csv(files.get_coll_file_path(bmgf_ds, bmgf_coll, val))
        df = df.set_index('year')
        out['BMGF-' + val] = df[country]
    un2019_ds = 'un_population_2019'
    un2019_coll = 'country_pop'
    for val in files.get_coll_vals(un2019_ds, un2019_coll):
        df = p.read_csv(files.get_coll_file_path(un2019_ds, un2019_coll, val))
        df = df.set_index('year')
        out['UN2019-' + val] = df[country]
    un2022_ds = 'un_population_2022'
    un2022_coll = 'country_pop'
    for val in files.get_coll_vals(un2022_ds, un2022_coll):
        df = p.read_csv(files.get_coll_file_path(un2022_ds, un2022_coll, val))
        df = df.set_index('year')
        out['UN2022-' + val] = df[country]
    witt_ds = 'witt_population-2019'
    witt_coll = 'country_pop'
    for val in files.get_coll_vals(witt_ds, witt_coll):
        df = p.read_csv(files.get_coll_file_path(witt_ds, witt_coll, val))
        df = df.set_index('year')
        out['Witt-' + str(val)] = df[country]
    return out


# compare
def compare_all_country(country, start=2020, end=2100):
    df = merge_all_country(country)
    df = df[(df.index >= start) & (df.index <= end)]
    out = p.DataFrame()
    out['peak'] = df.max()
    out['peak_year'] = df.idxmax()
    out['man-years'] = df.sum()/1000000000
    out['mean'] = df.mean()
    return out
