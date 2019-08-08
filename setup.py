from distutils.core import setup

setup(
    name="Marshmallow stubs",
    url=None,
    author='Lev Subbotin',
    author_email='grander.stark@yandex.ru',
    version="0.1",
    package_dir={'': 'package'},
    package_data={"marshmallow": ["__init__.pyi", "exceptions.pyi", "fields.pyi"]},
    packages=[
        "marshmallow"
    ]
)