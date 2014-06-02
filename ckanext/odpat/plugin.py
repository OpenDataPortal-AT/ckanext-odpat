import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.odpat.lib.dgvat_helper as dgvat_helper

import logging


log = logging.getLogger(__name__)

class OdpatPortalPlugin(plugins.SingletonPlugin):
    '''theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):

        # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'public')

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')


class OdpatDatasetFormPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    '''Dataset Form.

    '''
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IRoutes)

    def before_map(self, map):
        log.fatal('before map')

        return map

    def after_map(self, map):
        log.fatal('after map')
        return map

    def get_helpers(self):
        log.fatal('get Helpers')
        return { 'categories': dgvat_helper.categorization, 'frequencies': dgvat_helper.update_frequency }

    def _modify_package_schema(self, schema):
        schema.update({
            'schema_name': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'maintainer_link': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'schema_language': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'schema_characterset': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'date_released': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'begin_datetime': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'end_datetime': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'metadata_linkage': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'attribute_description': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'publisher': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'geographic_toponym': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'geographic_bbox': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'lineage_quality': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'en_title_and_desc': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'license_citation':[toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'metadata_identifier':[toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'metadata_modified':[toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'date_updated':[toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'publishing_date':[toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'publishing_state':[toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'log_message': [toolkit.get_validator('ignore_missing')],
            'update_frequency': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'categorization': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')]
        })

        schema['resources'].update({
                    'language':[toolkit.get_validator('ignore_missing')],
                    'characterset':[toolkit.get_validator('ignore_missing')]
                })
        return schema

    def create_package_schema(self):
        schema = super(OdpatDatasetFormPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(OdpatDatasetFormPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(OdpatDatasetFormPlugin, self).show_package_schema()
        # schema.update({
        #     'schema_name': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'maintainer_link': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'schema_language': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'schema_characterset': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'date_released': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'begin_datetime': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'end_datetime': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'metadata_linkage': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'attribute_description': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'publisher': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'geographic_toponym': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'geographic_bbox': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'lineage_quality': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'en_title_and_desc': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'license_citation': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'metadata_identifier': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'metadata_modified': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'date_updated': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'publishing_date': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'publishing_state': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'log_message': [toolkit.get_validator('ignore_missing')],
        #     'update_frequency': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')],
        #     'categorization': [toolkit.get_converter('convert_from_extras'), toolkit.get_validator('ignore_missing')]

        # })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
