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
    df = p.read_csv(files.get_file_path('bmgf_population', 'pop_data'))
    return df['location_name'].unique()


def witt_locations():
    df = p.read_csv(files.get_file_path('witt_population', 'recode'))
    datadf = p.read_csv(files.get_coll_file_path('witt_population', "all_pop", 1))
    dfl = df[df['dim'] == 'isono'].copy()
    out = []
    for i, row in dfl.iterrows():
        count = len(datadf[datadf['isono'] == row['code']])
        if count > 0:
            out.append({'name': row['name'], 'code': row['code']})
    outdf = p.DataFrame(out)
    return outdf


def un_locations():
    df = p.read_csv(files.get_coll_file_path('un_population', 'all_pop', 'high'))
    dfg = df.groupby('Region')
    outdf = p.DataFrame()
    outdf = dfg.first()
    outdf = outdf.reset_index()
    return outdf   #  outdf[outdf['Type'] == 'Country/Area'].copy()


def un_country_names():
    df = un_locations()
    return df[df.Type == 'Country/Area']['Region'].to_list()


def un_region_names():
    df = un_locations()
    return df[df.Type == 'Region']['Region'].to_list()


def un_subregion_names():
    df = un_locations()
    return df[df.Type == 'Subregion']['Region'].to_list()


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


# retunrs a list of common countries
def countries():
    uc = un_country_names()
    b = bmgf_location_names()
    w = witt_locations()['name'].to_list()
    common = list(set(uc).intersection(set(b), set(w)))
    return common


# get UN isono from country name
def country_code(country):
    df = p.read_csv(files.get_file_path('witt_population', 'recode'))
    df = df.set_index('name')
    return df.loc[country]['code']


# retunrs a list of common regions (none!)
def regions():
    uc = un_region_names()
    b = bmgf_location_names()
    w = witt_locations()['name'].to_list()
    common = set(uc).intersection(set(b), set(w))
    return list(common)


# returns a list of common subregions (only a couple!)
def subregions():
    uc = un_subregion_names()
    b = bmgf_location_names()
    w = witt_locations()['name'].to_list()
    common = set(uc).intersection(set(b), set(w))
    return list(common)

