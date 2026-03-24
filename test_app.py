import pytest
from app import app

# Test 1: Header exists
def test_header():
    layout = app.layout
    assert "header" in str(layout)

# Test 2: Graph exists
def test_graph():
    layout = app.layout
    assert "sales-chart" in str(layout)

# Test 3: Radio button exists
def test_radio_button():
    layout = app.layout
    assert "region-filter" in str(layout)