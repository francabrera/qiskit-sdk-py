from setuptools import setup

packages = ["qiskit",
            "qiskit.dagcircuit",
            "qiskit.extensions",
            "qiskit.extensions.standard",
            "qiskit.mapper",
            "qiskit.qasm",
            "qiskit.qasm._node",
            "qiskit.simulators",
            "qiskit.unroll"]

requierments = ["IBMQuantumExperience>=1.8",
                  "requests>=2.18,<2.19",
                  "networkx>=1.11,<1.12",
                  "ply==3.10",
                  "numpy>=1.13,<1.14",
                  "scipy>=0.19,<0.20",
                  "matplotlib>=2.0,<2.1"]

setup(
    name="qiskit",
    version="0.3",
    description="IBM QISKit SDK",
    long_description="""Python software development kit (SDK) and Jupyter
notebooks for working with OpenQASM and the IBM Q experience (QX).""",
    url="https://github.com/IBM/qiskit-sdk-py",
    author="IBM Research - Q Team",
    author_email="atilag@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.x",
        "Topic :: Software Development :: SDK",
        "Topic :: Scientific",
        "Programming Language :: Python :: 3",
    ],
    keywords="qiskit sdk quantum",
    packages=packages,
    install_requires=requierments,
    python_requires=">3.0",
)
