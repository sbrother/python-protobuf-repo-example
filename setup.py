import setuptools
import distutils.command.build

distutils.command.build.build.sub_commands.insert(0, ('protobuf-custom-build', None))

setuptools.setup()
