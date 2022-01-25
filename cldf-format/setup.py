from setuptools import setup


setup(
    name='cldfbench_steinertthrelkeldmodals',
    py_modules=['cldfbench_steinertthrelkeldmodals'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'modals=cldfbench_steinertthrelkeldmodals:Dataset',
        ],
        'cldfbench.commands': [
            'modals=modalscommands',
        ],
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
