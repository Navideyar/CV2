from compressor.filters.css_default import CssAbsoluteFilter
from compressor.filters.cssmin import CSSMinFilter
from compressor.filters.jsmin import JSMinFilter

class CustomCssAbsoluteFilter(CssAbsoluteFilter):
    def __init__(self, *args, **kwargs):
        super(CustomCssAbsoluteFilter, self).__init__(*args, **kwargs)
        self.url_patterns = self.url_patterns + (
            (r'url\([\'"]?([^\)\'"]*/static/[^\)\'"]*)[\'"]\)', r'url("%s\1")'),
        ) 