# prettymapp

Prettymapp is a webapp to create beautiful artsy maps from OpenStreetMap data.

The underlying Python package is a rewrite of the fantastic [prettymaps](https://github.com/marceloprates/prettymaps) 
project with focus on speed and fully integrated configuration to interface with the webapp. 
All credit for the original prettymaps idea, designs and implementation go to its author [@marceloprates]
(https://github.com/marceloprates). The prettymapp rewrite drops more complex configuration 
options in favour of improved speed, reduced code complexity and simplified configuration interfaces. 
It is fully tested and adds a [streamlit](https://streamlit.io/) webapp.

## Development
Interactive installation + changes in package require app restart.


## TODO
- Cleanup examples
- svg vs png display quality?
- Nördlingen, 136 radius just plots first example, maybe if geocoding doesnt work, same with miami

- ValueError: Nominatim could not geocode query "matthias-ehrenfried-str. 16, 97074 wuerzburg"
- if changing example, only values that are different in example definition are reset, e.g. contour color etc.