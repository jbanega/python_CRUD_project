from setuptools import setup

setup(
    name="miEmpresa",
    version="0.1",
    py_modules="miEmpresa",
    install_requires=[
        "Click",
    ],
    entry_points="""
            [console_scripts]
            miEmpresa=miEmpresa:cli
    """,
)