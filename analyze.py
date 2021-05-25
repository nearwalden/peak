# analyze datasets

import files
import pandas as p


# merge all global
def merge_all():
    out = p.DataFrame()
    bmgf_ds = 'bmgf_population'
    bmgf_coll = 'global_pop'
    for val in files.get_coll_vals(bmgf_ds, bmgf_coll):
        df = p.read_csv(files.get_coll_file_path(bmgf_ds, bmgf_coll, val))
        df = df.set_index('year')
        out['BMGF-' + val] = df['population']
    un_ds = 'un_population'
    un_coll = 'global_pop'
    for val in files.get_coll_vals(un_ds, un_coll):
        df = p.read_csv(files.get_coll_file_path(un_ds, un_coll, val))
        df = df.set_index('year')
        out['UN-' + val] = df['population']
    witt_ds = 'witt_population'
    witt_coll = 'global_pop'
    for val in files.get_coll_vals(witt_ds, witt_coll):
        df = p.read_csv(files.get_coll_file_path(witt_ds, witt_coll, val))
        df = df.set_index('year')
        out['Witt-' + str(val)] = df['population']
    return out


# compare global
def compare_all(start=2020, end=2100):
    df = merge_all()
    df = df[(df.index >= start) & (df.index <= end)]
    out = p.DataFrame()
    out['peak'] = df.max()
    out['peak_year'] = df.idxmax()
    out['manyears'] = df.sum()/1000000000
    out['mean'] = df.mean()
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
    un_ds = 'un_population'
    un_coll = 'country_pop'
    for val in files.get_coll_vals(un_ds, un_coll):
        df = p.read_csv(files.get_coll_file_path(un_ds, un_coll, val))
        df = df.set_index('year')
        out['UN-' + val] = df[country]
    witt_ds = 'witt_population'
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
