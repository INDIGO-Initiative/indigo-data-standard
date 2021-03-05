import io
import os
import json
from jsonpointer import resolve_pointer
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from compiletojsonschema.compiletojsonschema import  CompileToJsonSchema


class DataDictionaryDirective(SphinxDirective):
    option_spec = {
        'schema': directives.unchanged,
        'path': directives.unchanged,
    }

    def run(self):

        schema = CompileToJsonSchema(
            os.path.join(self.config['schema_dir_path'], self.options.get('schema')),
            codelist_base_directory=self.config['codelist_dir_path']
        ).get()

        fields_to_show = []
        for path in [i.strip() for i in self.options.get('path').split(',') if i.strip()]:
            fields_to_show.extend(self._get_fields_worker(schema, path))


        tgroup = nodes.tgroup(cols=3)
        for i in range(3):
            tgroup += nodes.colspec(colwidth=1)

        table = nodes.table('', tgroup)
        header_row = nodes.row()

        for header in ['Name', 'Definition', 'Type']:
            header_row += self._cell(header)

        tgroup += nodes.thead('', header_row)
        tbody = nodes.tbody()
        tgroup += tbody
        for data in fields_to_show:
            row = nodes.row()
            # Title
            row += self._cell(data['title'])
            # Description
            content = [data['description']]
            if data['type'] == 'string' and data['codelistDescription']:
                content.append('Codelist options are:')
                content.append(data['codelistDescription'])
            elif data['type'] == 'string' and data['enum']:
                content.append('Codelist options are:')
                list = nodes.bullet_list()
                for option in data['enum']:
                    list += nodes.list_item('', nodes.Text(option))
                content.append(list)
            row += self._cell(content)
            # Type
            if data['type'] == 'number':
                row += self._cell("Number")
            elif data['type'] == 'string' and data['patternHint']:
                row += self._cell(data['patternHint'])
            elif data['type'] == 'string' and (data['codelistDescription'] or data['enum']):
                content = ['Codelist']
                row += self._cell(content)
            elif data['type'] == 'string':
                row += self._cell('Text')
            else:
                row += self._cell('')

            tbody += row

        return [table]

    def _cell(self, contents):
        entry = nodes.entry()
        if not isinstance(contents, list):
            contents = [contents]
        for content in contents:
            if isinstance(content, str):
                entry += nodes.paragraph('', nodes.Text(content))
            else:
                entry += content
        return entry

    def _get_fields_worker(self, json_schema, start_pointer, title='', last_description=''):
        out = []
        our_json_schema = resolve_pointer(json_schema, start_pointer)
        if our_json_schema.get("type") == "object":
            for key in our_json_schema.get("properties").keys():
                out.extend(
                    self._get_fields_worker(
                        json_schema=json_schema,
                        start_pointer=start_pointer + "/properties/" + key,
                        title=self._join_title(title, our_json_schema.get("title", "")),
                        last_description= our_json_schema.get("description", "") or last_description
                    )
                )
        elif our_json_schema.get("type") in ["string", "number"]:
            if not start_pointer.endswith('/status'):
                out.append(
                    {
                        "title": self._join_title(title, our_json_schema.get("title", "")),
                        "description": our_json_schema.get("description") or last_description,
                        "type": our_json_schema.get("type"),
                        "enum": our_json_schema.get("enum"),
                        "patternHint": our_json_schema.get("patternHint"),
                        "codelistDescription": our_json_schema.get("codelistDescription"),
                    }
                )
        return out

    def _join_title(self, bit1, bit2):
        if bit1 and bit2:
            return bit1.strip() + " - " + bit2.strip()
        elif bit1:
            return bit1.strip()
        elif bit2:
            return bit2.strip()
        else:
            return ""


def setup(app):
    app.add_config_value('schema_dir_path', default=None, rebuild='html')
    app.add_config_value('codelist_dir_path', default=None, rebuild='html')
    app.add_directive('datadictionary', DataDictionaryDirective)
    return {}

