class TargetMapping:
    def __init__(self):
        self.Covid = 0
        self.Normal = 1
    def to_dict(self):
        return self.__dict__
    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))
    
    
    