import rioxarray
import xarray as xr
import geopandas as gpd
from xarray import Dataset

def preparar_para_recorte(dataset:Dataset, crs="epsg:4326", xdim="lon", ydim="lat") -> Dataset:
    """Sub-função de main().
    Ajusta coordenadas e dados para o recorte da chuva.

    Args:
        dataset (Dataset): Dado a ser recortado pelo shapefile
        crs (str, optional): Projeção cartográfica. Defaults to "epsg:4326".
        xdim (str, optional): Nome da dimensão "longitude" no dataset. Defaults to "lon".
        ydim (str, optional): Nome da dimensão "latitude" no dataset. Defaults to "lat".

    Returns:
        Dataset: Dados tratados para recorte
    """
    dataset = dataset.assign_coords(lon=(((dataset.lon + 180) % 360) - 180)).sortby(xdim)
    dataset = dataset.rio.set_spatial_dims(x_dim=xdim, y_dim=ydim) 
    dataset = dataset.rio.write_crs(crs)
    return dataset


def main(dataset:str,shapefile:str) -> Dataset:
    """Recorta dado de chuva do MERGE a partir de um dado de contorno

    Args:
        dataset (str): dado merge convertido para nc.
        shapefile (str): arquivo .shp

    Returns:
        Dataset: Dado recortado
    """
    shp_bacia = gpd.read_file(shapefile)
    #leitura, preparação e recorte dos dados
    dados = xr.open_dataset(dataset)
    dados_preparados = preparar_para_recorte(dados.prec)
    dados_recortados = dados_preparados.rio.clip(shp_bacia["geometry"], "epsg:4326")

    return dados_recortados