show = [
    # Show Capacity
    'document.getElementById("SearchResults_column_toggler").getElementsByClassName("checker")['
    '12].firstChild.firstChild.click();',

    # Show Used Capacity
    'document.getElementById("SearchResults_column_toggler").getElementsByClassName("checker")['
    '13].firstChild.firstChild.click();',
]


def get_index(key_code: str) -> str:
    return f"""
    x = document.getElementById("SearchResults");
        for (var i = 0, row; row = x.rows[i]; i++){"{"}
            if (x.rows[i].getAttribute('key')=="{key_code}"){"{"}
                return (x.rows[i]._DT_RowIndex);
            {"}"}
        {"}"}
    """


def get_data(class_index: int) -> list:
    # Get name & capacity & used capacity info for specified class & section
    return [f'return document.getElementById("SearchResults").rows[{class_index}].getAttribute("key")',
            f'return document.getElementById("SearchResults").rows[{class_index}].children[6].textContent',
            f'return document.getElementById("SearchResults").rows[{class_index}].children[7].textContent', ]
