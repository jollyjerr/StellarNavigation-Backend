def formatToCytoscape(celestial):
    return {
        'data': {
            'id': celestial.id,
            'label': celestial.name
        },
        'position': {
            'x': 500,
            'y': (celestial.semi_major_axis*0.00001)
        },
        'style': {
            'width': (celestial.radius*0.001),
            'height': (celestial.radius*0.001),
            'color': 'yellow',
            'background-color': 'blue'
        }
    }
