from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from pv_plugingg.schema_packages.schema_package import m_package

        return m_package


class lab1PackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from pv_plugingg.schema_packages.lab1_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)


lab1_schema_package_entry_point = lab1PackageEntryPoint(
    name='lab1Package',
    description='lab1 package entry point configuration.',
)
