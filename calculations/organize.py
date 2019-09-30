def formatToCytoscape(celestial):
    return {
        'data': {
            'id': celestial.id,
            'label': celestial.name
        },
        'position': {
            'x': 300,
            'y': celestial.semi_major_axis / 1000
        }
    }