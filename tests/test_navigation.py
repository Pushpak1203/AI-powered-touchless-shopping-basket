# tests/test_navigation.py

import pytest
from navigation import get_current_section_from_distance

def test_following_customer():
    assert get_current_section_from_distance(30) == "Following Customer"

def test_adjusting_distance():
    assert get_current_section_from_distance(100) == "Adjusting"

def test_stopped():
    assert get_current_section_from_distance(200) == "Stopped"
