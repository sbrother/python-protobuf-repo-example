import setuptools
import distutils.command.build

distutils.command.build.build.sub_commands.append(('protobuf-custom-build', None))

setuptools.setup()
