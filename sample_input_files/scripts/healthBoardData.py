


healthBoardIdToName = {
"S08000015":"NHS Ayrshire and Arran",
"S08000016":"NHS Borders",
"S08000017":"NHS Dumfries and Galloway",
"S08000019":"NHS Forth Valley",
"S08000020":"NHS Grampian",
"S08000022":"NHS Highland",
"S08000024":"NHS Lothian",
"S08000025":"NHS Orkney",
"S08000026":"NHS Shetland",
"S08000028":"NHS Western Isles",
"S08000029":"NHS Fife",
"S08000030":"NHS Tayside",
"S08000031":"NHS Greater Glasgow and Clyde",
"S08000032":"NHS Lanarkshire"}


# Link between Health Board and Local Authorities  (https://en.wikipedia.org/wiki/Subdivisions_of_Scotland#Health)
healthBoardsAndLocalAuthoriesMap = {
"Ayrshire and Arran" : ["East Ayrshire","North Ayrshire","South Ayrshire"],
"Borders" : ["Scottish Borders"],
"Dumfries and Galloway" : ["Dumfries and Galloway"],
"Fife" : ["Fife"],
"Forth Valley" : ["Clackmannanshire", "Falkirk", "Stirling"],
"Grampian" : ["Aberdeenshire", "City of Aberdeen", "Moray"],
"Greater Glasgow and Clyde" : ["City of Glasgow", "East Dunbartonshire", "East Renfrewshire", "Inverclyde", "Renfrewshire", "West Dunbartonshire"],
"Highland" : ["Argyll and Bute", "Highland"],
"Lanarkshire" : ["North Lanarkshire", "South Lanarkshire"],
"Lothian" : ["City of Edinburgh", "East Lothian", "Midlothian", "West Lothian"],
"Orkney" : ["Orkney Islands"],
"Shetland" : ["Shetland Islands"],
"Tayside" : ["Angus", "City of Dundee", "Perth and Kinross"],
"Western Isles" : ["Western Isles (Na h-Eileanan Siar)"]
}

# the names of the local authority in the spreadsheets downloaded from NRS do 
# not match the names we have in the healthBoardId and 
# healthBoardsAndLocalAuthoriesMap dictionaries. 
# Here we define the transformations
authority_name_map = { 
"Aberdeen City" : "City of Aberdeen",
"Argyll & Bute" : "Argyll and Bute",
"Dumfries & Galloway" : "Dumfries and Galloway",
"Dundee City" : "City of Dundee",
"East Lothian(2)" : "East Lothian",
"Edinburgh, City of":"City of Edinburgh",
"Na h-Eileanan Siar" : "Western Isles (Na h-Eileanan Siar)",
"Glasgow City" : "City of Glasgow",
"Perth & Kinross" : "Perth and Kinross"}


def getLocalAuthorityName(la_name, mapping=authority_name_map):
    """
    Sometimes the name of a local authority does not match up with the name
    in the health boards to authority map, here we take a local authority name
    and transform it according to the transformation dict and return the 
    'correct' local authority name.
    :param: la_name the name of the local authority (str)
    :param: mapping a dict{str:str} of possible local authotiy name to correct name.
    """
    if la_name in authority_name_map.keys():
        return authority_name_map[la_name]
    else:
        return la_name



# The following data structures provide a quick and easy way of looking up
# the values in these dicts.
healthBoardNameToId = {}
LocalAuthorityToHealthBoardNameMap = {}
LocalAuthorityToHealthBoardIdMap = {}

cached = False
if cached == False:
    print("Creating caches")
    # create the datastructes that need to be cached
    for hbid, hbname in healthBoardIdToName.items():
        healthBoardNameToId[hbname] = hbid
        healthBoardNameToId[hbname.replace('NHS ', '')] = hbid

    for hbname, laList in healthBoardsAndLocalAuthoriesMap.items():
        for laname in laList:
            # put both the correct (i.e the LA name as it appears in the 
            # wikipedia data) and the one that appears in the NRS data
            # so there is as little conversion needed as possibble when
            # using this dict.
            LocalAuthorityToHealthBoardNameMap[laname] = hbname
            LocalAuthorityToHealthBoardIdMap[laname] = healthBoardNameToId[hbname]
            for nrs_name, wiki_name in authority_name_map.items():
                if wiki_name == laname:
                    LocalAuthorityToHealthBoardNameMap[nrs_name] = hbname
                    LocalAuthorityToHealthBoardIdMap[nrs_name] = healthBoardNameToId[hbname]


    cached = True
    print("\b\b...done")


