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

    def __init__(self, rules=None):
        self.rules = rules

    def add_rule(self, route, cls):
        self.rules.append(
            {'route': route, 'class': cls})
