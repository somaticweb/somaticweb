from jinja2.ext import Extension

def micro_only(value):
    return [v for v in value if getattr(v, "micro", False)]

def macro_only(value):
    return [v for v in value if not getattr(v, "micro", False)]

class SwExtension(Extension):
    def __init__(self, environment):
        environment.filters["micro_only"] = micro_only
        environment.filters["macro_only"] = macro_only

myfilter = SwExtension
