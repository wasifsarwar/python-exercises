def get_ok_items(carryon, personal, restricted):
    all_items = carryon.union(personal)
    ok_items = all_items - restricted
    return ok_items