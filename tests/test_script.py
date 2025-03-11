# tests/test_script.py
import pytest

# Assuming animation functions are in script.js
# and the index.html includes necessary elements and script import


@pytest.mark.parametrize("element_id", ["animatedElement"]) # Example
def test_animation_exists(element_id):
    # This test is meant to be a high-level test
    # that confirms the existence of the animation effect.
    # If we use JS for example, we check the element exists
    # and that the animation css class is available
    with open("index.html", "r") as f:
        html_content = f.read()

    assert f'<div id="{element_id}"' in html_content, f"Element with id '{element_id}' not found in index.html"
    # To check animation class, check style.css or the inline styles of index.html
    with open("style.css", "r") as f:
        css_content = f.read()

    assert ".animation" in css_content or f"#{element_id}.animation" in html_content, "Animation class not found in style.css or inline styles"

@pytest.mark.parametrize("element_id", ["animatedElement"])
def test_animation_runs(element_id, script_js):
    # This is a more detailed test.
    # It checks whether the animation is actually running,
    # maybe by checking if a css property is changing at all (or over time if possible)
    # For example, let's assume a simple animation that changes the element's position

    # The test should check the value of a certain element
    # Maybe the element's style.left property increases over time
    # Check it's getting some values
    assert False, "Animation not implemented yet"



