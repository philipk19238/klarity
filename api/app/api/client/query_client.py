class QueryClient:

    def __init__(self, expected_params=None):
        self.expected_params = expected_params or set()
    
    def add_param(self, param):
        self.expected_params.add(param)

    def parse_request(self, request, subtarget=None):
        kwargs = request.args
        parsed = {}
        for k, v in kwargs.items():
            if k not in self.expected_params:
                continue
            if subtarget is None:
                parsed[k] = v
            else:
                parsed[subtarget + '.' + k] = v
        return parsed

    def query(self, model, **kwargs):
        res = []
        for dao in model.objects(__raw__ = kwargs):
            res.append(dao)
        return res

    

    
