class where_clause:
    def __init__(self):
        self.clause = {
            "dates"  : None,   
            "region" : None,     
            "code"   : None,
            }
    
    def set_dates(self,
                  data_ini: str,
                  data_fi: str):
        """
        Creates the clause for temporal restriction
        """
        self.clause["dates"] = f"fechaobservacion <= '{data_ini}' AND fechaobservacion > '{data_fi}'"

    def set_latitude(self,
                     bbox):
        """
        Creates de clause for geographical filter
        """
        self.clause["region"] = f"latitud < '{bbox.min_lat}' AND latitud > '{bbox.max_lat}' AND longitud < '{bbox.min_lon}' AND longitud > '{bbox.max_lon}'"

    def set_region(self,
                     codes: list):
        """
        Creates de clause for choosing data from explicitly specified stations.
        This function is actually under development can raise errors. Currently is
        preferred to download all data and obtain the data from the desired station 
        in post-process.
        """

        clause=[]
        for code in codes:
            clause.append(f"AND")
            clause.append(f"codigoestacion == '{code}")

        self.clause["code"] = f"".join(clause)

    