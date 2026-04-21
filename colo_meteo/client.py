from sodapy import Socrata
import json
import pandas as pd
from pathlib import Path

class ColombianWeatherClient:
    ### Build ###
    def __init__(self,
                 token: str = None,
                 dataset_id: str = None,
                 select: str = None,
                 where_clause: str = None,
                 limit: int = None):
        """
        Initialize Socrata client for datos.gov.co
        """
        self.client = Socrata("www.datos.gov.co", token)
        self.dataset_id = dataset_id
        self.select = select
        self.where = where_clause
        self.limit = limit  # s'ha d'ajustar segons el volum de dades que demanem

    
    def set_dataset(self,
                    dataset_id: str):
        """
        Change the active dataset
        """
        self.dataset_id = dataset_id
        return self
    
    def set_limit(self,
                  limit: int):
        """
        Establishes a new limit
        """
        self.limit = limit
        return self

    def set_clause(self,
                  where_clause: int):
        """
        Sets the clause which data need to meet to be called
        """
        self.where = where_clause
        return self
    
    def select_columns(self,
                       columns: str):
        """
        Select the data variables for retrieving
        """
        self.select = columns
        return self

    ### Metadata ###

    def meta_datasets(self,
                      directory: str = "metadata",
                      metadata_level: str = "minimal"):
        """
        Creates a json file with the all meteorollogical datasets' metadata.
        For a more user-friendly way of knowing from which dataset retrieve 
        the desired data.

        -----------
        Parameters:

        directory: str = "data"
            Directory where to create the json file

        full_metada: bool = False
            If full, all the metadata available in the api is written in the json file.
            If minimal, a minimal version of the metadata is provided.
        """

        Path(f"{directory}").mkdir(parents=True, exist_ok=True)

        datasets = self.client.datasets()

        meta=[]
        if metadata_level == "full":
            for dataset in datasets:
                if dataset.get('owner').get('id') == "xac7-ivuv":  # "determina" els datsets meteorològics

                    meta.append(dataset)
            
            with open("datasets_meta_full.json", "w", encoding="utf-8") as f:
                json.dump(
                    meta,
                    f,
                    ensure_ascii = False,
                    indent       = 4,
                )

        elif metadata_level == "minimal":
            for dataset in datasets:
                if dataset.get('owner').get('id') == "xac7-ivuv":

                    minimal_meta = {
                        'name'  : dataset.get('resource').get('name'),
                        'id'    : dataset.get('resource').get('id'),
                        'owner' : dataset.get('owner'),
                        }
                    meta.append(minimal_meta)
                    
            with open("datasets_meta_mimnimal.json", "w", encoding="utf-8") as f:
                json.dump(
                    meta,
                    f,
                    ensure_ascii = False,
                    indent       = 4,
                )

    def meta(self,
             directory: str = "metadata",
             metadata_level: str = "minimal"):
        """
        Creates a json file with the chosen meteorollogical dataset's metadata.
        For a more user-friendly way of knowing what the current dataset contains. 

        -----------
        Parameters:

        directory: str = "data"
            Directory where to create the json file

        full_metada: bool = False
            If full, all the metadata available in the api is written in the json file.
            If minimal, a minimal version of the metadata is provided.
        """

        Path(f"{directory}").mkdir(parents=True, exist_ok=True)

        id = self.dataset_id
        meta = self.client.get_metadata(id)

        if metadata_level == "full":
            with open(f"{directory}/{id}_meta_full.json", "w", encoding="utf-8") as f:
                json.dump(
                    meta,
                    f,
                    ensure_ascii = False,
                    indent       = 4,
                )

        elif metadata_level == "minimal":
            with open(f"{directory}/{id}_meta_minimal.json", "w", encoding="utf-8") as f:
                json.dump(
                    {
                        'name'    : meta.get('name'),
                        'id'      : meta.get('id'),
                        'columns' : [column.get('name') for column in meta.get('columns')],
                    },
                    f,
                    ensure_ascii  = False,
                    indent        = 4,
                )

    ### Access data ###

    def get_data(self,
                 to_dataframe: bool = True) -> pd.DataFrame | list:
        """
        Retrieves the data.

        -----------
        Parameters:

        to_dataframe: bool = True
            Whether to return data as a pd.DataFrame or a list

        --------
        Returns:

        df | query: pd.DataFrame | list
            Contains the data
        """

        query = self.client.get(
            dataset_identifier = self.dataset_id,
            select             = self.select,
            where              = self.where,
            limit              = self.limit,
        )

        if to_dataframe:
            df = pd.DataFrame.from_records(query)
            return df
        else:
            return query
        
    ## Close connection ###

    def close(self):
        """Close the client connection"""
        self.client.close()