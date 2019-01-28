def seasonId(season):

    switch = {
            0:  'PREASEASON 3',
            1:  'SEASON 3',
            2:  'PRESEASON 4',
            3:  'SEASON 4',
            4:  'PRESEASON 5',
            5:  'SEASON 5',
            6:  'PRESEASON 6',
            7:  'SEASON 6',
            8:  'PRESEASON 7',
            9:  'SEASON 7',
            10: 'PRESEASON 8',
            11: 'SEASON 8'
    }
    return switch.get(season)
