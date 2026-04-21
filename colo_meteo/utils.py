class where_clause:
    def __init__(self):
        self.clause = {
            "dates": None,   
            "region": None,     
            "codes": None,
        }
        self._custom_conditions = []  # Para condiciones adicionales
    
    def set_dates(self, start_date: str, end_date: str):
        """Set date range filter"""
        self.clause["dates"] = f"fechaobservacion >= '{start_date}' AND fechaobservacion <= '{end_date}'"
        return self
    
    def set_region(self, bbox):
        """Set geographic bounding box filter"""
        self.clause["region"] = (
            f"latitud >= {bbox.min_lat} AND latitud <= {bbox.max_lat} AND "
            f"longitud >= {bbox.min_lon} AND longitud <= {bbox.max_lon}"
        )
        return self
    
    def set_codes(self, codes: list):
        """Set station codes filter"""
        if codes:
            conditions = [f"codigoestacion = '{code}'" for code in codes]
            self.clause["codes"] = f"({' OR '.join(conditions)})"
        return self
    
    def add_condition(self, field: str, operator: str, value):
        """Add custom condition"""
        if isinstance(value, str):
            self._custom_conditions.append(f"{field} {operator} '{value}'")
        else:
            self._custom_conditions.append(f"{field} {operator} {value}")
        return self
    
    def get_clause(self) -> str:
        """Build complete WHERE clause"""
        conditions = []
        
        # Add main conditions
        for value in self.clause.values():
            if value:
                conditions.append(value)
        
        # Add custom conditions
        conditions.extend(self._custom_conditions)
        
        return " AND ".join(conditions) if conditions else ""
    
    def clear(self):
        """Reset all conditions"""
        self.clause = {k: None for k in self.clause}
        self._custom_conditions = []
        return self
    
    def __str__(self) -> str:
        return self.get_clause()

