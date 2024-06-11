"""
this is the package sphinxcontrib.console.
"""

from typing import Dict
from typing import Any
from sphinx.application import Sphinx

from .excel import ExcelDirective

def setup(application: Sphinx) -> Dict[str, Any]:
    """
    setup extension.
    """
    application.add_directive('excel', ExcelDirective)
    return {"version": (0,1,0), "parallel_read_safe": True}
