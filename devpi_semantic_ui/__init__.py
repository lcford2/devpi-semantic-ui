try:
    # Python 3.9+
    from importlib.resources import files
except ImportError:
    # Fallback for older Python versions
    from pkg_resources import resource_filename

from .__about__ import __version__, __description__


def devpiserver_cmdline_run(xom):
    '''
    Load theme when `theme` parameter is 'semantic-ui'.
    '''
    if xom.config.args.theme == 'semantic-ui':
        try:
            # Modern approach using importlib.resources
            xom.config.args.theme = str(files('devpi_semantic_ui'))
        except NameError:
            # Fallback for systems without importlib.resources
            xom.config.args.theme = resource_filename('devpi_semantic_ui', '')
        xom.log.info("Semantic UI Theme loaded")


def devpiserver_pyramid_configure(config, pyramid_config):
    '''Perform Pyramid level configuration'''
    pyramid_config.include('devpi_semantic_ui')


def includeme(config):
    config.add_route('searchapi', '/+search', accept='application/json')
    config.scan()
