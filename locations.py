# normalize locations

# from prefect import task, Flow
# from atlas import data
import pandas as p
import files

WORLD_NAMES = {
    'bmgf': 'Global',
    'un': 'WORLD',
    'witt': 'WORLD'
    }


def bmgf_location_names():
    df = p.read_csv(files.get_path('bmgf_population', 'pop_data'))
    return df['location_name'].unique()


def witt_locations():
    df = p.read_csv(files.get_path('witt_population', 'recode'))
    dfl = df[df['dim'] == 'isono'].copy()
    return dfl.drop('dim', axis=1)


def un_locations():
    df = p.read_csv(files.get_path('un_population', 'high_variant'))
    dfg = df.groupby('Region')
    outdf = p.DataFrame()
    outdf = dfg.first()
    outdf = outdf.reset_index()
    return outdf   #  outdf[outdf['Type'] == 'Country/Area'].copy()


def compare_names(names, dataset, un):
    not1 = []
    only1 = []
    both = []
    un_list = un['Region'].to_list()
    for item in names:
        if item in un_list:
            both.append(item)
        else:
            only1.append(item)
    for item in un_list:
        if item not in names:
            not1.append(item)
    out = {dataset: only1,
            'un': not1,
            'both': both
        }
    return out


def compare_all_names(b, w, u):
    bu = compare_names(b, 'bmgf', u)
    wu = compare_names(w['name'].to_list(), 'witt', u)
    print("BU = " + str(len(bu['both'])) + ", WU = " + str(len(wu['both'])))
    all_len = 0
    for item in bu['both']:
        if item in wu['both']:
            all_len += 1
    print("All = " + str(all_len))


def compare_numbers(witt, un):
    not1 = []
    only1 = []
    both = []
    un_list = un['Country code'].to_list()
    witt_list = witt['code'].to_list()
    for item in witt_list:
        if item in un_list:
            both.append(item)
        else:
            only1.append(item)
    for item in un['Country code']:
        if item not in witt['code']:
            not1.append(item)
    out = {'witt': only1,
            'un': not1,
            'both': both
    }
    return out


