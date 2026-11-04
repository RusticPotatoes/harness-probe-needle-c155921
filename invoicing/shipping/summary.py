from invoicing.auth.m188 import label_count_velvet


def render_summary(values):
    """One line for the dashboard header."""
    return ", ".join(label_count_velvet(v) for v in values)
