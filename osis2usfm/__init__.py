"""Package init file for converting OSIS references to USFM."""

BOOKS = {
    'exod': 'EXO',
    'deut': 'DEU',
    'josh': 'JOS',
    'judg': 'JDG',
    'ruth': 'RUT',
    '1sam': '1SA',
    '2sam': '2SA',
    '1kgs': '1KI',
    '2kgs': '2KI',
    '1chr': '1CH',
    '2chr': '2CH',
    'ezra': 'EZR',
    'esth': 'EST',
    'ps': 'PSA',
    'prov': 'PRO',
    'eccl': 'ECC',
    'song': 'SNG',
    'ezek': 'EZK',
    'joel': 'JOL',
    'amos': 'AMO',
    'obad': 'OBA',
    'jonah': 'JON',
    'nah': 'NAM',
    'zeph': 'ZEP',
    'zech': 'ZEC',
    'matt': 'MAT',
    'mark': 'MRK',
    'luke': 'LUK',
    'john': 'JHN',
    'acts': 'ACT',
    '1cor': '1CO',
    '2cor': '2CO',
    'phil': 'PHP',
    '1thess': '1TH',
    '2thess': '2TH',
    '1tim': '1TI',
    '2tim': '2TI',
    'titus': 'TIT',
    'phlm': 'PHM',
    '1pet': '1PE',
    '2pet': '2PE',
    '1john': '1JN',
    '2john': '2JN',
    '3john': '3JN',
    'jude': 'JUD',
    # apocrypha
    'esthgr': 'ESG',
    'epjer': 'LJE',
    'prazar': 'S3Y',
    '1macc': '1MA',
    '2macc': '2MA',
    '3macc': '3MA',
    '4macc': '4MA',
    '1esd': '1ES',
    '2esd': '2ES',
    'prman': 'MAN',
    'addps': 'PS2',
    'odes': 'ODA',
    'psssol': 'PSS',
    '4ezra': 'EZA',
    '5ezra': '5EZ',
    '6ezra': '6EZ',
    'dangr': 'DAG',
    '5apocsyrpss': 'PS3',
    '2bar': '2BA',
    'epbar': 'LBA',
    '1en': 'ENO',
    '1meq': '1MQ',
    '2meq': '2MQ',
    '3meq': '3MQ',
    'reproof': 'REP',
    '4bar': '4BA',
    'eplao': 'LAO',

    # etc
    'front': 'FRT',
    'introduction': 'INT',
    'back': 'BAK',
    'concordance': 'CNC',
    'glossary': 'GLO',
    'index': 'TDX',
    'gazetteer': 'NDX',
    'x-other': 'OTH'
}


def convert(osis_refs):
    """Convert each OSIS ref in the list to a USFM ref.

    *Note*: This method doesn't validate any references. It simply takes a map of books that are
    different between OSIS & USFM and converts them.
    """
    is_string = False
    if isinstance(osis_refs, str):
        osis_refs = [osis_refs]
        is_string = True

    usfm_refs = []

    for ref in osis_refs:
        parts = ref.split('.')

        # If the book part is different, convert otherwise just uppercase it
        if parts[0].lower() in BOOKS.keys():
            parts[0] = BOOKS[parts[0].lower()]
        else:
            parts[0] = parts[0].upper()

        usfm_refs.append('.'.join(parts))

    return usfm_refs if is_string is False else usfm_refs[0]
