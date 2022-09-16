def Gender(us_mass_shooting):
    us_mass = us_mass_shooting.GENDER.value_counts().reset_index()
    us_mass.rename(columns={'index':'GENDER', 'GENDER':'Count of victims per Gender'}, inplace=True)
    return us_mass

def ShootingType(us_mass_shooting):
    shooting_type = us_mass_shooting.SHOOTINGTYPE.value_counts().reset_index()
    shooting_type.rename(columns={'index':'SHOOTINGTYPE', 'SHOOTINGTYPE':'Count of Victims per Shooting Type'}, inplace=True)
    return shooting_type

def Race(us_mass_shooting):
    us_mass_race = us_mass_shooting.RACE.value_counts().reset_index()
    us_mass_race.rename(columns={'index':'RACE', 'RACE':'Count of Victims per Race'}, inplace=True)
    return us_mass_race

def State(us_mass_shooting):
    us_mass_state = us_mass_shooting.STATE.value_counts().reset_index()
    us_mass_state.rename(columns={'index':'STATE', 'STATE':'Count of Victims Per State'}, inplace=True)
    return us_mass_state

def Year(us_mass_shooting):
    year = us_mass_shooting.YEAR.value_counts().reset_index()
    year.rename(columns={'index':'Year', 'YEAR':'Count of Victims per Year'}, inplace=True)
    return year

def Summary(us_mass_shooting):
    us_mass_summary = us_mass_shooting.SUMMARY.unique()
    return us_mass_summary

def MentalHealthSources(us_mass_shooting):
    us_mass_mentalsources = us_mass_shooting.MENTALHEALTHSOURCES.unique()
    return us_mass_mentalsources

def InfoSources(us_mass_shooting):
    us_mass_infosources = us_mass_shooting.SOURCES.unique()
    return us_mass_infosources

def Weapons(us_mass_shooting):
    us_mass_weapons = us_mass_shooting.WEAPONDETAILS.unique()
    return us_mass_weapons

def Assault(us_mass_shooting):
    us_mass_assault = us_mass_shooting.ASSAULT.value_counts().reset_index()
    us_mass_assault.rename(columns={'index':'ASSAULT', 'ASSAULT':'Count of Assaulted Victims'}, inplace=True)
    return us_mass_assault

def NumberOfWeapons(us_mass_shooting):
    us_mass_numweapons = us_mass_shooting.NUMWEAPONS.value_counts().reset_index()
    us_mass_numweapons.rename(columns={'index':'Number of Weapons', 'NUMWEAPONS':'assaulted victims'}, inplace=True)
    return us_mass_numweapons

def TypesOfWeapons(us_mass_shooting):
    us_mass_typesofweapons = us_mass_shooting.TYPEOFWEAPONS.unique()
    return us_mass_typesofweapons

def WeaponsObtained(us_mass_shooting):
    us_mass_weaponsobtained = us_mass_shooting.WHEREWEAPONOBTAINED.unique()
    return us_mass_weaponsobtained

def WeaponsObtainedLegally(us_mass_shooting):
    weapons_obtained_legally = us_mass_shooting.WEAPONSOBTAINEDLEGALLY.value_counts().reset_index()
    weapons_obtained_legally.rename(columns={'index':'weapons obtained legally', 'WEAPONSOBTAINEDLEGALLY':'Count of Weapons Obtained Legally'}, inplace=True)
    return weapons_obtained_legally

def MentalNotes(us_mass_shooting):
    us_mass_shooting_mentalNotes = us_mass_shooting.MENTALHEALTHNOTES.unique()
    return us_mass_shooting_mentalNotes

def PriorSignsOfMentalIllness(us_mass_shooting):
    prior_signs = us_mass_shooting.PRIORSIGNSOFMENTALILLNESS.value_counts().reset_index()
    prior_signs.rename(columns={'index':'Prior Signs of Mental Illness', 'PRIORSIGNSOFMENTALILLNESS':'Count of how many people showed Prior Signs of Mental Illness'}, inplace=True)
    return prior_signs

def LocationType(us_mass_shooting):
    us_mass_location = us_mass_shooting.LOCATIONTYPE.value_counts().reset_index()
    us_mass_location.rename(columns={'index':'Location Type', 'LOCATIONTYPE':'Count of Victims per Location'}, inplace=True)
    return us_mass_location

def Case(us_mass_shooting):
    case = us_mass_shooting.CASE.unique()
    return case

def GenderFatalities(us_mass_shooting):
    us_mass_gender_fatalities = us_mass_shooting.groupby('GENDER')[['FATALITIES']].sum().sort_values('FATALITIES', ascending=False).reset_index()
    return us_mass_gender_fatalities

def ShootingTypePerPRIORSIGNSOFMENTALILLNESS(us_mass_shooting):
    prior_signs_shooting_type = us_mass_shooting.groupby('SHOOTINGTYPE')['PRIORSIGNSOFMENTALILLNESS'].size().reset_index()
    return prior_signs_shooting_type