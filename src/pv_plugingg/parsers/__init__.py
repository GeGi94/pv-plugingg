from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from pv_plugingg.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class lab1ExperimentParserEntryPoint(ParserEntryPoint):

    def load(self):
        from pv_plugingg.parsers.lab1_batch_parser import lab1ExperimentParser

        return lab1ExperimentParser(**self.model_dump())


class lab1ParserEntryPoint(ParserEntryPoint):

    def load(self):
        from pv_plugingg.parsers.lab1_measurement_parser import lab1Parser

        return lab1Parser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


lab1_experiment_parser_entry_point = lab1ExperimentParserEntryPoint(
    name='lab1ExperimentParserEntryPoint',
    description='lab1 experiment parser entry point configuration.',
    mainfile_name_re='^(.+\.xlsx)$',
    mainfile_mime_re='(application|text|image)/.*',
)


lab1_parser_entry_point = lab1ParserEntryPoint(
    name='lab1ParserEntryPoint',
    description='lab1 parser entry point configuration.',
    mainfile_name_re='^.+\.?.+\.((eqe|jv|mppt)\..{1,4})$',
    mainfile_mime_re='(application|text|image)/.*',
)
