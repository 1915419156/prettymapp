from osmnx.geometries import geometries_from_polygon
import geopandas as gpd

from prettiermaps import geo
from prettiermaps import plotting
from prettiermaps import dataclean
from prettiermaps.settings import LANDCOVER, DRAW_SETTINGS


def main():
    address = "Praça Ferreira do Amaral, Macau"
    radius = 1100

    # aoi = bbox_to_poly(*bbox_from_point(geocode(query=address), dist=radius)) # Might be faster
    aoi = geo.get_aoi_from_user_input(address=address, radius=radius)

    osm_tags = {}
    for element in LANDCOVER.values():
        for k, v in element.items():
            try:
                osm_tags.setdefault(k, []).extend(v)
            except TypeError:
                osm_tags[k] = v

    # TODO: Maybe independent queries that merge together, parallelized.
    # Or define all elements in query, and then
    df = geometries_from_polygon(polygon=aoi, tags=osm_tags)
    df = gpd.clip(df, aoi)

    df = dataclean.cleanup_df(df=df, landcover=LANDCOVER)
    df = geo.adjust_street_width(df=df)

    # df = df.dissolve(by="osm_type")

    ax = plotting.plot(df, drawing_kwargs=DRAW_SETTINGS)
    return ax
