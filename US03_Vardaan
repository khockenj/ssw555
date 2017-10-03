import datetime

def birthBeforeDeath(data):
    errorEntriesList = [ ]
    for id , entry in data[ 'INDI' ].items ( ):
        if 'BIRT' in entry and 'DEAT' in entry:
            if entry[ 'BIRT' ][ 'DATE' ][ 'VAL' ] > entry[ 'DEAT' ][ 'DATE' ][ 'VAL' ]:
                errorEntriesList.append ( (id , entry) )
    if errorEntriesList != [ ]:
        errorEntriesList.sort ( key=lambda x: int ( x[ 0 ].replace ( '@' , "" ).replace ( 'I' , "" ) ) )
        outputErrors = '';
        for id , entry in errorEntriesList:
            outputErrors += '\nError: US03: birth of a person ' + id + ' seems to occur after death'
            # outputErrors += '\n'
    else:
        outputErrors = ''
    return outputErrors
