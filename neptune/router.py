class NRouter(object):
    """
    The URL route handling class

    Rule is defined as:
        [
            { 'route': '/', 'class': 'cname' },
            { 'route': '/b/:id', 'class': 'cname' },
            { 'route': '/home', 'class': 'cname' },
        ]
    """

    # TODO Add Validator for rules
    # TODO Decide whether regex or not, route priority etc.

    def __init__(self, rules=[]):
        self.rules = rules

    def add_rule(self, route, cls):
        self.rules.append(
            {'route': route, 'class': cls})

    def get_cls(self, route):
        # TODO Fix it 
        for a in self.rules:
            if a['route'] == route:
                return a['class']()
        return '404'
