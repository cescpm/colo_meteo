# Building of the where clause for querying data from datos.gov.co
# Not needed to know the required sintaxi for requesting data

class where_clause:
    def __init__(self):
        self.clause = {
            "dates": None,   
            "region": None,     
            "codes": None,
        }
        self._custom_conditions = []  # Para condiciones adicionales
    
    ### clauses ###
    def set_dates(self,
                  start_date: str,
                  end_date: str):
        """
        Set date range filter. 

            |------------------------------|
        start_date                      end_date

        When used in a request, the API will only return the observations whose dates
        fall inside the the time-range defined by the user.

        -----------
        Parameters:

        start_date: str
            date of the time-interval starting (included)

        end_date: str
            date of the time-interval ending (not included)
        """

        self.clause["dates"] = f"fechaobservacion >= '{start_date}' AND fechaobservacion <= '{end_date}'"
        return self
    
    def set_region(self,
                   bbox):
        """
        Set geographic bounding box filter.
        This function requires a prior colo_meteo.fence.BoundingBox object
        to be build.

                     ______________(max lat/lon)
                     |             |
                     |             |
                     |             |
                     |             |
        (min lat/lon)|_____________|

        When used in a request, the API will only return the observations whose coordinates
        fall inside the the region defined by the user.

        -----------
        Parameters:
        
        bbox
            Custom python object
            Contains the maximum and minimum latitudes and longitudes of a chosen square
        """
        self.clause["region"] = (
            f"latitud >= {bbox.min_lat} AND latitud <= {bbox.max_lat} AND "
            f"longitud >= {bbox.min_lon} AND longitud <= {bbox.max_lon}"
        )
        return self
    
    def set_codes(self,
                  codes: list):
        """
        Set station codes filter

        When used in a request, the API will only return the observations whose station code
        match one of the ones in the defined-by-the-user list.
        -----------
        Parameters:

        codes: list
            Contains the codes of the station desired to be retrieved
        """
        if codes:
            conditions = [f"codigoestacion = '{code}'" for code in codes]
            self.clause["codes"] = f"({' OR '.join(conditions)})"
        return self
    
    def add_condition(self,
                      field: str,
                      operator: str,
                      value):
        """
        Add custom condition

        Once studied the content (variables) of the dataset, 
        user can try to define a condition
        """
        if isinstance(value, str):
            self._custom_conditions.append(f"{field} {operator} '{value}'")
        else:
            self._custom_conditions.append(f"{field} {operator} {value}")
        return self
    
    ### exporting ###
    def get_clause(self) -> str:
        """
        Build complete clause and returns it as a ready-to-use where argument
        """
        conditions = []
        
        # Add main conditions
        for value in self.clause.values():
            if value:
                conditions.append(value)
        
        # Add custom conditions
        conditions.extend(self._custom_conditions)
        
        return " AND ".join(conditions) if conditions else ""
    
    ### Restoring to default ###
    def clear(self):
        """
        Reset all conditions
        """
        self.clause = {k: None for k in self.clause}
        self._custom_conditions = []
        return self
    
    ### visualization ###
    def __str__(self) -> str:
        return self.get_clause()

