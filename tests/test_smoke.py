import cnstats

def test_import():
    assert cnstats is not None
    print("\nSuccessfully imported cnstats")

def test_version():
    # Simple check if we can access some attributes if they exist
    # Since I don't know the exact internal structure deeply yet, 
    # just confirming the package is findable.
    import cnstats.zbcode
    assert cnstats.zbcode is not None
