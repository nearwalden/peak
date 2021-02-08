# analyze datasets

import files
import pandas as p


def merge_bmgf_un():
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
    return out


# compare
def compare_bmgf_un(start=2020, end=2100):
    df = merge_bmgf_un()
    df = df[(df.index >= start) & (df.index <= end)]
    out = p.DataFrame()
    out['peak'] = df.max()
    out['peak_year'] = df.idxmax()
    out['manyears'] = df.sum()/1000000000
    return out
