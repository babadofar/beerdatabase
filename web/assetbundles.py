from flask.ext.assets import Bundle

from web import app

from react import jsx

transformer = jsx.JSXTransformer()


def react_filter(_in, out, **kw):
    out.write(transformer.transform_string(_in.read()))


js_filters = []
css_filters = []

minify = not app.debug

react = 'js/lib/react/react.js'
react_dom = 'js/lib/react/react-dom.js'

if minify:
    # Use jsmin and cssmin when not running in debug
    js_filters.append('jsmin')
    css_filters.append('cssmin')
    react = 'js/lib/react/react.min.js'
    react_dom = Bundle()

css_base = Bundle(
    'js/lib/fontawesome/css/font-awesome.css',
    Bundle(
        'js/lib/skeleton/css/normalize.css',
        'js/lib/skeleton/css/skeleton.css',
        'css/base.css',
        'css/auocomplete.css',
        filters=css_filters
    ),
    filters=['cssrewrite'],
    output='gen/css_base.css'
)


js_beer_list = Bundle(
    'js/lib/underscore/underscore-min.js',
    react,
    react_dom,
    Bundle(
        'js/lib/atomic-fixed.js',
        'js/src/util.js',
        'js/src/api.js',
        'js/src/Autocomplete.jsx',
        'js/src/SortableTable.jsx',
        'js/src/BreweryTable.jsx',
        'js/src/PolBeerTable.jsx',
        'js/src/BeerOverview.jsx',
        'js/src/StyleList.jsx',
        'js/src/BeerFixer.jsx',
        'js/src/PolShopOverview.jsx',
        filters=js_filters
    ),
    filters=[react_filter],
    output='beerlist.js'
)
