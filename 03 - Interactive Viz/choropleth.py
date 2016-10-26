import pandas as pd
import folium

def buildChoroplethMap (dataFrame, scale = [0, 500, 1000, 1500, 2000], outputFileName = 'switzerland_map'):
    
    if 'Granted Money' not in dataFrame.columns:
        raise ValueError ('The supplied data frame must contain a column named \"Granted Money\".')
    
    cantonsFrame = pd.read_csv ('cantons.csv')
    mapFrame = pd.merge (cantonsFrame, pd.DataFrame (dataFrame ['Granted Money']), left_index = True, right_index = True)
    
    cantons_data_path = 'ch-cantons.topojson.json'

    map_cantons = folium.Map (location = [46.8, 8.28], zoom_start = 8)
    map_cantons.choropleth (geo_path = cantons_data_path, data = mapFrame,
                             columns = ['Canton', 'Granted Money'],
                             threshold_scale = scale,
                             key_on = 'feature.id',
                             topojson = 'objects.cantons',
                             fill_color = 'YlOrBr', fill_opacity = 0.7, line_opacity = 0.2,
                             legend_name = 'Granted Money (Mio CHF)')
    
    map_cantons.save (outputFileName + '.html')