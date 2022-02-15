# Protobuf repository example: pip installable

This small repository is designed as an example of how to solve the common case
of wanting a protobuf schema repository shared between multiple microservices.
This works out of the box for most languages, but due to the issues discussed in
[protobuf/1491](https://github.com/protocolbuffers/protobuf/issues/1491), it is
tricky to accomplish for Python services.

Using this method, you can keep your schema repository as is (see the contents
of `example_proto/`, adding only minimal Python packaging artifacts to the top
level. This will allow you to install (and automatically compile) the Python
generated code with `pip install /path/to/this/repo`. For example:

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv) $ pip install 'git+https://github.com/sbrother/python-protobuf-repo-example'
(venv) $ python
>>> from example_proto.food_pb2 import Food
>>> # success!
```

Under the hood this uses a
[custom setuptools command](https://github.com/sbrother/protobuf-custom-build).
