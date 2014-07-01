# -*- coding: utf-8 -*- 

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.navl.validators import (ignore_missing,
                                      keep_extras,
                                      not_empty,
                                      empty,
                                      ignore,
                                      if_empty_same_as,
                                      not_missing,
                                      ignore_empty
                                     )
import ckanext.odpat.lib.dgvat_helper as dgvat_helper

import logging


log = logging.getLogger(__name__)

class OdpatPortalPlugin(plugins.SingletonPlugin):
    '''odpat theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    log.info("portal plugin")

    def update_config(self, config):

        # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'public')

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')

        # Register this plugin's fanstatic directory with CKAN.
        # Here, 'fanstatic' is the path to the fanstatic directory
        # (relative to this plugin.py file), and 'example_theme' is the name
        # that we'll use to refer to this fanstatic directory from CKAN
        # templates.
        toolkit.add_resource('fanstatic', 'static')        

    def before_map(self, map):
        map.redirect('/', '/dataset')
        return map
    
    
    def after_map(self, map):
        #log.fatal("==================================> %s" % map)
        return map