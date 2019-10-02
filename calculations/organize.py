def formatToCytoscape(celestial):
    nodeList = []

    axis = (celestial.semi_major_axis*0.00001)
    width = (celestial.radius*0.001)
    height = (celestial.radius*0.001)

    for key in celestial.smallCelestials:
        nodeList.append(formatSmall(key, axis))

    nodeList.append({
        'data': {
            'id': celestial.id,
            'label': celestial.name
        },
        'position': {
            'x': 500,
            'y': axis
        },
        'style': {
            'width': width,
            'height': height,
            'color': 'yellow',
            'background-color': celestial.color
        }
    })
    return nodeList

def formatSmall(small, axis):
    return {
        'data': {
            'id': small.id * 500,
            'label': small.name
        },
        'position': {
            'x': (small.semi_major_axis*0.0001) + 500,
            'y': (small.semi_major_axis*0.0001) + axis
        },
        'style': {
            'width': (small.radius*0.001),
            'height': (small.radius*0.001),
            'color': 'yellow',
            'background-color': small.color
        }
    }
