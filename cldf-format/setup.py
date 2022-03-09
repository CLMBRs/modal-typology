from setuptools import setup


setup(
    name='cldfbench_modaltypology',
    py_modules=['cldfbench_modaltypology'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'modals=cldfbench_modaltypology:Dataset',
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
