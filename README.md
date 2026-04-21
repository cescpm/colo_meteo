# colo_meteo

## Description

`colo_meteo` is a Python library that provides easy access to meteorological and hydrological data from IDEAM (Instituto de Hidrologia, Meteorologia y Estudios Ambientales) in Colombia. The library uses the Socrata Open Data API to query official datasets from www.datos.gov.co. 

In order to be able to use this library, registration in https://evergreen.data.socrata.com/ is required. So a token can be created and requests done.

## Features

- Query meteorological data (precipitation, temperature, humidity...)
- Filter by geographic region (bounding boxes)
- Filter by date ranges
- Filter by specific station codes
- Return data as pandas DataFrames or JSON
- Save metadata and query results

## Installation

### From GitHub (recommended)
```bash
pip install git+https://github.com/cescpm/colo_meteo.git
```
## Typical datasets
- s54a-sgyg: Precipitación
- sbwg-7ju4: Temperatura
- uext-mhny: Humedad relativa
