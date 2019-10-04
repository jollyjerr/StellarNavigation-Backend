# Stellar Navigation
*A web application for exploring the stars.*
![intro](https://github.com/jollyjerr/StellarNavigation-Backend/blob/master/GitHubFiles/intro.gif)

Stellar Navigation is a web application for displaying and navigating multiple stellar systems at scale.
This exciting project was developed during a single week of my time at Flatiron School using these fantastic technologies:

##### [Backend](https://github.com/jollyjerr/StellarNavigation-Backend)
- Python
- Flask
- SqlAlchamy
- Marshmellow
##### [Frontend](https://github.com/jollyjerr/StellarNavigation-Frontend)
- React.js
- React-Router
- Cytoscape.js
- React-Cytoscape
- HTML Canvas

... and more!

*This README is specific to the projects backend, for the frontend README, see [here](https://github.com/jollyjerr/StellarNavigation-Frontend)*

## Features

This RESTful API was developed using Python and Flask - both of which were new technologies to me at the start of the project.

Flask-SqlAlchamy, Flask-Marshmellow, and Flask-Migrate were all used to make the API reliable and scaleable.
Additional stellar systems could easily be added - and the backend and frontend were designed to adapt immediately to any new
planets, stars, comets, or full stellar systems.

This backend provides the frontend with accurate mapping data for the Canvas graph display. Because Python handles numbers 
more eloquently than JS, running calculations in this system and sending the results to the frontend achieves a level of accuracy
not achievable with Node.js.

After receiving a calculation request from the frontend, this API calculates the distance and time involved in the requested
intergalactic journey. In an updated release, I hope to incorporate the wonderful [Poliastro](https://pypi.org/project/poliastro/)
library to calculate accurate orbital animations and valid Hohmann transfers between bodies.

![calculations](https://github.com/jollyjerr/StellarNavigation-Backend/blob/master/GitHubFiles/calculate.gif)


## Contributing
Feel free to open pull requests or report any bugs!

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
