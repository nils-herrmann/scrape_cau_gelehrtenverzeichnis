"""Utility functions for parsing data."""
from typing import Optional
from lxml.etree import _Element

def get_text(node: Optional[_Element],
             path: str,
             namespaces: Optional[dict]) -> Optional[str]:
    """Get the text of an XML node."""
    if node is not None:
        if node.find(path, namespaces) is not None:
            return node.find(path, namespaces).text
    return None


def determine_qp_type(qp_types_list):
    """Determine qualification type"""
    for qp_type in qp_types_list:
        if 'Dissertation' in qp_type:
            return 'Dissertation'
        elif 'HabilitationTreatise' in qp_type:
            return 'Habilitation'
